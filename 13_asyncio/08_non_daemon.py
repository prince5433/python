#non daemon thread basically means that the thread will keep running even after the main program has finished executing. In contrast, a daemon thread will automatically exit when the main program exits, even if the thread is still running.

import threading
import time

def monitor_temp():
    while True:
        print("monitoring tea temperature...")
        time.sleep(2)

t = threading.Thread(target=monitor_temp, daemon=False)
t.start()
print("main program done")

#non daemon thread will keep running even after the main program has finished executing.