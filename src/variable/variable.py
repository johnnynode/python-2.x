#coding=utf-8

# 测试 变量赋值
def test1():
    counter = 100  # 赋值整型变量
    miles = 1000.0  # 浮点型
    name = "John"  # 字符串

    print counter
    print miles
    print name
    print 

# 测试 变量赋值
def test2():
    str = 'Hello World!'
 
    print str           # 输出完整字符串
    print str[0]        # 输出字符串中的第一个字符
    print str[2:5]      # 输出字符串中第三个至第五个之间的字符串
    print str[2:]       # 输出从第三个字符开始的字符串
    print str * 2       # 输出字符串两次
    print str + "TEST"  # 输出连接的字符串


# 执行函数
test1()
test2()