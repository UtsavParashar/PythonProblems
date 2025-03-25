# https://realpython.com/async-io-python/#the-asyncio-package-and-asyncawait

import asyncio

async def z(x):
    return x

async def f(x):
    y = await z(x)
    return y

async def g(x):
    yield x

if __name__ == '__main__':
    print(asyncio.run(g(10)))