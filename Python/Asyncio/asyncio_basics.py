# credit - https://www.youtube.com/watch?v=Qb9s3UiMSTA

import asyncio

# Coroutine function - which while awaiting passes the control to the event loop
# it returns coroutine object which is passed to the run method
async def main():
    print('Start of the main coroutine')
    


## print(main()) #-> This will just generate the corountine object

# run funtion starts the event loop and takes coroutine object as the argument
asyncio.run(main())

