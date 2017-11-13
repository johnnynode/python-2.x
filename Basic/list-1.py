# coding=utf-8

list = ["list", 789, 2.23, "johnny", 70.2]
tinylist = [123, "johnny"]

print list               # 输出完整列表
print list[0]            # 输出列表的第一个元素
print list[1:3]          # 输出第二个至第三个元素
print list[2:]           # 输出从第三个开始至列表末尾的所有元素
print tinylist * 2       # 输出列表两次
print list + tinylist    # 打印组合的列表

"""
$ python Basic/list.py
['list', 789, 2.23, 'johnny', 70.2]
list
[789, 2.23]
[2.23, 'johnny', 70.2]
[123, 'johnny', 123, 'johnny']
['list', 789, 2.23, 'johnny', 70.2, 123, 'johnny']

"""
