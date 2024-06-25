import asyncio
def callback(p):
    print(f'Callback function invoked. Parameter is {p}')
async def main(loop):
    print('Register the callback...')
    loop.call_later(0.2, callback, 1)
    loop.call_later(0.1, callback, 2)
    loop.call_soon(callback, 3)
    await asyncio.sleep(0.4)
if __name__ == '__main__':
    loop = asyncio.get_event_loop()
    try:
        loop.run_until_complete(main(loop))
    finally:
        print('Close the loop...')
        loop.close()