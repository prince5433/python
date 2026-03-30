from multiprocessing import Process, Value

def increment(counter):
    for _ in range(100000):
        with counter.get_lock():  # Ensure that only one process can modify the counter at a time
            counter.value += 1



if __name__ == "__main__":
    counter = Value('i', 0)  # 'i' for integer, initial value 0
    processes = [Process(target=increment, args=(counter,)) for _ in range(5)]
    
    for p in processes:
        p.start()
    for p in processes:
        p.join()
    
    print(f"Final counter value: {counter.value}")