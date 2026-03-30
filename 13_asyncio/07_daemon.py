import threading
import time

def monitor_temp():
    while True:
        print("monitoring tea temperature...")
        time.sleep(2)

t = threading.Thread(target=monitor_temp, daemon=True)
t.start()
print("main program done")

#daemon thread will automatically exit when the main program exits, even if the thread is still running.