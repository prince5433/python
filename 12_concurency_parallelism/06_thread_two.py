import threading
import time

def prepare_chai(type_, wait_time):
    print(type_, "chai brewing...")
    time.sleep(wait_time)
    print(type_, "chai ready")

# Create threads for each type of chai with different wait times
t1 = threading.Thread(target=prepare_chai, args=("masala", 2))
t2 = threading.Thread(target=prepare_chai, args=("ginger", 3))
# Start the threadst1.start()
t1.start()
t2.start()

t1.join()
t2.join()