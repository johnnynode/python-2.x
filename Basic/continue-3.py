# coding=utf-8

n = 0
while n < 10:
  n += 1
  if n % 2 == 0:
    continue
  print(n)

"""
MacBook-Pro:python-2.x Johnny$ python Basic/continue-3.py
1
3
5
7
9
"""