'''
python中正则模块是re
使用大致步骤：
1. compile函数讲正则表达式的字符串便以为一个Pattern对象
2. 通过Pattern对象的一些列方法对文本进行匹配，匹配结果是一个Match对象
3. 用Match对象的方法，对结果进行操纵

'''


import re

# \d表示以数字
# 后面+号表示这个数字可以出现一次或者多次
s = r"\d+" # r表示后面是原生字符串，后面不需要转义


# 返回Pattern对象
pattern = re.compile(s)

# 返回一个Match对象
# 默认找到一个匹配就返回
m = pattern.match("one12two2three3")

print(type(m))
# 默认匹配从头部开始，所以此次结果为None
print(m)

# 返回一个Match对象
# 后面为位置参数含义是从哪个位置开始查找，找到哪个位置结束
m = pattern.match("one12two2three3", 3, 10)

print(type(m))
# 默认匹配从头部开始，所以此次结果为None
print(m)


print(m.group())

print(m.start(0))
print(m.end(0))
print(m.span(0))