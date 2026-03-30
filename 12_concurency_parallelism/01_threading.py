# Threading is best for I/O-bound tasks (waiting for input/output operations)
# Multiple threads share the same memory space and run concurrently
# Due to Python's GIL (Global Interpreter Lock), threads don't run in true parallel for CPU-bound tasks

import threading
import time

# Simulates taking customer orders (I/O-bound task)
def take_orders():
    for i in range(1,4):
        print(f"Taking order {i}")
        time.sleep(2)  # Simulates waiting time while taking order

# Simulates brewing chai (I/O-bound task)
def brew_chai():
    for i in range(1,4):
        print(f"Brewing chai {i}")
        time.sleep(3)  # Simulates waiting time while chai is brewing

# Create thread objects
# target parameter specifies the function to run in the thread
order_thread = threading.Thread(target=take_orders)
chai_thread = threading.Thread(target=brew_chai)

# Start both threads - they will now run concurrently
# This means both take_orders() and brew_chai() execute at the same time
order_thread.start()
chai_thread.start()

# join() makes the main program wait for threads to complete
# Without join(), the main program would finish before threads complete
order_thread.join()
chai_thread.join()

# This prints only after both threads have finished
print("All orders taken and chai brewed!")