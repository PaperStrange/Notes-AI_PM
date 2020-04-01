## Instruction to use

This collection contains records in several **mysql-related** problems. Press `Ctrl + F`, use keyword to search similar problem.

## Table

ProblemDomain | Date | Description | Solution | Status | Remark
------------ | ------------- | ------------- | ------------- | ------------- | -------------
Apache Hive | 2020-03-30 | 将远程库的按日数据排列的数据，重新按周排列 | date_formate函数 | 失败
  |  |  |  | week函数 | 失败 | week函数和date_formate一年多少周的计算方式不同
  |  |  |  | dayofweek函数 | 成功 | 参考[Apache Hive 内置函数(Builtin Function)列表](https://www.iteblog.com/archives/2032.html)，[存档链接](https://web.archive.org/save/https://www.iteblog.com/archives/2032.html)
Apache Hive | 2020-04-01 | 有一个本地的Excel表格，想拿它和远程表做匹配，远程库只能通过内部平台访问，平台不知可否上传文件 | 通过平台复制远程表的指定列名下的数据到本地Excel，统一在本地进行匹配 | 成功

