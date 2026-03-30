import threading
import time

def brew_chai():
    print(f"{threading.current_thread().name} started brewing chai")
    count = 0
    for _ in range(10**7):  # Simulates a CPU-bound task (heavy computation)
        count += 1
    print(f"{threading.current_thread().name} finished brewing chai")

# Create multiple threads to brew chai
thread1 = threading.Thread(target=brew_chai, name="Barista1")
thread2 = threading.Thread(target=brew_chai, name="Barista2")
# Due to Python's GIL, these threads will not run in true parallel for CPU-bound tasks
start = time.time()
# Start both threads
thread1.start()
thread2.start()
# Wait for both threads to finish
thread1.join()
thread2.join()
end = time.time()
print(f"Total time taken: {end - start:.2f} seconds")