from multiprocessing import Process
import time
# Simulates a CPU-bound task (heavy computation)
def cpu_heavy():
    print("crunching some numbers")
    total = 0
    for i in range(10**7):
        total += i
    print(f"done crunching, total: {total}")

if __name__ == "__main__":
    start=time.time()
    # Create a process to run the CPU-heavy function
    processes = [Process(target=cpu_heavy) for _ in range(2)]
    for p in processes:
        p.start()
    for p in processes:
        p.join()
    end=time.time()
    print(f"Total time taken: {end - start:.2f} seconds")