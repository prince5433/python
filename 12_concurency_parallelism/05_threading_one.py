import threading
import time

def boil_milk():
    print("boiling milk...")
    time.sleep(2)
    print("milk boiled")

def toast_bun():
    print("toasting bun...")
    time.sleep(3)# sleep basically kya karta hai ki thread ko kuch time ke liye pause kar deta hai, is case me 3 seconds ke liye toast_bun thread ko pause kar diya jayega
    print("done with bun toast")

start=time.time()# Start time to measure total execution time
# time,time basically gives us the current time in seconds since the epoch (January 1, 1970)
# Create threads for each task
t1 = threading.Thread(target=boil_milk)
t2 = threading.Thread(target=toast_bun)

# Start the threads
t1.start()
t2.start()

# Wait for both threads to finish
t1.join()
t2.join()
end=time.time()
print(f"Total time taken: {end-start:.2f} seconds")
#:. 2f basically kya karta hai ki end-start ke result ko 2 decimal places tak format kar dega, isse hume total time taken ka accurate measurement milega with 2 decimal points.