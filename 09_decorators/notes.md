# 🎨 Decorators in Python (Basics)

---

## 📌 Introduction

* New topic: **Decorators**
* Generators ke baad aata hai
* Similar lagte hain but actually different hain

---

## 🧠 Core Idea

* Decorator = **decoration / wrapper**
* Function ke upar extra layer add karna

---

## ☕ Analogy

* Coffee ke upar chocolate powder → decoration
* Same tarah function ke upar extra functionality

---

## 📌 Purpose

* Function ko change kiye bina:

  * extra behavior add karna

---

# 🧠 Concept

* Decorator:

  * ek function hota hai
  * jo dusre function ko wrap karta hai

---

## 📌 Important

* Original function change nahi hota
* Bas uske around wrapper lagta hai

---

# 🔁 Basic Structure

---

## 🛠️ Decorator Function

```python id="a1k9mz"
def mydecorator(func):
    def wrapper():
        print("before function runs")
        func()
        print("after function runs")
    return wrapper
```

---

## 🧠 Concept

* `func` → jo function pass ho raha hai
* `wrapper` → actual execution control karta hai

---

# 🔁 Using Decorator

---

## 🛠️ Syntax

```python id="p4d8xy"
@mydecorator
def greet():
    print("hello from decorators class from chai code")
```

---

## 🧠 Concept

* `@mydecorator`:

  * niche wale function ko wrap karta hai

---

# ▶️ Execution

```python id="k7m2vx"
greet()
```

---

## 🧠 Output Flow

1. before function runs
2. original function run
3. after function runs

---

# 🔍 Important Observation

* Agar decorator hata diya:

  * sirf original function chalega

---

# 🧠 Key Idea

* Decorator:

  * function ko wrap karta hai
  * extra code run karta hai

---

# ⚠️ Problem (Metadata Issue)

---

## 🛠️ Example

```python id="z2p8qn"
print(greet.__name__)
```

---

## ❗ Output

* wrapper

---

## 🧠 Problem

* Original function name lost ho jata hai
* Metadata change ho jata hai

---

# 🧠 Metadata

* Data about data
* Example:

  * file ka format
  * duration
  * size

---

# 🔁 Solution: functools.wraps

---

## 🛠️ Import

```python id="x2m9vx"
from functools import wraps
```

---

## 🛠️ Use

```python id="n5k3rt"
def mydecorator(func):
    @wraps(func)
    def wrapper():
        print("before function runs")
        func()
        print("after function runs")
    return wrapper
```

---

## 🧠 Concept

* `wraps(func)`:

  * original function ka metadata preserve karta hai

---

## 🖨️ Result

```python id="y8p2qs"
print(greet.__name__)
```

👉 Output: greet

---

# 🧠 Summary

* Decorator = wrapper function
* Function ke around extra behavior add karta hai
* `@decorator` syntax use hota hai
* Metadata issue aata hai
* `functools.wraps` se fix hota hai

---

## 📌 Final Idea

* Decorator:

  * function leta hai
  * execute karta hai
  * extra logic add karta hai
  * wrapper return karta hai

---

## 📎 Source

Based on transcript 


# 📝 Logging Decorator in Python

---

## 📌 Introduction

* Decorators ke kaafi use cases hote hain
* Django, FastAPI me extensively use hote hain
* Best way seekhne ka → khud bana ke

👉 Yahan ek **logging decorator** banaya gaya hai

---

# 🧠 Idea

* Function call hone se pehle:

  * log karna
* Function complete hone ke baad:

  * log karna

---

# 🔁 Basic Setup

---

## 🛠️ Import

```python id="a1k9mz"
from functools import wraps
```

---

# 🛠️ Decorator Function

```python id="p4d8xy"
def logactivity(func):
    @wraps(func)
    def wrapper(*args, **kwargs):
        print(f"calling {func.__name__}")
        result = func(*args, **kwargs)
        print(f"finished {func.__name__}")
        return result
    return wrapper
```

---

## 🧠 Concept

* `func` → original function
* `wrapper`:

  * sab arguments accept karta hai (`*args`, `**kwargs`)
* `func.__name__`:

  * function ka naam

---

## 📌 Important

* `*args` → multiple positional arguments
* `**kwargs` → keyword arguments

👉 Unknown inputs handle karne ke liye

---

# 🔁 Using Decorator

---

## 🛠️ Example Function

```python id="k7m2vx"
@logactivity
def brew_chai(type):
    print(f"brewing {type} chai")
```

---

## ▶️ Call

```python id="z2p8qn"
brew_chai("masala")
```

---

## 🧠 Output Flow

1. calling brew_chai
2. brewing masala chai
3. finished brew_chai

---

# 🔍 Important Observation

* Decorator automatically:

  * function call track karta hai
  * logging add karta hai

---

# 🔁 Handling More Parameters

---

## 🛠️ Updated Function

```python id="x2m9vx"
@logactivity
def brew_chai(type, milk="no"):
    print(f"brewing {type} chai")
    print(f"milk status {milk}")
```

---

## 🧠 Concept

* Function change ho gaya
* Decorator ko change nahi karna pada

👉 Because:

* `*args`, `**kwargs` sab handle kar lete hain

---

# 📌 Key Points

* Logging decorator:

  * function call track karta hai
* `wraps`:

  * metadata preserve karta hai
* `*args`, `**kwargs`:

  * flexible input handling
* Function change ho sakta hai
* Decorator same rehta hai

---

# 🧠 Final Idea

* Decorator reusable hota hai
* Ek hi decorator multiple functions pe use ho sakta hai
* Logging easily add kar sakte hain

---

## 📎 Source

Based on transcript 

# 🔐 Auth Decorator (Require Admin)

---

## 📌 Introduction

* Ek aur type ka decorator build kiya gaya
* Django jaise frameworks me bahut use hota hai
* Production me seekhne wali cheez hai

👉 Example: **Admin-only access decorator**

---

# 🧠 Idea

* Function ko wrap karna
* Sirf admin ko access dena
* Baaki users ko deny karna

---

# 🔁 Basic Setup

---

## 🛠️ Decorator Definition

```python id="a1k9mz"
from functools import wraps

def require_admin(func):
    @wraps(func)
    def wrapper(user_role):
        if user_role != "admin":
            print("access denied, admins only")
        else:
            return func(user_role)
    return wrapper
```

---

## 🧠 Concept

* `func` → original function
* `wrapper` → execution control karta hai
* `user_role` → input parameter

---

# 🔁 Using Decorator

---

## 🛠️ Example Function

```python id="p4d8xy"
@require_admin
def access_tea_inventory(user_role):
    print("access granted to tea inventory")
```

---

# ▶️ Function Calls

```python id="k7m2vx"
access_tea_inventory("user")
access_tea_inventory("admin")
```

---

## 🧠 Expected Behavior

* "user" → access denied
* "admin" → function execute

---

# 🔍 Observation

* User role check hota hai
* Agar admin nahi → function block
* Agar admin → function run

---

# ⚠️ Important Case

* Kabhi-kabhi error aa sakta hai
* Jab function return nahi karta

---

## 🧠 Fix

```python id="z2p8qn"
return None
```

---

## 🧠 Concept

* Explicit return likhna safe hota hai
* Python me default return → None hota hai
* Old codebases me required hota tha

---

# 📌 Notes

* Error har baar nahi aata
* Python version pe depend karta hai
* Explicit return likhna better practice hai

---

# 🧠 Key Points

* Decorator = access control
* Admin check implement kiya
* Wrapper function role check karta hai
* Function execution control hota hai
* Explicit return safe hota hai

---

## 📎 Source

Based on transcript 
