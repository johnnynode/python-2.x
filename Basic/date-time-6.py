# coding=utf-8

import datetime
i = datetime.datetime.now()
print ("当前的日期和时间是 %s" % i)
print ("ISO格式的日期和时间是 %s" % i.isoformat() )
print ("当前的年份是 %s" %i.year)
print ("当前的月份是 %s" %i.month)
print ("当前的日期是  %s" %i.day)
print ("dd/mm/yyyy 格式是  %s/%s/%s" % (i.day, i.month, i.year) )
print ("当前小时是 %s" %i.hour)
print ("当前分钟是 %s" %i.minute)
print ("当前秒是  %s" %i.second)

"""
$ python Basic/date-time-6.py
当前的日期和时间是 2017-11-16 09:59:13.570138
ISO格式的日期和时间是 2017-11-16T09:59:13.570138
当前的年份是 2017
当前的月份是 11
当前的日期是  16
dd/mm/yyyy 格式是  16/11/2017
当前小时是 9
当前分钟是 59
当前秒是  13
"""