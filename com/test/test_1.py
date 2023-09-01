async def a_double(x):
    return x * 2
import asyncio

if __name__ == '__main__':
    loop = asyncio.get_event_loop()
    try:
        print('Start coroutine...')
        d = a_double(20)
        print('Loop now ...')
        r = loop.run_until_complete(d)
        print('Result is : {}'.format(r))
    finally:
        print('Close the loop ...')
        loop.close()
