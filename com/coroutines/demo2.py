import asyncio
async def main():
    print('The main coroutine...')
    print('Coroutine 1 run...')
    r1 = await result1()
    print('Coroutine 2 run...')
    r2 = await result2(r1)
    return r1, r2

async def result1():
    print('This result1 coroutine function')
    return 'result coroutine'
async def result2(arg):
    print('This result2 coroutine function')
    return f'result2 received an argument {arg}'
if __name__ == '__main__':
    loop = asyncio.get_event_loop()
    try:
        r1, r2 = loop.run_until_complete(main())
        print(f'Result 1 is : \'{r1}\', result 2 is : \'{r2}\'')
    finally:
        print('Close the event loop...')
        loop.close()