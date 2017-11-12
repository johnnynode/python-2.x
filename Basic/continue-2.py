# coding=utf-8

var = 10

while var > 0:
  var -= 1
  if var == 5 or var == 8:
    continue
  print '当前值 :', var
print "Good bye!"

"""
MacBook-Pro:python-2.x Johnny$ python Basic/continue-2.py
当前值 : 9
当前值 : 7
当前值 : 6
当前值 : 4
当前值 : 3
当前值 : 2
当前值 : 1
当前值 : 0
Good bye!
"""