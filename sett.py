import time
def greet():

        print("hello after 6 seconds")
time.sleep(3)
greet()

#threading.Timer (non blocking similar to setTime)
import threading
def greet():
        print("the quick brown fox jumps")
timer = threading.Timer(3.0,greet)
timer.start()
#This is the closest equivalent to JavaScript’s setTimeout()
# ======= asyncio (async/await style) ===
import asyncio
async def greet():
        await asyncio.sleep(5)
        print("hello world!")
asyncio.run(greet())
