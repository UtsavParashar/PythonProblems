
import asyncio
 
async def fn1():
    asyncio.create_task(fn2())
    print('one')
    # await fn2()
    # await asyncio.sleep(1)
    print('four')
    await asyncio.sleep(1)
    print('five')

async def fn2():
    print('two')
    await asyncio.sleep(1)
    print('three')
 
asyncio.run(fn1())