# coding=utf-8

dict = {['Name']:'Zara', 'Age':7}
print "dict['Name']: ", dict['Name']

"""
$ python Basic/dictionary-6.py
Traceback (most recent call last):
  File "Basic/dictionary-6.py", line 3, in <module>
    dict = {['Name']:'Zara', 'Age':7}
TypeError: unhashable type: 'list'
"""