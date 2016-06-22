#### 写在前面

SQLAlchemy不是一个应用软件，而是一个Python Library。库的一个特点是，为了给用户提供友好的语法，常常会使用一些语言的高级特性。SQLAlchemy也不例外，源代码中大量涉及到Python的反射（自省），并使用了描述符（descriptor）等高级语言特性，给阅读源代码造成了一定困难。

本调研笔记中的相当一部分内容参考自SQLAlchemy在线文档。

## 20.2 核心层与ORM层

原文中已经给出了SQLAlchemy的两个层次的关系图：

![Figure 20.1][fig1]

SQLAlchemy的两个最主要的功能点就是**对象-关系映射（ORM）**和**SQL表达式语言**。SQL表达式语言可以独立于ORM使用。而当用户使用ORM时，SQL表达式语言在背后工作，但用户也可以通过开放的API操纵SQL表达式语言的行为。

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


## 20.3 改良DBAPI

首先，我们要理解什么是DBAPI，以下内容引用自SQLAlchemy文档的术语表：

> DBAPI是“Python数据库API规范”（Python Database API Specification）的简称。这是在Python中广泛使用的规范，定义了数据库连接的第三方库的使用模式。DBAPI是一个低层的API，在一个Python应用中基本上位于最底层，和数据库直接进行交互。SQLAlchemy的方言系统按照DBAPI的操作来构建。基本上，一个方言就是DBAPI加上一个特定的数据库引擎。通过在`create_engine()`函数中提供不同的数据库URL可以将方言绑定到不同的数据库引擎上。 
>
> 参见： [PEP 249 - Python Database API Specification v2.0](http://www.python.org/dev/peps/pep-0249/)
>
> —— [SQLAlchemy文档 - 术语表 - DBAPI](http://docs.sqlalchemy.org/en/rel_1_0/glossary.html#term-dbapi)


PEP的文档介绍比较枯燥，我们可以通过这个示例代码直观地理解DBAPI的使用模式：

```Python
connection = dbapi.connect(user="root", pw="123456", host="localhost:8000")
cursor = connection.cursor()
cursor.execute("select * from user_table where name=?", ("jack",))
print "Columns in result:", [desc[0] for desc in cursor.description]
for row in cursor.fetchall():
    print "Row:", row
cursor.close()
connection.close()
```

作为对比，SQLAlchemy的使用模式是这样的：

```Python
engine = create_engine("postgresql://user:pw@host/dbname")
connection = engine.connect()
result = connection.execute("select * from user_table where name=?", "jack")
print result.fetchall()
connection.close()
```

可以看到，二者的使用模式非常相似，都是直接通过SQL语句进行查询。SQLAlchemy只进行了封装，但没有进行高层次的抽象。不过，这只是SQLAlchemy最简单的使用方式，后面会看到，使用SQL表达式语言可以进行抽象性很高的描述，不需要手写SQL语句。

原文中给出了SQLAlchemy方言系统核心类的关系图：

![Figure20.2][fig2]

对照原文中的描述，阅读源代码：

> `Engine`、`Connection`两个类的`execute`方法返回的结果是一个`ResultProxy`，它提供了一个与DBAPI的游标类似但功能更丰富的接口。`Engine`，`Connection`和`ResultProxy`分别对应于DBAPI模块、一个具体的DBAPI连接对象，和一个具体的DBAPI游标对象。
>
> 在底层，`Engine`引用了一个叫`Dialect`的对象。`Dialect`是一个有众多实现的抽象类，它的每一个实现都对应于一个具体的DBAPI和数据库。一个为`Engine`而创建的`Connection`会咨询`Dialect`作出选择，对于不同的目标DBAPI和数据库，`Connection`的行为都不一样。
>
> `Connection`创建时会从一个连接池获取并维护一个DBAPI的连接，这个连接池叫`Pool`，也和`Engine`相关联。`Pool`负责创建新的DBAPI连接，通常在内存中维护DBAPI连接池，供频繁的重复使用。
>
> 在一个语句执行的过程中，`Connection`会创建一个额外的`ExecutionContext`对象。这个对象从开始执行的时刻，一直存在到`ResultProxy`消亡为止。

#### Engine和Connection

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

> 数据库模式是用形式化的语言描述的数据库系统的结构。在关系数据库中，模式定义了表、表中字段，以及表和字段间的关系
>
> —— [Webopedia](http://www.webopedia.com/TERM/S/schema.html)

直观来说，下面的SQL语句就描述了一个数据库的模式：

```SQL
CREATE TABLE users (
    id INTEGER NOT NULL,
    name VARCHAR,
    fullname VARCHAR,
    PRIMARY KEY (id)
);

CREATE TABLE addresses (
    id INTEGER NOT NULL,
    user_id INTEGER,
    email_address VARCHAR NOT NULL,
    PRIMARY KEY (id),
    FOREIGN KEY(user_id) REFERENCES users (id)
);
```

SQLAlchemy的模式定义功能就是用一种抽象的方式表达上面SQL语句的内容。下面的代码定义了和上面SQL语句相同的模式：

```Python
metadata = MetaData()

users = Table('users', metadata,
        Column('id', Integer, primary_key=True),
        Column('name', String),
        Column('fullname', String),
)
addresses = Table('addresses', metadata,
        Column('id', Integer, primary_key=True),
        Column('user_id', None, ForeignKey('users.id')),
        Column('email_address', String, nullable=False),
)

metadata.create_all(engine)
```

我们知道，SQL语言一共分为四大类：DDL，DML，DQL，DCL。DCL和具体的DBMS相关，这里不涉及。剩下的三类中，DDL和DML/DQL有很大的区别。上面的`CREATE TABLE`语句即属于DDL。对于DDL，SQLAlchemy使用Metadata进行抽象，而对于DML和DQL，SQLAlchemy使用SQL表达式语言进行抽象。

## 20.5 SQL表达式

SQLAlchemy的作者Mike Bayer在文章中指出，SQL表达式语言使用了Martin Fowler在*Patterns of Enterprise Application Architecture*书中的**查询对象**(Query Object)模式。Martin Fowler在书中是这么描述这个模式的：

> SQL是一个演化中的语言，很多开发人员对它不是非常熟悉。而且，你在写查询语句的时候需要知道数据库schema是什么样的。查询对象模式可以解决这些问题。
>
> 查询对象是一个解释器模式(Interpreter Pattern)，也就是一个对象可以把自己变成一个SQL查询。你可以通过使用类和属性，而不是表和字段来创建一条查询。用这种方法，你在写查询语句时可以不依赖数据库schema，对schema的改变也不会造成全局的影响。

Mike Bayer指出，SQL表达式的创建主要使用了**Python表达式**和**重载的操作符**。

sqlalchemy.sql.dml.Insert是UpdateBase的子类，而UpdateBase同时是ClauseElement和Executable的子类，所以可以将Insert的实例传给Connection.execute()

select是一个全局的函数，而不是类。在sql/expression.py中，调用public_factory，将selectable.Select类变为函数select，也就是将
`Select.__init__()`赋值给select。

--- 

# 参考资料

+ [SQLAlchemy 1.0 官方文档](http://docs.sqlalchemy.org/en/rel_1_0/index.html)
+ [Mike Bayer: SQLAlchemy所实现的模式](http://techspot.zzzeek.org/2012/02/07/patterns-implemented-by-sqlalchemy/)
+ [Mike Bayer: SQLAlchemy架构回顾](http://techspot.zzzeek.org/files/2011/sqla_arch_retro.key.pdf)

<!-- 以下内容不要删除 -->

[fig1]: https://raw.githubusercontent.com/nettee/SQLAlchemy-survey/master/picture/layers.png
[fig2]: https://raw.githubusercontent.com/nettee/SQLAlchemy-survey/master/picture/engine.png
[fig3]: https://raw.githubusercontent.com/nettee/SQLAlchemy-survey/master/picture/dialect-simple.png
[fig4]: https://raw.githubusercontent.com/nettee/SQLAlchemy-survey/master/picture/common-dbapi.png
[fig5]: https://raw.githubusercontent.com/nettee/SQLAlchemy-survey/master/picture/basic-schema.png
[fig6]: https://raw.githubusercontent.com/nettee/SQLAlchemy-survey/master/picture/table-column-crossover.png
[fig7]: https://raw.githubusercontent.com/nettee/SQLAlchemy-survey/master/picture/expression-hierarchy.png
[fig8]: https://raw.githubusercontent.com/nettee/SQLAlchemy-survey/master/picture/example-expression.png
[fig9]: https://raw.githubusercontent.com/nettee/SQLAlchemy-survey/master/picture/compiler-hierarchy.png
[fig10]: https://raw.githubusercontent.com/nettee/SQLAlchemy-survey/master/picture/statement-compilation.png
[fig11]: https://raw.githubusercontent.com/nettee/SQLAlchemy-survey/master/picture/mapper-components.png
[fig12]: https://raw.githubusercontent.com/nettee/SQLAlchemy-survey/master/picture/query-loading.png
[fig13]: https://raw.githubusercontent.com/nettee/SQLAlchemy-survey/master/picture/session-overview.png
[fig14]: https://raw.githubusercontent.com/nettee/SQLAlchemy-survey/master/picture/topological-sort.png
[fig15]: https://raw.githubusercontent.com/nettee/SQLAlchemy-survey/master/picture/uow-mapper-buckets.png
[fig16]: https://raw.githubusercontent.com/nettee/SQLAlchemy-survey/master/picture/uow-element-buckets.png