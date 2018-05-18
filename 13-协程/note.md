# 参考资料
- 资料
    - https://blog.csdn.net/andybegin/article/details/77884645
    - http://python.jobbole.com/86481/
    - http://python.jobbole.com/87310/
    - https://segmentfault.com/a/1190000009781688
    
# 迭代器
- 直接作用于for循环的叫可迭代对象,Iterable
- 不但可以作用于for循环,还可以被next调用的,叫Itrator


- 可以用isinstance判断
    
        from collections import Iterable
        l = [1,2,3,4]

        isinstance(l, Iterable)

        
        from collections import Iterator
        isinstance((x for x in range(10)), Iterator)
        
- iterable和Iterator的关系,可以通过iter函数运算

        isinstance(iter('abc'), Iterator)

# 生成器
- 一边循环一边计算的机制,generator
- 是一个算法/函数, 每次条用next的时候计算下一个值,最后跑出StopIteration
- 生成器创建:
    - 直接使用
    
            L = [x * x for x in range(10)]
            g = (x * x for x in range(10))
    - 函数中包含yield,则叫generator
    - next调用,遇到yield返回
    
    
             def odd():
                print('step 1')
                yield 1
                print('step 2')
                yield(3)
                print('step 3')
                yield(5)
        
             def fib(max):
                n, a, b = 0, 0, 1
                while n < max:
                    print(b)
                    a, b = b, a + b
                    n = n + 1
                return 'done'
                
             def fib(max):
                n, a, b = 0, 0, 1
                while n < max:
                    yield b
                    a, b = b, a + b
                    n = n + 1
                return 'done'

# 协程
- 历史
    - 3.4引入协程概念，用yield实现
    - 3.5 引入协程语法
    - 实现包asyncio,tornado, gevent
    
- 定义：“协程 是为非抢占式多任务产生子程序的计算机程序组件，
协程允许不同入口点在不同位置暂停或开始执行程序”。
从技术的角度来说，“协程就是你可以暂停执行的函数”。
如果你把它理解成“就像生成器一样”，那么你就想对了。
- 使用:   
    - yield关键字
    - send关键字
-  案例v1
    
- 协程的四个状态
    - inspect.getgeneratorstate(…) 函数确定，该函数会返回下述字符串中的一个：
    - GEN_CREATED：等待开始执行
    - GEN_RUNNING：解释器正在执行
    - GEN_SUSPENED：在yield表达式处暂停
    - GEN_CLOSED：执行结束
    - next预激（prime)
    - 完整执行过程v2
- 协程终止
    - 协程中未处理的异常会向上冒泡，传给 next 函数或 send 方法的调用方（即触发协程的对象）。
    - 终止协程的一种方式：发送某个哨符值，让协程退出。内置的 None 和Ellipsis 等常量经常用作哨符值==。
    
- 异常
    - 客户段代码可以在生成器对象上调用两个方法
    - generator.throw(Exctpiton):
    
            致使生成器在暂停的 yield 表达式处抛出指定的异常。如果生成器处理了抛出的异常，代码会向前执行到下一个 yield 表达式，而产出的值会成为调用 generator.throw方法得到的返回值。如果生成器没有处理抛出的异常，异常会向上冒泡，传到调用方的上下文中。
    - generator.close()
    
             致使生成器在暂停的 yield 表达式处抛出 GeneratorExit 异常。
             如果生成器没有处理这个异常，或者抛出了 StopIteration 异常（通常是指运行到结尾），
             调用方不会报错。如果收到 GeneratorExit 异常，生成器一定不能产出值，否则解释器会抛出RuntimeError 异常。生成器抛出的其他异常会向上冒泡，传给调用方。
    - v03               
- yield from
    - 为了得到返回值，协程必须正常终止；
    - 然后生成器对象会抛出StopIteration 异常，异常对象的 value 属性保存着返回的值。from
    - yield from 从内部捕获StopIteration异常
    - 并且把StopIteration异常value属性子作为yield from表达式的返回值
    - v04
    - v05
    - 委派生成器
        - 包含 yield from 表达式的生成器函数
        - 委派生成器在 yield from 表达式处暂停时，调用方可以直接把数据发给子生成器。
        - 子生成器再把产出的值发给调用方。
        - 子生成器返回之后，解释器会抛出 StopIteration 异常，并把返回值附加到异常对象上，
        此时委派生成器会恢复。
        - v06
        

# asyncio
- python3.4开始引入的标准库,内置了对移步io的支持
- asyncio本身是一个消息循环,
- 步骤
    - 创建消息循环
    - 把协程导入
    - 关闭
 - 案例08
 - 案例09-两个tasks
 - 案例v10-得到多个网站
 
# async and await
- 为了更好的表示异步io
- python3.5 开始引入
- 让coroutine代码更简洁
- 使用上,可以简单进行替换
    - 可以把 @asyncio.coroutine 替换成async
    - yield from 替换成await
- 案例v11, 把案例09直接替换
 
 
# aiohttp
- 介绍
    - asyncio实现单线程并发IO,在客户端用处不大
    - 在服务器端可以asyncio+coroutine配合,因为http是io操作
    - asyncio实现了TCP,UIDP,SSL等协议
    - aiohttp是给予asyncio实现的HTTP框架
    - pip install aiohttp
    - 案例07
    
    
# concurrent.futures
- python3新增的库
- 类似其他语言的线程池的概念
- 此模块利用multiprocessiong实现真正的平行计算
- 核心原理是：concurrent.futures会以子进程的形式，平行的运行多个python解释器，从而令python程序可以利用多核CPU来提升执行速度。
由于子进程与主解释器相分离，所以他们的全局解释器锁也是相互独立的。每个子进程都能够完整的使用一个CPU内核。
- concurrent.futures.Executor 
    - ThreadPoolExecutor
    - ProcessPoolExecutor
- submit(fn, args, kwargs)
    - fn:异步执行的函数
    - args,kwargs:参数
    
             # 官方死锁案例
            import time
            def wait_on_b():
                time.sleep(5)
                print(b.result())  #b不会完成，他一直在等待a的return结果
                return 5

            def wait_on_a():
                time.sleep(5)
                print(a.result())  #同理a也不会完成，他也是在等待b的结果
                return 6


            executor = ThreadPoolExecutor(max_workers=2)
            a = executor.submit(wait_on_b)
            b = executor.submit(wait_on_a)
            
    - 案例v14
      
- map(fn, \*iterables, timeout=None)
    - 跟map函数类似
    - 函数需要异步执行
    - timeout: 超时时间
    - 案例 v12
    - 案例v15
    - 起执行结果是list,数据需要从list中取出来
    
            with concurrent.futures.ThreadPoolExecutor(max_workers=3) as executor:
                print(list(executor.map(sleeper, x)))
           
- submit和map根据需要选一个即可
- 案例v13

- Future
    - 未来需要完成的任务
    - future 实例由Excutor.submit创建
    - 案例v17
