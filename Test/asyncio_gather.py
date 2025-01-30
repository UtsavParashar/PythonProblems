import asyncio

async def f1():
    print('Func1 started')
    await asyncio.sleep(2)
    print('Func1 completed')

async def f2():
    print('Func2 started')
    await asyncio.sleep(3)
    print('Func2 completed')
    

async def f3():
    print('Func3 started')
    await asyncio.sleep(1)
    print('Func3 completed')
    

async def main():
    await asyncio.gather(f1(), f2(), f3())
    print('Main Ended')

asyncio.run(main())