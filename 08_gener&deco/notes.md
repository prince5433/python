# ⚡ Generators in Python (Basics)

---

## 📌 Introduction

* New section: **Generators**
* Interesting concept hai
* Comprehensions se easy hai
* Bas difference samajhna hai:

  * normal function vs generator

---

# 🧠 Core Idea

👉 Normal function:

* Result **immediately return** karta hai
* Sab kuch memory me load hota hai

👉 Generator:

* **Ek-ek value generate karta hai**
* One-by-one result deta hai

---

## 📌 Important

* Generators memory optimized hote hain
* Har jagah use nahi karte
* Use-case based concept hai

---

# 🧠 Key Points

* Memory save karta hai
* Har value ek-ek karke milti hai
* Sab kuch ek saath load nahi hota

---

# 🔑 Important Keyword

👉 `yield`

* Generator me use hota hai
* `return` ki jagah use hota hai

---

# 🧠 Important Concepts

* Save memory
* Result immediately nahi chahiye
* Lazy evaluation

---

# 🛠️ Generator Definition

```python id="g1k9pz"
def serve_chai():
    yield "masala chai"
    yield "ginger chai"
    yield "elaichi chai"
```

---

## 🧠 Concept

* Function jaisa hi dikhta hai
* Bas `return` ki jagah `yield` use hota hai
* Ek-ek value return hoti hai

---

# 🧪 Using Generator

```python id="p4d8xy"
stall = serve_chai()
```

---

## 🧠 Observation

* Ye directly values nahi deta
* Sirf **reference hold karta hai**

---

## 🖨️ Output Type

👉 Generator object

---

# 🔁 Iterating Generator

```python id="k7m2vx"
for cup in serve_chai():
    print(cup)
```

---

## 🧠 Concept

* Loop run hone par values generate hoti hain
* Ek-ek karke

---

# 🔁 Working Behind the Scene

* Generator turant execute nahi hota
* Reference hold karta hai
* Jab loop ya next call hoti hai → tab run hota hai

---

# ⚡ Using next()

---

## 🛠️ Example

```python id="z2p8qn"
chai = serve_chai()

print(next(chai))
print(next(chai))
print(next(chai))
```

---

## 🧠 Output

* masala chai
* ginger chai
* elaichi chai

---

## 🧠 Concept

* `next()`:

  * function ko ek step run karta hai
  * next value deta hai

---

# ⏸️ Important Behavior

👉 Generator:

* Pause ho jata hai
* Next call par wahi se resume hota hai

---

# ❗ StopIteration Error

* Jab saari values khatam ho jati hain
* Next call → error

---

## 🧠 Concept

* Limited values yield karta hai
* Uske baad function complete ho jata hai

---

# 🔁 Generator vs Normal Function

---

## 🛠️ Normal Function

```python id="r2k6dv"
def get_chai_list():
    return ["cup1", "cup2", "cup3"]
```

---

## 🛠️ Generator Function

```python id="y8p4qs"
def get_chai_gen():
    yield "cup1"
    yield "cup2"
    yield "cup3"
```

---

## 🧠 Difference

* Normal → list return karta hai
* Generator → values ek-ek karke deta hai

---

# 📌 Key Points

* Generator = function + yield
* Memory efficient
* Lazy execution
* `next()` se control kar sakte hain
* Loop me use hota hai
* StopIteration error aata hai end me

---

## 📎 Source

Based on transcript 


# ♾️ Infinite Generators in Python

---

## 📌 Introduction

* Python me ek concept hota hai → **Infinite Generators**
* Kam use hote hain
* But kuch cases me useful hote hain
* AI aur real-time systems me use badh raha hai

---

## 🧠 Use Cases

* Streams
* Real-time systems
* Continuous logs / updates

---

## ⚠️ Important

* Carefully use karo
* Memory drain ho sakti hai
* Strong memory system chahiye

---

# 🛠️ Infinite Generator Example

```python id="i7k2pl"
def infinitechai():
    count = 1
    while True:
        yield f"refill {count}"
        count += 1
```

---

## 🧠 Concept

* `while True` → infinite loop
* `yield` → ek-ek value return karta hai
* Count track karta hai kitni baar refill hua

---

# ⚠️ Important Idea

* Normal loop me ye dangerous hota
* But generator me manageable hai
* Kyunki ek time pe ek value aati hai

---

# 🔁 Using Generator

---

## 🛠️ Example

```python id="x2m9vx"
chai = infinitechai()

for _ in range(3):
    print(next(chai))
```

---

## 🧠 Output

* refill 1
* refill 2
* refill 3

---

## 🧠 Concept

* Generator infinite hai
* But hum `range` se control kar rahe hain

---

# 🔍 Important

* Generator khud stop nahi karega
* User ko control karna padega

---

# 🔁 Multiple Users

---

## 🛠️ Example

```python id="n5k3rt"
user1 = infinitechai()
user2 = infinitechai()
```

---

## 🛠️ Usage

```python id="y8p2qs"
for _ in range(3):
    print(next(user1))

for _ in range(6):
    print(next(user2))
```

---

## 🧠 Observation

* Dono generators alag track karte hain
* Values mix nahi hoti

---

## 🧠 Concept

* Har generator instance independent hota hai
* Same function → multiple separate states

---

# 📌 Key Points

* Infinite generator = endless values
* `while True` use hota hai
* `yield` value deta hai
* Control user ke haath me hota hai
* Multiple instances independent hote hain

---

## 📎 Source

Based on transcript 


# 🔁 Advanced Generators (send & yield interaction)

---

## 📌 Introduction

