#SQLAlchemy
迈克·贝尔
SQLAlchemy是一个数据库工具包和基于Python语言的对象关系映射系统，在2005年被第一次介绍。最开始的时候，它追求在Python中提供一个端到端的系统来使用关系数据库，即用于数据库交互的API是可以直接被Python调用的。即使在SQLAlchemy发展的早期阶段，它的性能就吸引了很多关注。它的关键特征包括大量的对复杂数据库查询和对象映射的流畅处理，还有一个关于“工作单元”模式的实现，这个模式为数据库提供了一个高度自动化的可持续存储数据的系统。

SQLAlchemy从一个小的、粗糙定义的概念开始，通过一系列的转变和改进迅速发展起来，尽管它的用户群不断增大，但它仍在反复考虑对它内部架构以及外部接口的优化。到2009年1月，SQLAlchemy的0.5版本出来的时候，它已经开始假设一个可以证明ta处于多种产品部署的稳定形态了。通过0.6（2010年4月）和0.7版本（2011年5月），SQLAlchemy的架构和接口的进步增大了它达到最有效率且最稳定的系统的可能。从写这篇文章开始，SQLAlchemy正被大量的组织在不同领域使用着，并被许多以事实为评判标准的Python关系型数据库人员所考虑。

##20.1. 数据库抽象的挑战
术语“数据库抽象”经常用来假定表示一个数据库通信系统，这个系统隐藏了主要的关于数据如何被存储和查询的细节。这个术语有时被带入一个极端，即这样一个系统不应该仅仅隐藏在使用中的关系数据库的细节，还应该隐藏数据库中的关系型结构的细节，甚至隐藏潜在的数据存储是否是关系型的。

最普遍的关于对象关系映射系统的评论集中在一个假设上：这样的工具的主要目的是“隐藏”对关系型数据库的使用，掌握生成与数据库交互的任务以及把这个任务简化到一些实现细节上来。这个隐藏办法的中心是将设计和查询关系型结构的能力从开发人员那里拿走并交给一个不透明的黑箱子处理。

那些深入了解关系型数据库的人知道这个方法是完全不切实际的。这个方法想使关系结构和数据库查询被极大地功能化，并包含应用核心的设计。然而这些结构在不同种类的查询（不仅仅是在需求的数据上的不同，还包括在想要的信息结构上的不同）中，应该怎样被设计、组织和操作呢？如果这个方面相关的具体设计使用被隐藏了，那么在最开始使用一个关系型数据库就没有任何意义。

这个对潜在关系数据库的隐藏的追求和关系型数据库本身的需求的巨大差异经常被称为“对象关系阻抗失配”问题。而SQLAlchemy多少为这个问题带来了新的解决方法。

####SQLAlchemy对数据库抽象的方法
SQLAlchemy主张开发者必须乐意考虑他/她的数据的关系形式。一个预决定和隐藏模式、查询设计决策的系统排斥使用一个关系型数据库的有用性，导致所有的阻抗失配的经典问题。

同时，这些决策的实现能够且应该通过水平尽可能高的模式来执行。关联对一个模式来说的对象模型且通过SQL查询来保持它，是一项重复性很高的任务。允许一些工具来自动化这些任务需要一个应用的开发，这个应用应该更简洁、更有能力且效率更高，并且在手动开发这些操作的过程中创建这个应用只需占用一小部分时间。

为了这个目的，SQLAlchemy自称它是一个工具包，来强调开发者作为所有关系型结构和这些结构与这个应用的联系的设计者/架构师的角色，而不是作为一个函数库的一个被动的用户。通过揭露相关概念，SQLAlchemy信奉“漏洞抽象”的理念，鼓励开发者在应用和关系数据库之间剪裁一个定制的，完全自动化的交互层。SQLAlchemy的创新之处在于它允许了高度自动化但它没有减少对关系型数据库的控制。

##20.2. 内核/对象关系映射二分法
SQLAlchemy提供一个工具包方法的中心目标是作为一个丰富的接口，它暴露了数据库交互的每一层，将任务分成两个主要的部分叫做内核和对象关系映射。内核包括Python数据库API交互，为数据库所理解的文本SQL语句的翻译，以及数据库集合的管理。这些特点都作为公共接口所提出。对象关系映射，是建立在内核之上的一个特殊的库。SQLAlchemy提供的对象关系映射仅仅是许多可能的可以建立在内核上的对象抽象层中的一个，而许多开发者和开发组织直接在内核之上建立他们的应用程序。
 
 ![Figure 20.1][fig1]
 
图20.1：SQLAlchemy层的图解

内核/对象关系映射的划分已经成为SQLAlchemy的最典型的特点，这个特点有好的一面也有不好的一面。存在于SQLAlchemy中的明确的内核引导对象关系映射来关联映射数据库的类属性得到一个叫做“Table”的结构，而不是直接得到数据库表达的字符串列名；来用一个叫select的结构生成一个选择查询，而不是将查询语句和目标属性直接拼接成一个字符串进行查询；来通过一个叫做ResultProxy的包装结构获得结果行，这显然将select结构映射到了每一个结果行，而不是从一个数据库指针到一个用户定义的对象直接传递数据。
内核元素在一个非常简单的以对象关系映射为中心的应用程序中可能是不可见的。然而，由
于内核是细致地集成于对象关系映射中来允许在对象关系映射和内核结构之间的数据流动传递，一个更加复杂的以对象关系映射为中心的应用程序可以下调一个或两个隐藏内核的级别来用一个更复杂的特殊的通过细致调整的方法处理数据库，正如现状需求的一样。随着SQLAlchemy已经成熟，内核接口在定期使用时变得越来越不明确，因为对象关系映射继续提供更复杂和综合的模式。然而，内核的可用性也为SQLAlchemy早期获得成功作出了一定贡献，因为当对象关系映射正在开发的时候它允许早期的用户来完成现在不可能完成的事情。

