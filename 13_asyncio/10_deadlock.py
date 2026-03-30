import threading
lockA = threading.Lock()
lockB = threading.Lock()

def task1():
    with lockA:
        print("Task 1: Acquired lock A")
        with lockB:
            print("Task 1: Acquired lock B")

def task2():
    with lockB:
        print("Task 2: Acquired lock B")
        with lockA:
            print("Task 2: Acquired lock A")

t1 = threading.Thread(target=task1)
t2 = threading.Thread(target=task2)
t1.start()
t2.start()
t1.join()
t2.join()
# In this example, task1 acquires lockA and then tries to acquire lockB, while task2 acquires lockB and then tries to acquire lockA. This creates a deadlock situation where both tasks are waiting for each other to release the locks, and neither can proceed. To avoid this, you can use a consistent locking order or use a timeout when acquiring locks.