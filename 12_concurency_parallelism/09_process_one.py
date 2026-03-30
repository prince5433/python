import threading
import time

# Simulates a CPU-bound task (heavy computation)
def cpu_heavy():
    print("crunching some numbers")
    total = 0
    for i in range(10**7):
        total += i
    print(f"done crunching, total: {total}")

start=time.time()
# Create a thread to run the CPU-heavy function
threads = [threading.Thread(target=cpu_heavy) for _ in range(2)]
for t in threads:
    t.start()
for t in threads:
    t.join()
end=time.time()
print(f"Total time taken: {end - start:.2f} seconds")
