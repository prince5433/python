import asyncio
import time

from concurrent.futures import ThreadPoolExecutor

import concurrent
def check_stock(item):
    print(f"checking {item} in store...")
    time.sleep(3)#blocking operation
    return f"{item} stock: 42"

async def main():
    loop = asyncio.get_running_loop()
    with concurrent.futures.ThreadPoolExecutor() as pool:
        result = await loop.run_in_executor(
            #run in executor allows us to run blocking code in a separate thread or process without blocking the main event loop
        pool,
        check_stock,
        "masala chai"
)
        print(result)
        asyncio.run(main())