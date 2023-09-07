'''
协程调用普通函数（异步函数调用同步函数） - call_soon
'''
import asyncio
import functools
def callback(args, *, kwargs='default'):
    print(f'普通函数作为回调函数，参数：{args},{kwargs}')
# callback(1, kwargs='aaa')
async def main(loop):
    print('注册callback')
    loop.call_soon(callback, 1)
    wrapped = functools.partial(callback, kwargs='not default')
    loop.call_soon(wrapped, 2)
    await asyncio.sleep(0.2)
if __name__ == '__main__':
    loop = asyncio.get_event_loop()
    try:
        loop.run_until_complete(main(loop))
    finally:
        loop.close()