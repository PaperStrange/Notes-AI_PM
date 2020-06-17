## Instruction to use

This collection contains records in several **mysql-related** problems. Press `Ctrl + F`, use keyword to search similar problem.

## Table

ProblemDomain | Date | Description | Solution | Status | Remark
------------ | ------------- | ------------- | ------------- | ------------- | -------------
Apache Hive | 2020-03-30 | 将远程库的按日数据排列的数据，重新按周排列 | date_formate函数 | 失败
  |  |  |  | week函数 | 失败 | week函数和date_formate一年多少周的计算方式不同
  |  |  |  | dayofweek函数 | 成功 | 参考[Apache Hive 内置函数(Builtin Function)列表](https://www.iteblog.com/archives/2032.html)，[存档链接](https://web.archive.org/save/https://www.iteblog.com/archives/2032.html)
Apache Hive | 2020-04-01 | 有一个本地的Excel表格，想拿它和远程表做匹配，远程库只能通过内部平台访问，平台不知可否上传文件 | 通过平台复制远程表的指定列名下的数据到本地Excel，统一在本地进行匹配 | 成功
MYSQL | 2020-06-11 | Unknown column ‘xxx’ in ‘where clause’ | 对WHERE后面的字段加单引号 | 成功 | 任何字段，如果定义的类型是int型的可以不用加引号，但是如果是字符串类型的，必须加单引号
MYSQL | 2020-06-11 | SQL syntax near ')' | 在没有嵌套的情况下去除多余的() | 成功 | 举例：SELECT * FROM \nSELECT A FROM table1和SELECT * FROM (\nSELECT A FROM table1, \nSELECT B FROM table2)，但如果需要传递table则必须加()
MYSQL | 2020-06-12 | SQL syntax near AS XXX | 修改命名 | 成功 | 固有名词(index)和已经赋值的变量名不能再作为alias
MYSQL | 2020-06-12 | 查询子字符串是否在数据中查询失败 | 将IN和FIND_IN_SET函数换为LOCATE | 成功 | 原因未知
MYSQL | | | | |