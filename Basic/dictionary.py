# coding=utf-8

dict = {}
dict['one'] = "This is one"
dict[2] = "This is two"

tinydict = {"name":"johnny","code":6734, "dept":"sales"}

print dict['one']          # 输出键为'one' 的值
print dict[2]              # 输出键为 2 的值
print tinydict             # 输出完整的字典
print tinydict.keys()      # 输出所有键
print tinydict.values()    # 输出所有值

"""
$ python Basic/dictionary.py
This is one
This is two
{'dept': 'sales', 'code': 6734, 'name': 'johnny'}
['dept', 'code', 'name']
['sales', 6734, 'johnny']

"""
