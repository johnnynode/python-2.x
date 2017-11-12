# coding=utf-8

for letter in 'Python':
  if letter == 'h':
    continue
  print '当前字母 :', letter

var = 10
while var > 0:
  var -= 1
  if var == 5:
    continue
  print '当前变量值 :', var
print "Good bye!"

"""
MacBook-Pro:python-2.x Johnny$ python Basic/continue-1.py
当前字母 : P
当前字母 : y
当前字母 : t
当前字母 : o
当前字母 : n
当前变量值 : 9
当前变量值 : 8
当前变量值 : 7
当前变量值 : 6
当前变量值 : 4
当前变量值 : 3
当前变量值 : 2
当前变量值 : 1
当前变量值 : 0
Good bye!
"""