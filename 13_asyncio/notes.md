# ⚡ Async Python (Asyncio) – COMPLETE NOTES

---

# 📌 Introduction

* Async Python = **Asynchronous Programming**
* Python ko ek **new perspective** deta hai
* Modern frameworks like:
  👉 FastAPI async ka heavy use karte hain

👉 Async ka concept chhota hai
👉 BUT implementation bahut wide hai 

---

# 🧠 Prerequisites

Async samajhne se pehle aana chahiye:

* Threading
* Multiprocessing
* Locks / Mutex

👉 Ye sab already covered hone chahiye 

---

# ❗ Why Async Needed?

## ⚙️ Problem with Threading & Multiprocessing

* Threading:
  ❌ GIL issue

* Multiprocessing:
  ❌ Heavy (memory + process creation overhead)

---

## 🎯 Better Approach

👉 For IO-bound tasks → use Async

---

## 📌 IO-bound Examples

* API calls
* Database queries
* File reading
* HTTP requests

👉 Example:

* 100 API calls
* 20 files read
* 10 web pages fetch

➡️ Async sabko efficiently handle karta hai 

---

# 🚫 Blocking vs Non-Blocking

---

## ❌ Blocking Code

```python
time.sleep(3)
```

* pura program ruk jata hai
* next task wait karega

---

## ✅ Non-Blocking (Async)

```python
await asyncio.sleep(3)
```

* wait karta hai
* BUT dusre tasks chal sakte hain

👉 main thread block nahi hota 

---

# ⚡ Core Concepts (MOST IMPORTANT)

---

# 1️⃣ async Keyword

```python
async def func():
```

👉 normal function nahi
👉 coroutine banata hai

---

## 🧠 Coroutine kya hota hai?

👉 Special function
👉 pause ho sakta hai

✔ Resume bhi ho sakta hai

👉 Basically:

> "Pauseable function" 

---

# 2️⃣ await Keyword

```python
await some_task()
```

👉 kaam:

* execution pause karega
* jab tak result ready nahi

---

## 🧠 Important

* await sirf async function ke andar hi use hota hai

---

## 🎯 Real Meaning

👉 "Wait here, but block mat karo"

👉 dusre tasks run ho sakte hain

---

# 🔥 Important Confusion Clear

❌ Async ≠ background execution

✅ Async =
👉 wait gracefully
👉 while handling other tasks



---

# 3️⃣ asyncio Library

```python
import asyncio
```

👉 built-in Python library

👉 async programming ka backbone

---

# 4️⃣ Event Loop (MOST IMPORTANT)

---

## 🧠 Definition

👉 Event loop = engine

👉 coroutines ko:

* run karta hai
* schedule karta hai

---

## 📌 Kaam kya hai?

* tasks ko queue me daalta hai
* check karta hai kaun ready hai
* resume karta hai

---

## 🔁 Flow

1. task start
2. await → pause
3. event loop → next task
4. task ready → resume

---

## 🧠 Simple Meaning

👉 "Traffic controller of async tasks"

---

# 🔥 Event Queue

* saare paused tasks yaha store hote hain
* event loop continuously check karta hai

---

# 🧪 Basic Async Code

```python
import asyncio

async def brew_chai():
    print("Brewing chai...")
    await asyncio.sleep(2)
    print("Chai is ready")

asyncio.run(brew_chai())
```

---

## 🧠 Output Flow

* start
* wait (non-blocking)
* finish

---

# ⚡ Async vs time.sleep()

---

## ❌ time.sleep()

* blocking
* sequential execution

---

## ✅ asyncio.sleep()

* non-blocking
* concurrent execution

---

# 🚀 Multiple Coroutines (IMPORTANT)

---

## 📌 Using asyncio.gather()

```python
import asyncio

async def brew(name):
    print(f"Brewing {name}")
    await asyncio.sleep(2)
    print(f"{name} ready")

async def main():
    await asyncio.gather(
        brew("Masala chai"),
        brew("Green chai"),
        brew("Ginger chai")
    )

asyncio.run(main())
```

---

## 🧠 Key Insight

👉 sab tasks **parallel-like execute hote hain**

👉 total time ≈ max time
👉 NOT sum of times

---

## 🎯 Example

* 3 tasks × 2 sec

👉 total = ~2 sec (NOT 6 sec)



---

# ⚠️ Important Observation

---

## Async Version

* sab ek saath run
* fast

---

## time.sleep Version

* ek ke baad ek
* slow

---

# 🧠 Real World Analogy

---

## ❌ Blocking

👉 ek chai banake dusri start

---

## ✅ Async

👉 sab chai ek saath process

---

# 🚀 Why Async is Powerful?

* non-blocking
* high scalability
* better performance

👉 FastAPI fast kyun hai?
👉 Async ki wajah se 

---

# ⚡ When to Use What?

---

## 🧵 Threading

* IO-bound
* lightweight

---

## ⚙️ Multiprocessing

* CPU-bound
* heavy computation

---

## ⚡ Async

* IO-bound
* high concurrency
* best performance

---

# 🔥 Final Summary

---

## 🧠 Async Core

* async → coroutine
* await → pause
* asyncio → library
* event loop → scheduler

---

## 🎯 Golden Rule

👉 CPU-bound → multiprocessing
👉 IO-bound → async

---

## 🚀 Key Takeaway

👉 Async =
**"Do multiple tasks efficiently without blocking main thread"**

---

## 📎 Source

Based on transcript 
