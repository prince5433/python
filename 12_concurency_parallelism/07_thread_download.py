# Import threading module to enable concurrent execution
import threading
import time
import requests

# Function that will be executed by each thread
def download(url):
    print(f"starting download from {url}.")
    # Make HTTP GET request to download content from URL
    response = requests.get(url)
    print(f"Finished downloading from {url}, size: {len(response.content)} bytes")
 


# List of URLs to download images from
urls = [
  "https://httpbin.org/image/jpeg",
  "https://httpbin.org/image/png", 
"https://httpbin.org/image/svg"
]

# Record start time to measure performance
start=time.time()

# List to keep track of all thread objects
threads = 

# Create and start a separate thread for each URL
for url in urls:
    # Create a new thread that will run the download function with the given URL
    # target = function to run, args = arguments to pass to the function
    t = threading.Thread(target=download, args=(url,))
    
    # Start the thread (begins executing download function in parallel)
    t.start()
    
    # Add thread to list so we can wait for it later
    threads.append(t)

# Wait for all threads to complete before proceeding
# join() blocks until the thread finishes execution
for t in threads:
    t.join()

# Record end time and calculate total duration
end=time.time()
print(f"Total time: {end-start:.2f} seconds")