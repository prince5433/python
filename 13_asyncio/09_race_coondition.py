#race condition is a situation where two or more tasks are trying to access the same resource at the same time, and the outcome depends on the order in which they access the resource. This can lead to unpredictable behavior and bugs in your code.

import threading
chai_stock = 0

def restock():
    global chai_stock
    for i in range(100000):
        chai_stock += 1

threads = [threading.Thread(target=restock) for _ in range(2)]
# yahe pe 2 threads create ho rahe hain jo restock function ko run karenge, aur dono threads chai_stock variable ko access karenge. Iska matlab hai ki dono threads ek hi resource (chai_stock) ko access kar rahe hain, aur agar dono threads ek hi time pe chai_stock ko update karne ki koshish kar rahe hain, toh race condition ho sakta hai, jisme final chai_stock value unpredictable ho sakti hai. Iska solution ye hai ki aap threading.Lock() ka use karke critical section ko protect kar sakte hain, jisse ki ek time pe sirf ek thread hi chai_stock ko update kar sake.
for t in threads:
    t.start()
for t in threads:
    t.join()
print(f"Final chai stock: {chai_stock}")