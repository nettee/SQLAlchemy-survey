# SQLAlchemy体系结构分析

此项目为SQLAlchemy源代码的分析，是《软件体系结构》的课程作业的一部分。课程作业的全部内容详见[wiki页](https://github.com/nettee/SQLAlchemy-survey/wiki)。

### 目录结构

/sqlalchemy-1.0 下是SQLAlchemy项目的完整源代码，于2016年3月29日克隆自[zzzeek/sqlalchemy][1]的master分支。

[1]: https://github.com/zzzeek/sqlalchemy

### 配套环境安装

##### 1. 安装SQLAlchemy

```shell
easy_install SQLAlchemy
```

##### 2. 安装一个DBAPI

推荐安装[SQLite][SQLite]，一个轻量级数据库，适合测试。

[SQLite]: http://www.sqlite.org/download.html

安装SQLite之后还要安装pysqlite，这是SQLite为Python提供的API，也就是DBAPI。

```shell
sudo apt-get install libsqlite3-dev
sudo easy_install pysqlite
```

