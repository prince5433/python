# Multiprocessing is best for CPU-bound tasks (heavy computations)
# Each process has its own memory space and runs in true parallel on different CPU cores
# Bypasses Python's GIL, allowing true parallel execution

from multiprocessing import Process
import time

# Function to brew chai - each process will run this independently
def brew_chai(name):
    print(f"Brewing chai for {name}")
    time.sleep(3)  # Simulates time-consuming brewing process
    print(f"Chai for {name} is ready!")

# This guard is REQUIRED for multiprocessing on Windows
# Prevents infinite process spawning when the module is imported
if __name__ == "__main__":
    # Create a list of 3 separate processes using list comprehension
    # Each process will run brew_chai() with a unique name argument
    chai_makers=[
        Process(target=brew_chai, args=(f"CHAI MAKER #{i+1}",))
        for i in range(3)
    ]

    # Start all processes - they will run in parallel on different CPU cores
    # All 3 chai makers will brew simultaneously
    for maker in chai_makers:
        maker.start()

    # Wait for all processes to complete before continuing
    # join() ensures the main program doesn't exit before processes finish
    for maker in chai_makers:
        maker.join()
    
    # This prints only after all processes have completed
    print("All chai brewed!")