## Instruction to use

This collection contains records in several **python-related** problems. Press `Ctrl + F`, use keyword to search similar problem.

## Table

ProblemDomain | Date | Description | Solution | Status | Remark
------------ | ------------- | ------------- | ------------- | ------------- | -------------
Pandas: can not write into dataframe | 2020-07-19 | 向一个pandas dataframe写入数据 | df.loc[cond1, cond2] = value | 成功 | 假设：dataframe中有数据
  |  |  |  | df.iloc[cond1][cond2] = value | 失败 | iloc只能用于索引
  |  |  |  | df = df.append(pandas.DataFrame({col1: value1, col2: value2}), ignore_index=True) | 成功 | 假设：dataframe没有数据的情况
Pandas: can not encode | pandas.read_csv("test.csv", encoding="GB18030") | 失败 | 可能只适用于全部都是一种文字形式的情况
  |  |  |  | import imp; import sysy; imp.reload(sys) | 失败 | python3.x不需要在代码中指定
  |  |  |  | 记事本/notepad打开->另存为->UTF-8格式->手动调整部分格式的缺失 | 成功 | 不够高效