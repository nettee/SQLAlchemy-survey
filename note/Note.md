SQLAlchemy 1.0版本共有272353行Python代码，929个类。而且由于Python的语法灵活，函数和类都可以作为一个对象进行传递，在SQLAlchemy的源代码中大量使用Python高阶函数和反射（自省）特性，给阅读源代码造成了一定困难。本调研笔记中的相当一部分内容来自源代码中的注释与SQLAlchemy在线文档。

## 20.2 核心层与ORM层

在理解SQLAlchemy的分层之前，首先要明确SQLAlchemy的定位，SQLAlchemy工作在DBAPI上，是一个抽象层次更高的系统。在应用中使用SQLAlchemy处理关系数据库的时候，从上到下有这样几个层次：

1. SQLAlchemy ORM层
2. SQLAlchemy Core层
3. DBAPI
4. DBMS

我们假设用户使用了SQLite数据库。SQLite是一个DBMS（数据库管理系统），位于架构中的最底层。

Python中与SQLite进行交互的模块叫做pysqlite，由于SQLite数据库较为流行，pysqlite已经加入Python标准库中，名为[sqlite3][pythonlib-sqlite3]。

[pythonlib-sqlite3]: https://docs.python.org/3/library/sqlite3.html

pysqlite遵循DBAPI规范，[DBAPI][DBAPI]定义了Python访问数据库的通用接口，规定了Connection, Cursor等对象的行为和方法，不同的数据库厂商开发Python与数据库交互的模块时，都遵循DBAPI，这样Python程序就不需要考虑底层数据库的实现细节。在DBAPI这一层，已经进行了一次封装和抽象。

[DBAPI]: https://www.python.org/dev/peps/pep-0249/


## 20.3 驯服DBAPI

上文提到过，SQLAlchemy核心层是构建在DBAPI之上的。那么首先我们要弄清楚SQLAlchemy核心层是怎么通过DBAPI进行数据库连接和交互的。回顾图20.2中的示意图：

