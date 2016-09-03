# SQLAlchemy体系结构调研

这项调研是为了完成《软件体系结构》的课程作业。课程作业要求每个小组（1~2名同学）调研一个开源软件，翻译_Architecture of Open Source Applications_中的一个章节，并根据翻译写一篇关于这个软件的调研笔记。我们的调研内容是SQLAlchemy。所有人的作业提交在[这里](http://aosabook.cc/)。

主要成果：

+ _Architecture of Open Source Applications_中SQLAlchemy章节的翻译：[A](https://github.com/nettee/SQLAlchemy-survey/blob/master/note/Translation-A.md)、[B](https://github.com/nettee/SQLAlchemy-survey/blob/master/note/Translation-B.md)
+ [SQLAlchemy体系结构笔记](https://github.com/nettee/SQLAlchemy-survey/blob/master/note/Note.md)

## 目录结构

```
.
├── example 学习SQLAlchemy的示例代码
├── note 翻译和笔记
├── picture 笔记中使用到的图片
├── reference 参考资料
└── sqlalchemy-1.0 SQLAlchemy项目的完整源代码*
```

\* 于2016年3月29日克隆自[zzzeek/sqlalchemy][1]的master分支

[1]: https://github.com/zzzeek/sqlalchemy

## 试用SQLAlchemy

### 1. 安装SQLAlchemy

```shell
easy_install SQLAlchemy
```

### 2. 安装一个DBAPI

推荐安装[SQLite][SQLite]，一个轻量级数据库，适合测试。

[SQLite]: http://www.sqlite.org/download.html

安装SQLite之后还要安装pysqlite，这是SQLite为Python提供的API，也就是DBAPI。

```shell
sudo apt-get install python-dev libsqlite3-dev
sudo easy_install pysqlite
```

