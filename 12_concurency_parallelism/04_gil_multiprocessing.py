from multiprocessing import Process
import time

def crunch_numbers():
    print(f"starteed the count process")
    count = 0
    for _i in range(10**8):
        count += 1
    print(f"finished the count process")

if __name__ == "__main__":
    start=time.time()

    p1=Process(target=crunch_numbers)
    p2=Process(target=crunch_numbers)

    p1.start()
    p2.start()

    p1.join()
    p2.join()

    end=time.time()
    print(f"Total time taken: {end-start:.2f} seconds")