对象关系映射/内核这种方法的负面影响是指令必须要经过更多步骤才能完成。Python的传统C实现对个人函数的调用有一个重大的不可避免的妨碍，这是Python运行慢的原发性主因。传统的改善这个的方法包括通过重新处理和内联来缩短调用链，用C代码来替换临界性能的区域。SQLAlchemy花费了许多年来使用这两种方法来提升性能。然而，越来越被人接受的PyPy Python解释器可能会保证抑制剩余的性能问题，这个解释器不需要将SQLAlchemy的内部构件的主要部分替换成C代码，因为PyPy解释器通过及时的内联和编译极大地减少了长调用链的影响。

##20.3. 改良数据库应用程序接口系统
SQLAlchemy本质上是一个通过数据库应用程序接口与数据库进行交互的一个系统。数据库应用程序接口本身不是一个实际存在的库，而只是一种规范。因此，数据库应用程序接口可以有针对性地为某个有特殊目标的数据库定制地实现，比如MySQL或PostgreSQL，或者为非数据库应用程序接口的数据库适配器，例如ODBC和JDBC而定制地实现。

数据库应用程序接口面临着两个挑战。第一个是为数据库应用程序接口的基本使用模式提供一个易于使用并且功能全面的外观模式。第二个是需要较好地处理数据库应用程序接口实现和潜在的数据库引擎的极端易变的特性。



####“方言”系统
数据库应用程序接口系统所描述的接口是极其简单的。它的核心组件包括数据库应用程序接口系统自己，连接对象，指针对象——一个数据库用语，代表一个特别的数据库语句的上下文和与它关联的结果。一个简单的这些对象之间的交互以及从一个数据库中查找数据的例子如下：
connection = dbapi.connect(user="user", pw="pw", host="host")
cursor = connection.cursor()
cursor.execute("select * from user_table where name=?", ("jack",))
print "Columns in result:", [desc[0] for desc in cursor.description]
for row in cursor.fetchall():
    print "Row:", row
cursor.close()
connection.close()
SQLAlchemy创建了一个和经典数据库应用程序接口系统会话差不多的外观模式。这个外观模式的入口是create_engine函数的调用，调用之后数据库连接和相关配置信息就装配了。一个Engine的实例就是产生的结果。这个对象就代表数据库应用程序接口系统的入口，但它自己并没有直接表现出来。

对于简单的语句执行，Engine提供了一个“模糊执行”的接口。捕获和关闭一个数据库应用程序接口系统连接和指针的行为都在这样的场景之后执行：
engine = create_engine("postgresql://user:pw&#64;host/dbname")
result = engine.execute("select * from table")
print result.fetchall()
当SQLAlchemy0.2出来的时候，Connection对象就加进来了，提供了明确维护数据库应用程序接口系统连接的作用域的能力：
conn = engine.connect()
result = conn.execute("select * from table")
print result.fetchall()
conn.close()
Engine或Connection对象的execute函数返回的结果叫做一个ResultProxy（结果代理）对象，它提供了一个与DBAPI指针相似的接口，但拥有更丰富的行为。Engine，Connection和ResultProxy分别是DBAPI组件的一个实例，特定DBAPI连接的一个实例和特定DBAPI指针的一个实例。

在这些场景的幕后，Engine类参照一个叫Dialect的对象。Dialect是一个抽象类，许多类实现了它，每一个实现都是为了某个特定DBAPI或数据库的结合。为一个Engine创建的一个Connection将会指向这个Dialect对象来作出所有的决策，这些决策依赖于具体的DBAPI目标和使用中的数据库将会有不同的行为。

Connection对象一创建，就会从叫做Pool的资源库获得并维护一个实际的DBAPI连接，这个资源库Pool也与Engine相联系。Pool资源库负责创建新的DBAPI连接，通常还负责在内存池里维护这些连接来应对频繁的复用。

在一个语句的执行期间，一个额外的叫做ExecutionContext的对象被Connection所创建。这个对象的生存周期从执行那个点开始一直贯穿ResultProxy的生存周期。这个对象也可以作为一个特殊的子类获得，用作一些DBAPI和数据库方面的结合所需。
图20.2阐释了所有这些对象以及他们之间的相互关系以及和DBAPI组件之间的关系：
 
![Figure 20.2][fig2]
 	
图20.2:Engine，Connection，ResultProxy API

####处理DBAPI的可变性
为了处理DBAPI行为的可变性，首先我们考虑这个难题的作用域。DBAPI规范，当前在版本2，被描述成一系列的API定义，这些定义允许一个在数据库行为上的较宽范围的可变性，并剩下了许多未定义的领域。最后，现实的DBAPI展示了在几个领域的很大的可变性，包括什么时候Python的unicode字符串是可接受的以及什么时候它们是不可接受的；“last inserted id”（最新插入的id）——就是说，一个自动生成的主键——可能怎样在一个insert语句执行后被获得；以及有范围的参数的值可能怎样被指定和解读。它们也可能有大量的特殊的适应类型的行为，包括对二进制，精度小数，日期，布尔类型，以及unicode数据的处理。

SQLAlchemy通过多层次的子类化来允许Dialect和ExecutionContext这两个对象的可变性，从而实现以上所说的处理。图20.3阐释了当以psycopg2的方式使用SQLAlchemy时Dialect和ExecutionContext两个类之间的关系。PGDialect类提供了一些行为，这些行为是针对PostgreSQL数据库的使用的，比如ARRAY数据类型和schema目录；
PGDialect_psycopg2这个类提供了一些针对psycopg2 DBAPI的行为，包括unicode数据的处理器和服务器端的指针。
 
