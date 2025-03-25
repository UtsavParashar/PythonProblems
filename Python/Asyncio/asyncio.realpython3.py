# https://realpython.com/async-io-python/#the-asyncio-package-and-asyncawait

import asyncio
import time

async def part1(n):
    print('Running part1 - 1')
    await asyncio.sleep(n)
    print('Running part1 - 2')

async def part2(n):
    print('Running part2 - 1')
    await asyncio.sleep(n)
    print(f'Running part2 - 2')

async def chain(n):
    p1 = await part1(n)
    p2 = await part2(n)

async def main(n):
    await asyncio.gather(*(chain(m) for m in range(1, n)))

if __name__ == '__main__':
    asyncio.run(main(3))