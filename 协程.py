# 异步I/O
# asyncio
import asyncio
import time
@asyncio.coroutine
def hello():
    print("hello ")
    r = yield time.sleep(3)
    print('hello agin')
x = []
for i in range(3):
    x.append(hello())
loop = asyncio.get_event_loop()
loop.run_until_complete(asyncio.wait(x))
loop.close
'''
1 @asyncio.coroutine把一个generator标记为coroutine类型，然后，我们就把这个coroutine扔到EventLoop中执行。
2 hello()会首先打印出Hello world!，然后，yield from语法可以让我们方便地调用另一个generator。由于asyncio.sleep()也是一个coroutine，所以线程不会等待asyncio.sleep()，而是直接中断并执行下一个消息循环。当asyncio.sleep()返回时，线程就可以从yield from拿到返回值（此处是None），然后接着执行下一行语句。
3 把asyncio.sleep(1)看成是一个耗时1秒的IO操作，在此期间，主线程并未等待，而是去执行EventLoop中其他可以执行的coroutine了，因此可以实现并发执行。

'''

# async和await
@asyncio.coroutine
def hello():
    print('hello')
    r = yield from asyncio.sleep(1)
    print('hello again')

# async await新语法：

async def hello():
    print('hello')
    r = await asyncio.sleep(1)
    print('hello again')
