import threading
import asyncio

@asyncio.coroutine
def hello():
    print('Hello world! (%s)' % threading.currentThread())
    print('Start..... (%s)' % threading.currentThread())
    yield from asyncio.sleep(10)
    print('Done..... (%s)' % threading.currentThread())
    print('Hello again! (%s)' % threading.currentThread())

loop = asyncio.get_event_loop()
tasks = [hello(), hello()]
loop.run_until_complete(asyncio.wait(tasks))
loop.close()