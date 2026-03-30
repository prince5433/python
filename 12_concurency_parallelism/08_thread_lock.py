import threading

counter=0
lock=threading.Lock()# lock basically ek aisa mechanism hai jo multiple threads ke beech me shared resources ko access karne ke liye synchronization provide karta hai, is case me counter variable ek shared resource hai jise multiple threads access kar rahe hain, lock ensure karta hai ki ek time me sirf ek thread hi counter variable ko modify kar sake,

def increment_counter():
    global counter
    for _ in range(100000):
        with lock:# with statement ke andar lock acquire ho jata hai aur with block ke end me automatically release ho jata hai, isse hume manually lock.acquire() aur lock.release() likhne ki zarurat nahi padti, ye ensure karta hai ki agar with block ke andar koi exception bhi aata hai to lock release ho jayega, isse deadlock ka risk kam ho jata hai
            counter+=1

threads=[threading.Thread(target=increment_counter) for _ in range(5)]
for t in threads:
    t.start()
for t in threads:
    t.join()
print(f"Final counter value: {counter}")