![Figure 20.3][fig3]
 	
图20.3：简单的Dialect/ExecutionContext层

当处理一个支持多数据库的DBAPI时，一个上面所说的模式的变体就出现了。这样的例子包括pyodbc，它通过ODBC处理任意多的数据库后端；以及zxjdbc，一个只支持Jython的处理JDBC的驱动。随着一个sqlalchemy.connectors包中的混合类的使用，以上的关系是增广的，这个包提供了DBAPI的多后端的普遍的一些行为。图20.4显示了sqlalchemy.connectors.pyodbc为MySQL和Microsoft SQL Server在特定pyodbc的dialect间共享的一些普遍的函数。
 	
![Figure 20.4][fig4]
 	
图20.4：共享于dialect层的普遍的DBAPI行为

##20.4. 模式定义
随着数据库的连接和交互的建立，下一个任务是要规定后端不可知的SQL语句的创建和操纵。要达到这个目标，我们首先需要定义我们将怎样引用存在于一个数据库中的表和列——即模式。表和列代表了数据是如何组织的，并且大多数由表达式和命令组成的SQL语句引用了这些结构。

一个对象关系映射或数据访问层需要提供编程访问SQL语言的途径；在底层就是一个描述表和元组的可编程系统。这就是SQLAlchemy提供的第一个强大的对于核心和对象关系映射的分割，通过提供Table和Column两个类来描述数据库的结构且独立于用户模型的类定义。把模式定义从对象关系映射分割出来的基本原理是关系模式可以按照关系数据库被清晰地设计，包括限定平台的细节（如果需要的话），不需要被对象关系的概念搞得一团糟——这样保持了一个分离的关系。独立于对象关系映射组件也意味着模式描述系统只是对任何其他种类的对象关系系统有用，而这些系统可能会建立在核心之上。

Table和Column模型被归入叫做“元数据”的范围，元数据提供了容器对象叫做MetaData来代表一个Table对象的集合。这个结构主要从Martin FowLer的Patterns of Enterprise Application Architecture一书中关于“元数据映射”的描述中推断出来。图20.5显示了sqlalchemy.schema包中的一些重要元素。
 
![Figure 20.5][fig5]
 
图20.5：基本的sqlalchemy.schema对象

Table代表一个实际出现在一个目标schema的表的名称和其他属性。它的Column对象集合表示表中单独的列的名称和类型信息。一组完整的描述了约束，下标，以及序列的对象用于填充更多的细节，它们中的一些会影响引擎和SQL构造系统的一些行为。特别地，ForeignKeyConstraint这个类对确定两个表如何连接是极为重要的。

Schema包中的Table和Column相对于其他包来说是独一无二的，且它们是双继承的，
都从sqlalchemy.shema和sqlalchemy.sql.expression包中继承，不仅作为schema水平的结构来提供服务，而且作为SQL语句的核心语法来提供服务。这个关系显示在图20.6。
 
![Figure 20.6][fig6]
 
图20.6：Table和Column类的双继承

在图20.6中我们可以看到Table和Column从sql包中继承。作为“你可以从它里面查询”的一种特殊形式，称作FromClause，以及作为“你可以在一个SQL表达式中使用的东西”，称作ColumnElement。

##20.5. SQL表达式
在SQLalchemy的开发期间，生成SQL的方法是不清晰的。一个文本语言可能有一个可能的候选SQL语句；这是一个普遍的方法，这个方法处于著名的像Hibernate的HQL这样的对象关系工具的核心。然而对Python语言来说，有个更加有趣的选择：那就是使用Python的对象和表达式来生成表达树结构，甚至重定义Python的操作符以至赋予这些操作符SQL语句的行为。

虽然它可能不是第一个这样做的工具，但是包含在Bicking的SQLObject中的SQLBuilder库有着高度可信度，因为Sqlalchemy的语言表示中使用了Python对象和操作符机制这个妙计。用这个方法，Python对象表示一个SQL语句的词汇部分。这些Python对象拥有的方法，以及重载的操作符，生成了来源于这些对象的新的词汇结构。最常见的对象是Column对象——SQLObject在一个对象关系映射的类中通过.q属性用一个命名空间存取来表现这些；SQLalchemy把那个属性命名为.c。这个.c属性到今天依然在核心可选择的元素中被维护着，比如那些有代表性的表和查询语句。

####表达树
如果你正解析一个SQL语句，一个SQLalchemy的SQL表达结构非常符合你创建的那个类型——它是一个分析树，除开发者直接创建分析树之外，其他人都是从一个字符串得到它。这个分析树中的结点的核心类型叫做ClauseElement，图20.7显示了ClauseElement和一些重要的类之间的关系。
 
![Figure 20.7][fig7]
 
图20.7：基本的表达层

通过构造函数、方法和重写Python操作符的使用，为一个像这样的SQL语句
SELECT id FROM user WHERE name = ?
创建的结构可能会在Python中像这样被创建：
from sqlalchemy.sql import table, column, select
user = table('user', column('id'), column('name'))
stmt = select([user.c.id]).where(user.c.name=='ed')
上面的select结构的构造显示在图20.8中。注意字面值'ed' 的表示包含在_BindParam的构造中，因此导致它作为一个有范围限制的参数标记被提出，且在SQL语句字符串中用一个问号来表示。
 
![Figure 20.8][fig8]
 
图20.8：表达树的例子

从属性图我们可以看到，一个简单的下行的对节点的遍历就可以迅速创建一个解析过的SQL表述，我们将会在语句编译那一节看到更深入的细节。

