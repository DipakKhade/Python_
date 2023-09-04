# AsyncIO in Python | Python Tutorial - Day #96
import asyncio

import time

async def fun1():
    await asyncio.sleep(1)
    print('This is a frist function')

async def fun2():
    await asyncio.sleep(4)
    print('This is a second function')

async def fun3():
    await asyncio.sleep(1)
    print('This is a third function')

async def main():
    L=await asyncio.gather(
        fun1(),
        fun2(),
        fun3()
    )

