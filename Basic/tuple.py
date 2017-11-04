# coding=utf-8

tuple = ("tuple", 786, 2.23, "johnny", 70.2)
tinytuple = (123, "johnny")

print tuple               # 输出完整元组
print tuple[0]            # 输出元组的第一个元素
print tuple[1:3]          # 输出第二个至第三个的元素
print tuple[2:]           # 输出从第三个开始至列表末尾的所有元素
print tinytuple * 2       # 输出元组两次
print tuple + tinytuple   # 打印组合的元组

"""
$ python Basic/tuple.py
('tuple', 786, 2.23, 'johnny', 70.2)
tuple
(786, 2.23)
(2.23, 'johnny', 70.2)
(123, 'johnny', 123, 'johnny')
('tuple', 786, 2.23, 'johnny', 70.2, 123, 'johnny')
"""
