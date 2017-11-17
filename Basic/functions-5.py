# coding=utf-8

def printme(str):
  "打印任何传入的字符串"
  print str;
  return;

# 调用printme函数
printme()

"""
$ python Basic/functions-5.py
Traceback (most recent call last):
  File "Basic/functions-5.py", line 9, in <module>
    printme()
TypeError: printme() takes exactly 1 argument (0 given)
"""