# coding=utf-8

dict = {'Name':'Zara', 'Age':7, 'Class':'First'}

del dict['Name']
dict.clear()
del dict

print "dict['Age']: ", dict['Age']
print "dict['School']: ", dict['School']

"""
$ python Basic/dictionary-4.py
dict['Age']:
Traceback (most recent call last):
  File "Basic/dictionary-4.py", line 9, in <module>
    print "dict['Age']: ", dict['Age']
TypeError: 'type' object has no attribute '__getitem__'
"""