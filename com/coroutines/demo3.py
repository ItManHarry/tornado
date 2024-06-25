import functools
import asyncio
def call_back(arg, *, kwarg='default'):
    print(f'The simple function, arguments are {arg}, keyword argument is {kwarg}')
async def main(loop):
    print('Register the callback function')
    loop.call_soon(call_back, 1)
    wrapped = functools.partial(call_back, kwarg='Not default')
    loop.call_soon(wrapped, 2)
    await asyncio.sleep(0.2)
if __name__ == '__main__':
    loop = asyncio.get_event_loop()
    try:
        loop.run_until_complete(main(loop))
    finally:
        print('Close the loop')
        loop.close()