Python操作符方法
在SQLalchemy中，一个像这样的表达式：
column('a') == 2
产生的结果要么True 要么False，但是替代了一个SQL表达式的构造。这样的根本实现是使用Python的特殊的操作符函数机制来重载操作符：例如像__eq__, __ne__, __le__,__lt__, __add__, __mul__之类的方法。面向列的表达式节点通过一个叫ColumnOperators的类提供了重载Python操作符的行为。使用操作符重载，表达式column('a') == 2就等同于：
from sqlalchemy.sql.expression import _BinaryExpression
from sqlalchemy.sql import column, bindparam
from sqlalchemy.operators import eq

_BinaryExpression(
    left=column('a'),
    right=bindparam('a', value=2, unique=True),
    operator=eq
)
eq构造实际上是一个发源于Python内置的operator中的一个函数。作为一个对象（也就是operator.eq）而不是一个字符串（也就是=）来代表操作符允许字符串表示在语句编译时被定义，当数据库方言已知的时候。

####编译
负责将文本SQL语句解析成SQL表达树的中心类是Compiled这个类。这个类有两个主要的子类，SQLCompiler和DDLCompiler类。SQLCompiler类翻译SQL的操作字段，这些字段有SELECT，INSERT，UPDATE和DELETE语句，共同地被分类为DQL（data query language）和DML（data manipulation language）。而DDLCompiler处理各种各样的CREATE和DROP语句，被分类为DDL（data definition language）。还有个额外的类层专注于字符串表示的类型，这个类层起始于TypeCompiler类。独特的数据库方言之后提供它们自己的所有三种编译器类型的子类来针对目标数据库定义SQL的语言方面。图20.9提供了一个关于PostgreSQL方言的这个类层的概观。
 
![Figure 20.9][fig9]
 
图20.9：编译器层，包括PostgreSQL特有的实现

Compiled的子类定义了一系列的访问函数，每个函数都被一个特殊的子类ClauseElement关联着。一个ClauseElement节点层被遍历并且一个语句通过递归连接每一个访问函数的输出字符串的方式被构造出来。由于这个过程，Compiled对象维护了匿名标识符名称、有限制范围的参数名和子查询的嵌套的一个状态，在其他事情中，所有的这些都是为了一个字符串SQL语句和有限制范围和默认值的参数的一个最终集合的产生。图20.10显示了访问函数作用于文本单元的过程。
 
![Figure 20.10][fig10]
 
图20.10：调用一个语句编译层

一个完全的Compiled结构包含整个SQL字符串和有限制范围的值的集合。这些被一个ExecutionContext对象强制保证为DBAPI的execute方法期盼的格式，这个格式包括像这样的注意事项：一个声明为unicode对象的处理，用于存储有限制范围的值的集合的类型，以及有限制范围的值如何比较它们自己的细节应该强制为适合DBAPI和目标数据库相应表示出来。

##20.6. 类映射和ORM
我们现在把注意力移到ORM上来。第一个目标是使用我们定义的元数据表去允许把用户定义的类映射到一个数据库表中元组的集合上去。第二个目标是允许用户定义的类间的关系的定义，这个定义是基于一个数据库中表之间的关系的。

####经典的 vs. 声明式的
我们用术语“经典映射”来指SQLalchemy的允许一个对象关系的数据映射到一个出现的用户类的系统。这中形式考虑了Table对象和用户定义的类来成为两个独立定义的实体，这两个实体通过函数mapper来连接在一起。
一旦mapper被应用到一个用户定义的类，那么这个类就会呈现出于表中的元组相一致的属性：
class User(object):
    pass

mapper(User, user_table)

now User has an ".id" attribute User.id

Mapper函数也可以给类添加其他的属性，包括与其他种类的对象相一致的属性，还包括任意的SQL表达式。添加任意属性到一个类中的机制在Python中被称为“monkeypatching”；然而，由于我们正在用一个数据驱动和非任意的方式来做这件事，这个操作的精髓最好用术语class instrumentation表达。

现代的以声明扩展为中心的SQLAlchemy的使用，是一个与许多其他对象关系工具使用的普遍的像动作记录一样地类声明系统相似的结构的系统。在这个系统中，最终用户用类定义明确地定义了内嵌的属性，每一个内嵌属性都表示在这个类上被映射的属性。Table对象，大部分情况下，没有被明确地被提及，它也不是mapper中的函数；只有这个类，Column对象，和其他ORM相关的属性被命名了：
class User(Base):
    __tablename__ = 'user'
    id = Column(Integer, primary_key=True)
上面可能出现类仪器（class instrumentation）通过我们的配置id = Column()被直接获得的情况，但是事实不是这样的。声明扩展使用了一个Python的元类，这是一种每当一个新类被第一次声明时就运行一系列操作的很方便的方式，来从被声明的类中生成一个新的Table对象，并将这个对象随着这个类传递到mapper函数中。Mapper函数之后就用一模一样的方式做它的工作，将它自己的属性添加到这个类中，这种情况下朝向id属性，并将以前存在的替换掉。到元类初始化完成的时候（即当执行流离开User描绘的块的时候），被id标记的Column对象就已经被移动到一个新的Table中了，并且User.id已经被一个针对这个映射的新的属性所替代了。

SQLAlchemy总打算要有个可速记的、声明的配置形式。然而，声明的创建为了有利于接下来的工作被延迟了，同时固化了经典映射的结构。一个叫做ActiveMapper的临时性扩展，在早期就出现了，之后成为了Elixir项目。它在一个高水平的声明系统中重定义了映射结构。声明的目标是通过建立一个几乎精确保存SQLAlchemy经典映射概念的系统来颠倒Elixir的大量抽象出来的方法的方向，这个声明只是认识到它们如何被用来减少冗长和增多对类水平扩展的适应，相比一个经典的映射来说。

