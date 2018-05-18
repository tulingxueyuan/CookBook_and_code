def simple_coroutine():
    print('-> start')
    x = yield
    print('-> recived', x)

sc = simple_coroutine()
print(1111)
# 可以使用sc.send(None)，效果一样
next(sc)

print(2222)
sc.send('zhexiao')

