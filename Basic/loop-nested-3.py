# coding=utf-8

i = 1
# j=1
while i <= 9:
    if i <= 5:
        print("*" * i)

    elif i <= 9:
        j = i - 2 * (i - 5)
        print("*" * j)
    i += 1
else:
    print("")

"""
$ python Basic/loop-nested-3.py
*
**
***
****
*****
****
***
**
*

"""
