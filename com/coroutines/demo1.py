import asyncio
async def foo():
    print('This is a coroutine')
    return 'Return Result'
if __name__ == '__main__':
    loop = asyncio.get_event_loop()
    try:
        print('Start run the coroutine now...')
        coro = foo()
        result = loop.run_until_complete(coro)
        print(f'run util complete can get the coroutine\'s '
              f'\'{result}\', default is None')
    finally:
        print('Close the event loop.')
        loop.close()