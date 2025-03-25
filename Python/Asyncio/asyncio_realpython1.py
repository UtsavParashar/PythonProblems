# https://realpython.com/async-io-python/

import asyncio
import time

async def count():
    print('One')
    await asyncio.sleep(1)
    print('Two')

async def main():
    await asyncio.gather(count(), count(), count())

if __name__ == '__main__':
    s = time.perf_counter()
    asyncio.run(main())
    print(time.perf_counter() - s)