* Ab tak humne **basic yield usage** dekha
* Ye common use hai
* But ek aur advanced use case bhi hota hai

👉 **Generator ko data send karna**

---

## 🧠 Core Idea

* Normally:

  * `yield` → data return karta hai

👉 But:

* Caller bhi generator ko data **send kar sakta hai**

---

# 🔁 Two-way Communication

* Generator:

  * data deta hai
* Caller:

  * data bhej sakta hai

👉 Dono taraf interaction possible hai

---

# 🛠️ Example: Chai Customer

```python id="c7k2pl"
def chai_customer():
    print("welcome! what chai would you like?")
    order = yield

    while True:
        print(f"preparing {order}")
        order = yield
```

---

## 🧠 Concept

* `order = yield`:

  * yield se value receive bhi ho sakti hai
* Generator pause hota hai aur input wait karta hai

---

# 🔁 Using Generator

---

## 🛠️ Setup

```python id="x2m9vx"
stall = chai_customer()
```

---

## 🧠 Concept

* Ye sirf reference banata hai
* Execution start nahi hota

---

# ▶️ Start Generator

```python id="n5k3rt"
next(stall)
```

---

## 🧠 Concept

* Generator start hota hai
* First print execute hota hai
* Yield par pause ho jata hai

---

# 📤 Sending Data

---

## 🛠️ Example

```python id="y8p2qs"
stall.send("masala chai")
```

---

## 🧠 Flow

* `send()` → value generator ko deta hai
* `order = yield` → us value ko store karta hai
* Fir print hota hai → preparing masala chai

---

# 🔁 Sending Next Value

```python id="h9m2zx"
stall.send("lemon chai")
```

---

## 🧠 Concept

* Generator resume hota hai
* New value receive karta hai
* Fir print → preparing lemon chai

---

# ⚠️ Important Case

👉 Agar ye line hata di:

```python id="q1w7dv"
order = yield
```

---

## ❗ Result

* Infinite loop chalne lagega
* Program continuously run karega
* Memory issue ho sakta hai

---

## 🧠 Reason

* `while True` loop hai
* Koi pause point nahi hai
* Yield hi pause control karta hai

---

# 🔍 Detailed Flow

---

## Step 1

```python id="y4t8qs"
stall = chai_customer()
```

* Reference create hota hai

---

## Step 2

```python id="r3k9fs"
next(stall)
```

* Generator start hota hai
* Print hota hai
* Yield par pause

---

## Step 3

```python id="p1x7dv"
stall.send("masala chai")
```

* Value `order` me aati hai
* While loop run hota hai
* Print → preparing masala chai
* Fir yield par pause

---

## Step 4

```python id="m8z4qn"
stall.send("lemon chai")
```

* New value receive
* Fir print → preparing lemon chai

---

# 🧠 Key Insight

* `yield`:

  * return bhi karta hai
  * receive bhi karta hai

👉 Dual behavior

---

# 📌 Important Points

* Generator ko start karne ke liye `next()` use hota hai
* `send()` se data pass karte hain
* `yield` pause + resume control karta hai
* Without yield → infinite loop issue
* Real-world frameworks me use hota hai

---

## 📎 Source

Based on transcript 


# ⚙️ Advanced Generator Concepts (yield from & close)

---

## 📌 Introduction

* Generators ke aur advanced concepts
* Ab hum dekhenge:

  * `yield from`
  * `close()`

---

## 🧠 Important Idea

* Generator:

  * kabhi khud value generate karta hai
  * kabhi dusre source se value leta hai

---

# 🔁 yield from

---

## 📌 Concept

* Dusre generator ya iterable se values lene ke liye
* Delegation jaisa kaam karta hai

---

## 🛠️ Example

```python id="a1k9mz"
def local_chai():
    yield "masala chai"
    yield "ginger chai"
```

---

```python id="p4d8xy"
def imported_chai():
    yield "matcha chai"
    yield "oolong chai"
```

---

## 🛠️ Combined Generator

```python id="k7m2vx"
def full_menu():
    yield from local_chai()
    yield from imported_chai()
```

---

## 🛠️ Usage

```python id="z2p8qn"
for chai in full_menu():
    print(chai)
```

---

## ▶️ Output

* masala chai
* ginger chai
* matcha chai
* oolong chai

---

## 🧠 Concept

* `yield from`:

  * dusre generator ko delegate karta hai
  * values automatically forward hoti hain

---

# 🔁 close() Method

---

## 📌 Concept

* Generator ko manually close karna
* Memory cleanup ke liye important

---

## 🛠️ Example

```python id="x2m9vx"
def chai_stall():
    try:
        while True:
            order = yield "waiting for chai order"
    except:
        print("stall closed, no more chai")
```

---

## 🛠️ Usage

```python id="n5k3rt"
stall = chai_stall()
next(stall)
stall.close()
```

---

## 🧠 Concept

* `close()`:

  * generator ko stop karta hai
  * cleanup trigger karta hai

---

# ⚠️ Important

* Generator automatically stop ho sakta hai
* But manually close karna better practice hai

---

## 🧠 Reason

* Memory cleanup hota hai
* Memory leaks avoid hote hain
* Performance better hoti hai

---

# 🔁 Try-Except (Try-Catch)

---

## 📌 Concept

* Python me:

  * try → code run karo
  * except → error handle karo

---

## 🧠 Note

* Dusri languages me ise **try-catch** bolte hain
* Python me → **try-except**

---

# 🧠 Summary

* `yield` → pause & resume
* `next()` → next value
* `send()` → data bhejna
* `yield from` → dusre generator se values lena
* `close()` → generator stop + cleanup

---

## 📎 Source

Based on transcript 
