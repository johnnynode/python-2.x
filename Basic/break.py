# coding=utf-8

for letter in 'Python':
    if letter == 'h':
        break
    print '当期字母 ：', letter

var = 10
while var > 0:
    print '当期变量值 ：', var
    var -= 1
    if var == 5:
        break

print "Good bye!"

"""
$ python Basic/break.py
当期字母 ： P
当期字母 ： y
当期字母 ： t
当期变量值 ： 10
当期变量值 ： 9
当期变量值 ： 8
当期变量值 ： 7
当期变量值 ： 6
Good bye!

"""
