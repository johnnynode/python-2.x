# coding=utf-8

import time

localtime = time.localtime(time.time())
print "本地时间为：", localtime

"""
$ python Basic/data-time-2.py
本地时间为： time.struct_time(tm_year=2017, tm_mon=11, tm_mday=15, tm_hour=9, tm_min=19, tm_sec=59, tm_wday=2, tm_
yday=319, tm_isdst=0)
"""