无论使用的是经典的还是声明式的映射，一个被映射的类都会呈现新的允许它根据它的属性表达SQL结构的行为。SQLAlchemy最初跟着SQLObject的行为：使用一个特殊的属性作为SQL元组表达的来源，这个属性被SQLAlchemy称作 .c，像下面这个例子一样：
result = session.query(User).filter(User.c.username == 'ed').all()
然而在0.4版本，SQLAlchemy将这个功能移到被映射的属性自己身上了：
result = session.query(User).filter(User.username == 'ed').all()
这个在属性存取上的变化结果是一个很大的改善，因为它允许像元组的对象出现在这个类中来获得额外的针对类的能力，而不是直接出现在那些起源于底层的Table对象的类中。它也允许在不同类属性之间的集成使用，例如直接引用表中元组的属性，引用来源与那些元组的SQL表达式的属性，以及引用一个相关类的属性。最后，它提供了一个在映射的类之间的一个对称性，和一个映射的类的实例，在这个实例中同样的属性依赖于父属性的类型将呈现不同的行为。与类绑定的属性返回SQL表达式，而与实例绑定的属性返回实际的数据。

####一个映射的剖析
与我们的User类绑定的id属性是一类在Python中叫做描述符的对象，它有__get__，__set__和__del__方法，Python运行时为所有涉及这个属性的类和实例听从这个属性。SQLAlchemy的实现被称作一个InstrumentedAttribute，并且我们将用另一个例子阐释这个外观模式幕后的世界。以一个Table对象和一个用户定义的类开始，我们建立了一个只有一个被映射的元组的映射，以及一个relationship对象，它定义了一个对相关类的引用：
user_table = Table("user", metadata,
    Column('id', Integer, primary_key=True),
)

class User(object):
    pass

mapper(User, user_table, properties={
    'related':relationship(Address)
})
当一个映射完成了，这个与类相关的对象的结构的细节就显示在图20.11中。
 
![Figure 20.11][fig11]
 
图20.11：一个映射的剖析

这个图显示了一个SQLAlchemy映射解释为在用户自定义类和它被映射到的元数据表之间交互的两个隔离层。类仪器是朝左边画的，而SQL和数据库函数是朝右边画的。一般模式是：对象组合用来隔绝行为的角色，对象继承用来区分一个特别的角色的行为差异。

在类仪器的领域，ClassManager与被映射的类相连接，而它的InstrumentedAttribute对象集合与每一个类中的被映射的属性相连接。InstrumentedAttribute也是之前提到的面向公共的Python描述符，当在一个基于类的表示中使用的时候（例如User.id==5），它还产生SQL表达式。当处理一个User的实例时，InstrumentedAttribute将那个属性的行为委托给一个AttributeImpl对象，这个对象是针对被映射的数据类型定制的几个品种之一。

在映射这一方面，Mapper对象代表一个用户定义的类和一个可选择单元的连接，最典型的就是Table。Mapper维护了一个每个属性的对象集合叫做MapperProperty，这个集合处理SQL对特殊属性的表示。MapperProperty最普遍的变体是ColumnProperty，它代表一个映射的元组或SQL表达式，和RelationshipProperty，它代表一个与其他映射的连接。

MapperProperty将加载属性的行为——包括属性如何在一个SQL语句中呈现和它如何从一个结果行中被填充——委托给一个LoaderStrategy对象，这个对象有几个变体。不同的LoaderStrategies决定一个属性的加载行为是否被推迟，饥饿，或立即执行。在映射配置时会选择一个默认版本，有在查询时使用一个轮流策略的选项。RelationshipProperty也引用了一个DependencyProcessor类，这个类处理在刷新时映射之间的依赖性和属性同步应该如何进行。DependencyProcessor的选择基于相关的与关系连接的父亲和目标可选性的几何结构。

Mapper/RelationshipProperty结构形成了一个图，在这个图中，Mapper对象是节点，RelationshipProperty是有向边。一旦一个应用程序声明了一整套映射，一个推迟的叫做配置过程的“初始化”步骤就开始进行了。它主要被每个RelationshipProperty用来集结在它的父类和目标映射之间的细节，包括AttributeImpl以及DependencyProcessor的选择。这个图是一个关键数据结构，它的使用贯穿了整个ORM的操作。它参与操作，比如叫“cascade”的行为，定义操作如何通过对象路径传播，在查询操作中相关对象和集合在哪里被马上“饥饿”载入，以及在对象刷新方面，开始一系列持续步骤前，一个所有对象的依赖图在哪里被创建。

##20.7. 查询和装载行为
SQLAlchemy通过Query对象启动所有的装载对象行为。Query以之开始的基本状态包括实体，就是映射的类的列表和/或要查询的个体SQL表达式。它也有对Session类的引用，这个类代表与一个或多个数据库的连接，以及一个关于在这些连接上处理累计的数据缓冲。下面是一个基本的使用示例：
from sqlalchemy.orm import Session
session = Session(engine)
query = session.query(User)
我们创建了一个将会向User的实例屈服的Query对象，这个对象与一个新的我们创建的Session对象有关。Query提供了一个有生产力的建筑者模式，用的是和之前讨论的select结构同样的方式，在这种方式中每一次一个方法被调用，额外的标准和修改器就和一个声明结构联系起来。当一个迭代的操作在Query中被调用时，它就会建立一个SQL表达式结构来代表一个SELECT，将它发送给数据库，然后将结果集的行解释为面向ORM的结果，并与被要求的实体的初始集相一致。

Query使得很难区分操作的SQL解析和数据加载两个部分。前者指一个SELECT语句的构造，后者指将SQL结果行解释为ORM映射的结构。数据加载实际上不需要SQL解析步骤就可以进行，但是Query可能会被要求从一个用户手写的文本查询语句中解析结果。

