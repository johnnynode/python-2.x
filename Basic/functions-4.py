# coding=utf-8

def changeme(mylist):
  "修改传入的列表"
  mylist.append([1,2,3,4])
  print "函数内取值：", mylist
  return

# 调用changeme函数
mylist = [10,20,30];
changeme(mylist);
print "函数外取值：", mylist

"""
$ python Basic/functions-4.py
函数内取值： [10, 20, 30, [1, 2, 3, 4]]
函数外取值： [10, 20, 30, [1, 2, 3, 4]]
"""