![Figure 20.2](https://raw.githubusercontent.com/nettee/SQLAlchemy-survey/master/picture/engine.png)

这六个都是SQLAlchemy处理DBAPI的关键类，但用户代码在最简单的情况下只会使用到`Engine`, `Connection`, `ResultProxy`三个类，`Pool`, `Dialect`和`ExecutionContext`类则是隐藏在幕后的。一个简单的示例代码如下：

```Python
from sqlalchemy import *
engine = create_engine('sqlite:///:memory:', echo=True)
connection = engine.connect()
result = connection.execute('select * from table')
for row in result:
    print row
```

#### Engine和Connection

`Engine`是SQLAlchemy应用的入口点，是DBAPI的封装。但`Engine`并不直接处理DBAPI，而是在内部保存了`Pool`和`Dialect`的引用，用`Pool`处理数据库连接，用`Dialect`处理数据库行为。总体的结构如下图所示：

![Figure: engine architecture](http://docs2.sqlalchemy.org/en/latest/_images/sqla_engine_arch.png)

全局函数`create_engine`用来创建`Engine`对象，这个函数的第一个参数是一个数据库URL，还有一些关键字参数，用来控制`Engine`，`Pool`和`Dialect`对象的特性。其中关键字参数strategy用于指定创建`Engine`时的策略。函数会从全局的`strategies`字典中查找对应的策略（`EngineStrategy`的一个子类），将自己的参数传入策略类的`create`方法。如果strategy参数没有提供，则使用默认策略`DefaultEngineStrategy`。观察每个`EngineStrategy`子类的`create`方法，发现它们都会在创建`Engine`对象之前先创建`Dialect`对象和`Pool`对象，并将这两个对象的引用保存在`Engine`对象中，保证了`Engine`对象可以通过`Dialect`和`Pool`处理DBAPI。

`Connection`类看起来比`Engine`类更加强大。`Engine.connect()`方法用于创建`Connection`：

```Python
_connection_cls = Connection

def connect(self, **kwargs):
    return self._connection_cls(self, **kwargs)
```

调用`Engine.connect()`实际上是将`Engine`对象自己作为第一个参数传入了`Connection`的构造函数，但`Connection`的构造函数还要调用`Engine.raw_connection()`方法获得数据库连接。这样做主要是为了方便`Engine`的隐式执行接口。在`Connection`没有创建的时候，`Engine`也可以自己调用`raw_connection()`获得数据库连接。

不论怎样，`Connection`拥有`Engine`的引用，并可以通过`Engine`的访问`Pool`和`Dialect`对象。对数据库的操作通常是使用`Connection.execute()`方法进行的。

#### Pool

`Pool`负责管理DBAPI连接。`Connection`对象创建时，会从连接池中取出一个DBAPI连接，而在`close`方法调用时，会将连接归还。

`Pool`的代码定义在`pool.py`中，包括抽象父类`Pool`，和几个有具体功能的子类：

+ `QueuePool` 限制连接个数（默认使用）
+ `SingletonThreadPool` 为每个线程维护一个连接
+ `AssertionPool` 任何时候都只允许一个连接，否则抛出异常
+ `NullPool` 不进行任何池操作，直接打开/关闭DBAPI连接
+ `StaticPool` 有且仅有一个连接

#### 执行SQL语句

`Connection`的`execute`方法执行一个SQL语句，并返回一个`ResultProxy`对象。`execute`方法接受多种类型的参数，参数类型可以是一个字符串，也可以是`ClauseElement`和`Executable`的共同子类。关于`execute`方法的参数在下文中详细讨论，这里主要分析`execute`方法执行时背后的过程。

```Python
def execute(self, object, *multiparams, **params):
    if isinstance(object, util.string_types[0]):
        return self._execute_text(object, multiparams, params)
    try:
        meth = object._execute_on_connection
    except AttributeError:
        raise exc.InvalidRequestError(
        "Unexecutable object type: %s" %
        type(object))
    else:
        return meth(self, multiparams, params)
```

可以看到，`execute`方法对SQL语句对象的类型进行判断，如果是一个字符串，则调用`_execute_text`方法执行，否则调用对象的`_execute_on_connection`方法，而不同对象的`_execute_on_connection`方法会调用`Connection._execute_*()`方法，具体为：

+ `sql.FunctionElement`对象，调用`Connection._execute_function()`
+ `schema.ColumnDefault`对象，调用`Connection._execute_default()`
+ `schema.DDL`对象，调用`Connection._execute_ddl()`
+ `sql.ClauseElement`对象，调用`Connection._execute_clauseelement()`
+ `sql.Compiled`对象，调用`Connection._execute_compiled()`

以上的`Connection._execute_*()`方法都调用了`Connection._execute_context()`方法。这个方法的第一个参数是`Dialect`对象，第二个参数是`ExecutionContext`对象的构造器（构造器从`Dialect`对象获取）。在方法中调用构造器构造了一个`ExecutionContext`对象，并根据context对象的状态调用dialect对象的相关方法产生结果。对不同的状态，调用的dialect对象的方法不同，总的来说，调用的是`Dialect.do_execute*()`方法。

从上述方法调用的过程可以看出，`Connection`的`execute`方法最终将生成结果的任务转交给了`Dialect`的`do_execute`方法。SQLAlchemy正是用这种方法应对多变的DBAPI实现的：`Connection`在执行SQL语句的时候，会咨询`Dialect`作出选择。因此对于不同的目标DBAPI和数据库，`Connection`的行为都不一样。

#### Dialect

`Dialect`定义在engine/interfaces.py文件中，是一个抽象的接口，其中定义了三个`do_execute*()`方法，分别是`do_execute()`，`do_executemany()`和`do_execute_no_params()`。`Dialect`的子类通过实现这些接口来定义自己执行时的行为。SQLAlchemy中默认的dialect子类是`DefaultDialect`。在默认实现中，`do_execute`方法调用`Cursor.execute`，而`Cursor`是来自DBAPI的类。在这里，SQLAlchemy核心层和DBAPI层连接了起来。

`sqlalchemy.dialects`包中包含有来自firebird，mssql，mysql，oracle，postgresql，sqlite，sybase等数据库的dialect。以SQLite数据库为例，`SQLiteDialect`继承自`DefaultDialect`，而`SQLiteDialect_pysqlite`和`SQLiteDialect_pysqlcipher`。SQLite的dialect没有重写`do_execute*()`，而是重写了一些其他的方法，来定义一些和`DefaultDialect`不同的行为。例如，SQLite没有内置的DATE，TIME，DATETIME类型，`SQLiteDialect`处理了这些问题。

#### ResultProxy

`ResultProxy`包装了一个DBAPI游标(cursor)对象，使一行结果中的各个字段更容易访问。在数据库术语中，结果通常称为一个行(row)。

一个字段可以通过三种方式访问：

```Python
row = fetchone()
col1 = row[0] # 通过位置下标访问
col2 = row['col2'] # 通过名字访问
col3 = row[mytable.c.mycol] # 通过Column对象访问
```

ResultProxy定义了`__iter__`方法，可以在ResultProxy对象上使用for循环，效果和不断调用fetchone方法一样：

```Python
def __iter__(self):
    while True:
        row = self.fetchone()
        if row is None:
            return
        else:
            yield row
```



## 20.4 模式定义

sqlalchemy.sql.dml.Insert是UpdateBase的子类，而UpdateBase同时是ClauseElement和Executable的子类，所以可以将Insert的实例传给Connection.execute()

select是一个全局的函数，而不是类。在sql/expression.py中，调用public_factory，将selectable.Select类变为函数select，也就是将
`Select.__init__()`赋值给select。

