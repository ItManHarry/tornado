'''
协程调用同步函数 - call_at
'''
import asyncio
def callback(n, loop):
    print(f'N is {n}, run time {loop.time()}')
async def main(loop):
    now = loop.time()
    print('当前内部事件：', now)
    print('循环事件：', now)
    print('注册Callback')
    loop.call_at(now+1, callback, 1, loop)
    loop.call_at(now+2, callback, 2, loop)
    loop.call_soon(callback, 3, loop)
    await asyncio.sleep(3)
if __name__ == '__main__':
    loop = asyncio.get_event_loop()
    try:
        print('进入事件循环')
        loop.run_until_complete(main(loop))
    finally:
        print('关闭循环')
        loop.close()