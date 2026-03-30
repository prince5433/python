import asyncio
import threading
import time

def background_worker():
    while True:
        time.sleep(1)
        print("logging system health")

async def fetch_orders():
    await asyncio.sleep(3)
    print("order fetched")

t = threading.Thread(target=background_worker, daemon=True)
# daemon true basically means that this thread will not prevent the program from exiting
t.start()

asyncio.run(fetch_orders())