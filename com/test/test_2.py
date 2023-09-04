'''

'''
import asyncio
async def m1():
    print('This is coroutine one...')
    return 'm1'
async def m2(param):
    print('This is coroutine two...')
    return f'Method parameter : {param}'
async def main():
    print('This is the sys coroutine...')
    print('Waite coroutine one executes...')
    r1 = await m1()
    print('Wait coroutine two executes...')
    r2 = await m2(r1)
    return r1, r2
if __name__ == '__main__':
    loop = asyncio.get_event_loop()
    try:
        result = loop.run_until_complete(main())
        print(f'Result is : {result}')
    finally:
        print('Close the loop...')
        loop.close()