SQL解析和数据加载都利用了对一系列重要的Mapper对象形成的图的自顶向下的遍历，把每个元组的或每个SQL表达式所承担的ColumnProperty看作一个叶节点，把每个通过“eager-load”包含在query中的RelationshipProperty看作一条指向另一个Mapper节点的有向边。最后遍历和在每个节点采取的行动就是每个连接每个MapperProperty的LoaderStrategy的工作，它把元组和连接加到在SQL编译阶段产生的SELECT语句中，并产生出在数据加载阶段处理结果行的Python函数。

这些Python函数在数据加载阶段产生，当它们被调用时，每个函数都收到一个数据库行，结果在内存中的一个映射的属性的声明上产生可能的变化。它们为一个特殊的属性富有条件地被产生出来，基于第一个在结果集中的行，以及基于加载的选项。如果属性的一个加载没有进行，那么就不会有相应的函数产生。

图20.12显示了在一个贪心连接的加载策略下几个LoaderStrategy对象的遍历，显示了它们与一个编译后的SQL语句的连接，这个连接在Query的compile_context方法中出现。它也显示了结果行处理函数的生成，这些函数接收结果行并填充个体对象的属性，这个过程出现在Query的instances方法中。
 
![Figure 20.12][fig12]
 
图20.12：包括贪心连接加载的加载策略的遍历

SQLAlchemy的早期填充结果的方法是使用一个传统的与每个策略连接的混合对象方法遍历，来接收每个行并根据这些来处理。首先在0.5版本中介绍的不可赎回的加载器系统，导致了性能方面戏剧性的增长，因为它的许多决策考虑了行处理能只预先进行一次，而不是为每个行都进行一次，以及大量的无效的函数调用应该被淘汰。

##20.8. 会话/身份映射
在SQLAlchemy中，Session对象显示了为ORM的实际使用而准备的公共接口——也就是，加载和维护数据。它为一个给定的数据库连接的查询和持续操作提供了起始点。

Session对象，除作为数据库连通性的入口之外，它还维护了一个活动的对所有映射实体的引用，这些存在于内存中的实体是与这个Session对象相关的。Session为恒等映射和工作单元模式实现的一个外观就是用这种方式实现的，恒等映射和工作单元模式都被Fowler鉴定过。恒等映射为一个特殊的Session维护了一个有着独一无二身份数据库的所有对象的映射，消除了二重身份带来的问题。工作单元在恒等映射上建立，提供了一个用尽可能有效的方式自动化所有的在数据库中变化的维护过程的系统。实际的持续性步骤叫做“flush”，在现代的SQLAlchemy中这个步骤通常是自动化的。

####发展历史
Session是作为一个对发出一个flush的单任务负责的主要隐蔽的系统开始的。Flush过程包括发出SQL语句给数据库，保持对象的状态变化与工作单元系统的一致性，从而同步数据库现在的状态和内存中的状态。Flush总是SQLAlchemy中最复杂的操作之一。

Flush操作的调用在很早的版本中在一个叫commit的方法后面开始，它是一个出现在一个含蓄的、本地线程的叫做objectstore的对象中的方法。当你使用SQLAlchemy0.1时，不需要调用Session.add方法，也不需要一个明确的Session概念。只需要创建mappers，创建新的对象，编辑出现的对象通过queries加载（在queries自己被直接从Mapper对象调用的地方），然后提交所有的改变，通过objectstore.commit方法。为一个操作集合准备的对象池是无条件地全局模块的，并且无条件本地线程的。

objectstore.commit方法是一个即时的操作，第一批用户使用它，但是这个模块的健壮性迅速地撞墙了。现代SQLAlchemy的新用户有时哀叹为Session对象定义一个工厂，可能一个注册的需求，以及为每个Session组织他们的对象的需求，但是这比早期的更为可取，早期整个系统都是完全不明确的。0.1版本使用模式的方便仍然保持在现代的SQLAlchemy中，现代SQLAlchemy以会话注册的正常配置为特点来使用本地范围的线程。

Session自己仅在0.2版本介绍，宽松地模仿出现在Hibernate中的Session对象。这个版本以集成事务处理的控制为特点，在这里Session对象可以通过begin方法被放置在一个事务中，并通过commit方法完成Session。objectstore.commit方法重命名为objectstore.flush，新的Session对象可以在任意时刻创建。Session自己从另一个叫UnitOfWork的对象中消除，这个UnitOfWork对象作为一个对执行实际的flush操作负责的私有对象被维护。

当flush过程作为一个被用户明确调用的方法开始的时候，0.4版本介绍了autoflush的概念，即一个flush在每个query之前就开始。Autoflush的优势是被一个query发出的SQL语句总是可以访问相关的存在于内存中的确切状态，因为所有的变化都发送出去了。早期的版本没有这个特点，因为最普遍的使用模式是flush声明也永久提交变化。但是当autoflush被引进时，伴随有另一个特点叫做事务型的Session，它提供了一个Session，这个Session将自动在一个在用户明确调用commit之前维护的事务中调用。随着这个特点的引进，flush方法不再提交它冲刷的数据，而可以在一个自动化的底层被安全的调用。Session现在可以提供一个逐步的在内存和SQL查询状态之间的同步，它通过必要时flush，直到明确的commit步骤才永久地存留做到这一点。实际上，这个行为准确地说和java版本的Hibernate是一样的。然而，SQLAlchemy包含这个使用风格，基于和Python版本的Storm ORM一样的行为，是在0.3版本引入的。

