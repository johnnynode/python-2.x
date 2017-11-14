# coding=utf-8

tup = ('physics', 'chemistry', 1997, 2000);

print tup;
del tup;
print "After deleting tup : "
print tup;

"""
$ python Basic/tuple-4.py
('physics', 'chemistry', 1997, 2000)
After deleting tup :
Traceback (most recent call last):
  File "Basic/tuple-4.py", line 8, in <module>
    print tup;
NameError: name 'tup' is not defined
"""