0.5版本带来了更多的事务处理集成，这时post-transaction expiration被引入了；在每个commit或rollback之后，通过在消除Session时默认定义所有的状态，来又一次移动到相应地方，当SQL子查询语句重复查询数据时，或者当过期的对象属性在新的事务的上下文需要访问时。起初，SQLAlchemy是围绕这个假想创建的：SELECT语句应该无条件地尽可能少地发射出。提交时到期的行为因为这个原因而延迟了；然而，它完全地解决了Session问题，这个Session包含过期数据和滞后的事务处理，没有简单的方法来加载新数据时而不重建已经加载的所有对象集合。在早期，看起来这个难题不能被合理地解决，因为当Session应该考虑现在将过期的状态时这个问题是不明显的，因此需要为下一次访问生产一个昂贵代价的新的SELECT语句对象集合。然而，一旦Session移动到一个总是在一个事务处理中的模型时，事务处理的结束点就会表面化，相对数据终结的自然点来说因为一个高度隔离的事务的性质是它直到它被提交或者回滚了才能看到新的数据。不同的数据库和配置，当然有不同的事务隔离程度，包括根本就没有事务处理的情况。这些使用模式完全可以被SQLAlchemy的期满模式所接受；开发者只需要知道一个低程度隔离的水平可能曝光非孤立的改变在一个会话中，如果多会话分享同样的数据行的话。这和直接使用两个数据库连接将发生的有着根本的不同。

####会话概述
图20.13显示了一个Session和它处理的私有结构。
 
![Figure 20.13][fig13]
 
图20.13：会话概述

面向公共的部分的上面是Session自己和用户对象的集合，它们中的每一个都是一个映射类的实例。这儿我们可以看见映射的对象保持了对一个叫做InstanceState 的SQLAlchemy结构的引用，这个结构为一个个体的实例追踪了ORM状态，包括待定的属性变化和属性的生存周期状态。InstanceState是之前某节讨论到的属性instrumentation的实例水平上的方面，那一节是“一个映射的解析”，在类水平上与ClassManager相关，并维护了映射的对象的字典状态（例如Python __dict__ 属性）为了与这个类联系起来的AttributeImpl对象。

####状态追踪
IdentityMap是一个到InstanceState对象数据库实体的映射，为了那些有数据库特性的对象，这个特性是持久稳固的。IdentityMap的默认实现是和InstanceState一起自我管理它的大小，通过移除用户映射的实例，一旦所有对它们的强引用被移除时——用这种方式它和Python的WeakValueDictionary是同样的工作模式。

Session保护所有标记为dirty或deleted的对象集合，以及待定的从垃圾集合来的标记为new的对象， 通过创建对那些待定改变的对象的强引用。所有的强引用都会在flush后丢弃。

InstanceState也执行鉴定维护“什么被改变了”的任务，为一个特殊对象的属性，使用一个一改变就动作的系统，这个系统在设定到来的值到对象现在的字典之前在一个叫committed_state的字典中存储了一个特殊属性的“之前的”值。在flush时，committed_state的内容和与这个对象联系起来的__dict__的内容就会比较以产生在每个对象上的净改变集合。

在集合的情况下，一个分离的collections包和InstrumentedAttribute或InstanceState系统协调来维护一个特殊映射的对象集合的净改变集合。普通的Python类例如set，list和dict在使用和用历史追踪的mutator方法增广之前都是子集。这个集合系统在0.4版本被重写以变得可扩充的和可用的为任何像集合的对象。

####事务处理的控制
Session，在它的默认使用状态，为所有完成的操作维护了一个开放的事务，当commit或rollback被调用的时候。SessionTransaction维护了一个0的集合或者更多Connection对象，每个都代表一个在一个特殊的数据库上的开放的事务。SessionTransaction是一个懒惰初始化的对象，它以无出现的数据库状态开始。作为一个被需要用来参加语句执行处理的后端，一个与那个数据库相关的Connection对象要被加到SessionTransaction的链接列表中。当一个一次单独的连接是普遍的，而多连接的方案也是支持的，当决定基于与Table，Mapper或者这个操作中的SQL结构自己联系的配置，为一个特殊的操作使用特殊的连接时。多连接也可以使用双相的行为调整事务，为那些提供这个行为的DBAPI。

##20.9. 工作单元
Session提供的flush方法将它的工作移交给一个隔离的模块叫做unitofwork。正如前面提到的，flush过程可能是SQLAlchemy中最复杂的功能。
工作单元的工作是将所有出现在一个特殊的Session里的待定状态移出到数据库中，腾空这个Session维护的new，dirty，deleted集合。一旦完成，Session的内存中状态和出现在现在的事务中的状态就匹配了。主要的挑战是决定正确的一系列的持续步骤，然后用正确的顺序执行它们。这个包括决定INSERT，UPDATE和DELETE语句的列表，包括那些被删除或修改的行需要连坐的结果；确保UPDATE语句仅包含那些实际编辑的列；建立同步操作，即将要把主键列的状态复制到引用的外键列的操作，在那时新生成的主键指针就可以获得了；确保INSERT操作按对象加入Session的顺序发生，并且尽可能有效率；以及确保UPDATE和DELETE语句以确定性顺序发生，来减少死锁的机会。

####历史
工作单元这个实现是从一个业务方式的以特定方式写的复杂系统开始的；它的开发可以和在没有地图的情况下从一个森林里找出一条路相比较。早期的bug和遗忘的行为用补丁修复了，0.5版本重构了几次代码改善了一些事情，直到0.6版本工作单元才具有时间稳定性，很好的理解性，并且被几百个测试覆盖——可以完全地从头重写。在许多周的考虑以一致数据结构的新方法驱动时后，重写它的进程就是使用这个几天产生的新的模型，因为这个想法可以很好被理解。新实现的行为可以被很认真地交叉检查这个事实也支持了出现的版本。这个过程展示了第一个迭代，然而可怕地，是如何仍然有价值的，只要它提供了一个工作模型。它更展示了一个子系统总的重写如何不仅仅经常适当，并且是一个很难开发的系统中的集成部分。

####拓扑排序
在工作单元背后的主要范例是装配行为的整个列表来形成一个数据结构，这个结构中每个节点代表一个单独的步骤；在设计模式用语中它叫做命令模式。这个结构中的一系列的“命令”用拓扑排序组成一个特殊的顺序。一个拓扑排序是将事物基于一个局部排序来排序的过程，即，只有确定的元素必须排在其他的元素前面。图20.14显示了拓扑排序的行为。
 
![Figure 20.14][fig14]

图20.14：拓扑排序

工作单元建立了一个局部排序基于那些必须排在其他命令前面的持续性命令。这些命令之后被拓扑排序，并按顺序调用。一个命令优先与另一个命令的决定主要从一个relationship推断而来，这个relationship是两个Mapper对象的桥梁——通常，一个Mapper被认为是依赖与另一个。相似的规则也对多对多的关联表适用，但这里我们仅关注一对多和多对一的情况。外键依赖需要解决为了预防违规的约束，且不依赖需要将约束标志为“延期的”。但顺序允许主键识别符同样重要，这个在许多平台都只是生成的，当一个INSERT实际发生的时候，来从一个刚刚执行的INSERT语句的结果粒子性增加到一个非独立的行的将要插入的参数列表。对于删除，同样的顺序相反地被使用——非独立的行在那些它们依赖的行之前删除，当这些行由于没有它们的外键的引用而不能再出现时。

工作单元以一个拓扑排序表现在两个不同层面的系统为特点，基于出现的非独立结构。第一个层面将持续性的步骤组织成桶基于映射间的非独立性，即，满桶的与一个特别的类相关的对象。第二个层面打碎0或更多这样的桶分为更小的一批，来处理环形引用或自引用表的情况。图20.15显示了“桶”生成来插入一个User对象的集合，然后一个Address对象的集合，一个中间步骤在这个集合中复制新的生成的User主键的值到每个Address对象的user_id外键元组中。
 
![Figure 20.15][fig15]

图20.15：通过映射组织对象

在每个映射排序的情况，若干User和Address对象可以被flush，而不对步骤的复杂度或多少非独立性必须被考虑造成影响。
排序的第二个层面基于直接的单映射范围内个体的对象之间的非独立性组织持续性步骤。这种情况发生的最简单的例子是一个包含对它自己引用的外键的表；表中一个特殊的行需要在表中的引用这一行的某一行之前插入。另一个例子是当一系列的表有一个循环引用的时候：表A引用表B，表B引用表C，表C引用表A。一些A的对象必须在其他A对象之前插入来允许B和C对象也被插入。引用自己的表是循环引用的一种特殊情况。

为了决定哪一个操作可以在它们的聚集的每个Mapper桶，和将要被分为一个大的每个对象命令集合的桶中最后进行，一个循环的缺陷算法被应用到非独立性的集合中，这些非独立性出现在映射之间，这个算法使用了一个循环缺陷算法的改良版，这个改良版在Guido Van Rossum's blog可以找到。那些被卷入循环中的桶之后被分成每个对象操作，并混合成每个映射桶的集合，通过新的非独立性规则的从每对象的桶添加回每映射的桶。图20.16显示了User对象的桶被分成个体的每对象的命令，来源于一个新的从User到它自己的叫做contact的relationship的添加。
 
![Figure 20.16][fig16]
 
图20.16：组织循环引用到个体的步骤

桶结构背后的基本原理是它允许尽可能多的普通语句的配料，既减少Python中需要的步骤数量，也使更有效的与DBAPI之间的交互成为可能，这样有时可以用一个单独的Python方法调用执行成千上万的语句。只有当一个循环引用在映射之间出现时，更多代价的每对象非独立模式才开始生效，甚至它只为那些需要它的对象图的部分发生。

##20.10. 总结
SQLAlchemy从一开始目标就非常高远，目标是成为最富有特点和最通用的数据库产品。它已经做了许久保持专注与关系型数据库，意识到以一个深度和易于理解的方式支持关系型数据库的有用性是一个主要的事业；甚至现在，这个事业的范围仍继续扩大。

基于组成元素的方法打算用来从函数的每个区域提取最可能的值，提供许多不同的单元，应用程序可以单独使用或组合使用这些单元。这个系统已经历经了创建、维护和交付的挑战。

发展历程是缓慢的，基于那个理论：对一个坚实功能的一个有系统的、基础深厚的创建最终会比无根据的快速交货的创建更有价值。SQLAlchemy建立一个一致的文档充分的用户故事花费了很长时间，但是通过这个过程，潜在的架构总是领先一步，导致某些情况下像“时间机器”一样，在用户需要某些特点之前，这些特点已经存在于SQLAlchemy中了。

Python语言是一个可靠的主机（如果有一点过分讲究的话，特别是性能领域）。这个语言的一致性和惊人地运行时打开模式使SQLAlchemy提供了一个比用其他语言写的相似产品更良好的体验。

Python获得前所未有的深度接受和被尽可能广泛的不同领域和工程采用是SQLAlchemy项目的希望所在，关系型数据库的使用保持生气勃勃和先进的同样也是SQLAlchemy的希望。SQLAlchemy的目标是演示关系型数据库，Python，和好的考虑的对象模型都是非常值得做的开发工具。

这个工作在Creative Commons Attribution 3.0 Unported许可协议下可获得，欲查看细节，请点击full description of the license。


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
