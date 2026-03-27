# ⚠️ Exception Handling in Python (Basics)

---

## 📌 Introduction

* New section: **Exception Handling**
* Code me bhi real world jaise problems aati hain

---

# 🧠 Real World Analogy

* Chai shop me problems:

  * milk spill
  * missing ingredient
  * brewing issue

👉 Same code me bhi:

* errors aa sakte hain

---

# 🎯 Goal

* Errors ko:
  👉 gracefully handle karna

* Program crash nahi hona chahiye

---

# 🧠 Core Idea

* Problems inevitable hain
* Important hai:
  👉 unhe handle kaise karte hain

---

# 🛠️ Example Scenario

```python id="a1k9mz"
orders = ["masala", "ginger"]
print(orders[2])
```

---

## ❌ Output

* IndexError (list index out of range)

---

## 🧠 Concept

* Index exist nahi karta
* Error throw hota hai

---

# 🔍 Types of Errors

---

## 1️⃣ Index Error

* Jab index exist nahi karta

---

## 2️⃣ Key Error

* Jab dictionary me key missing ho

---

## 3️⃣ Zero Division Error

* Jab number ko 0 se divide karte hain

---

## 4️⃣ Type Error

* Jab incompatible types use hote hain

  * string + integer

---

## 5️⃣ Name Error

* Jab variable defined nahi hota

---

# 🧠 Important Observation

* Sab errors yaad rakhna zaruri nahi
* Error message dekh ke samajh aa jata hai

---

# 🔍 Python Improvement

* New Python versions me:

  * better error messages
  * debugging easy ho gaya hai

---

# 📌 Key Points

* Errors real world jaise hi hote hain
* Program crash nahi hona chahiye
* Errors ko handle karna important hai
* Different types ke errors exist karte hain
* Error message se understanding milti hai

---

# 🎯 Final Idea

* Exception handling ka purpose:
  👉 errors ko gracefully handle karna

---

## 📎 Source

Based on transcript 


# ⚙️ Exception Handling in Python (try-except, else, finally)

---

## 📌 Introduction

* Ab error handling ka syntax seekhenge
* Goal:
  👉 program crash na ho
  👉 errors gracefully handle ho

---

# 🛠️ Example (Key Error)

```python id="a1k9mz"
chai_menu = {
    "masala": 30,
    "ginger": 40
}

print(chai_menu["elaichi"])
```

---

## ❌ Output

* KeyError

---

## 🧠 Problem

* Key exist nahi karti
* Program crash ho jata hai

---

# 🔁 Solution → try-except

---

## 🛠️ Syntax

```python id="p4d8xy"
try:
    print(chai_menu["elaichi"])
except KeyError:
    print("the key that you are trying to access does not exist")
```

---

## 🧠 Concept

* `try`:

  * risky code likhte hain
* `except`:

  * error handle karta hai

---

# 🔍 Important Observation

* Error aane par:

  * custom message print hota hai
  * program crash nahi hota

---

# ⚡ Important Use Case

* Sensitive operations:

  * database calls
  * file open
  * web requests

👉 Inhe try block me wrap karte hain

---

# 🔁 Exception Object

```python id="k7m2vx"
except ValueError as e:
    print(e)
```

---

## 🧠 Concept

* `e` → error object
* actual error message print kar sakte hain

---

# 🧱 Advanced Example

```python id="z2p8qn"
def serve_chai(flavor):
    try:
        print(f"preparing {flavor} chai...")
        
        if flavor == "unknown":
            raise ValueError("we don't know that flavor")
```

---

## 🧠 Concept

* `raise`:

  * manually error throw karna

---

# 🔁 except Block

```python id="x2m9vx"
    except ValueError as e:
        print(e)
```

---

# 🔁 else Block

```python id="n5k3rt"
    else:
        print(f"{flavor} chai is served")
```

---

## 🧠 Concept

* `else`:

  * tab run hota hai jab error nahi aata

---

# 🔁 finally Block

```python id="y8p2qs"
    finally:
        print("next customer please")
```

---

## 🧠 Concept

* `finally`:

  * hamesha run hota hai
  * error aaye ya na aaye

---

# 🧪 Function Calls

```python id="h9m2zx"
serve_chai("masala")
serve_chai("unknown")
```

---

# 🧠 Execution Flow

---

## Case 1: Valid Flavor

* preparing masala chai
* masala chai is served
* next customer please

---

## Case 2: Invalid Flavor

* preparing unknown chai
* error print → we don't know that flavor
* next customer please

---

# 🔍 Important Observation

* Error aane par:

  * else block execute nahi hota
* finally block:

  * hamesha execute hota hai

---

# 📌 Key Points

* try → risky code
* except → error handling
* else → no error case
* finally → always run
* raise → manually error throw
* error object (`e`) → message access

---

# 🎯 Final Idea

* Exception handling:
  👉 program ko safe banata hai
  👉 crash hone se bachata hai

---

## 📎 Source

Based on transcript 


# ⚠️ Multiple Exception Handling in Python

---

## 📌 Introduction

* Ek hi time par multiple exceptions aa sakte hain
* Unhe handle karna seekhna important hai

---

# 🧠 Idea

* Different errors ke liye:
  👉 different `except` blocks use kar sakte hain

---

# 🛠️ Example Function

```python id="a1k9mz"
def process_order(item, quantity):
    try:
        price = {"masala": 20}[item]
        cost = price * quantity
        print(f"total cost is {cost}")
```

---

## 🧠 Concept

* Dictionary se price nikal rahe hain
* Cost = price * quantity

---

# 🔁 Exception 1 → KeyError

```python id="p4d8xy"
    except KeyError:
        print("sorry that chai is not on menu")
```

---

## 🧠 Concept

* Agar item exist nahi karta
* KeyError aata hai

---

# 🔁 Exception 2 → TypeError

```python id="k7m2vx"
    except TypeError:
        print("quantity must be in number")
```

---

## 🧠 Concept

* Agar quantity number nahi hai
* TypeError aata hai

---

# 🧪 Function Calls

```python id="z2p8qn"
process_order("ginger", 2)
process_order("masala", "2")
```

---

# 🧠 Execution Flow

---

## Case 1: Invalid Item

* "ginger" dictionary me nahi hai
  👉 KeyError
  👉 Output: sorry that chai is not on menu

---

## Case 2: Invalid Quantity

* "2" string hai
  👉 multiplication me issue
  👉 TypeError
  👉 Output: quantity must be in number

---

# 🔍 Important Observation

* Har error ke liye separate handling
* Program crash nahi hota

---

# ⚠️ Special Case (Operator Overloading)

* String * number:
  👉 Python allow karta hai
* Unexpected output mil sakta hai

---

## 🧠 Insight

* Code smart lagta hai
* But edge cases handle karna zaruri hai

---

# 🔁 Improvement Idea

* Input ko number me convert karna
* Validation add karna

---

# 📌 Key Points

* Multiple `except` blocks use kar sakte hain
* Har error ka alag handling hota hai
* KeyError → missing key
* TypeError → wrong type
* Operator overloading unexpected behavior de sakta hai

---

# 🎯 Final Idea

* Real world code:
  👉 multiple error handling use karta hai
  👉 validation important hoti hai

---

## 📎 Source

Based on transcript 


# 🚨 Raising Custom Exceptions in Python

---

## 📌 Introduction

* Hum apni **khud ki exceptions raise kar sakte hain**
* Code ke through samjhaya gaya

---

# 🛠️ Example Function

```python id="a1k9mz"
def brew_chai(flavor):
```

---

## 🧠 Concept

* Function chai flavor leta hai

---

# 🔁 Allowed Flavors

```python id="p4d8xy"
flavors = ["masala", "ginger", "elaichi"]
```

---

## 🧠 Concept

* Sirf ye flavors allowed hain

---

# 🔁 Condition Check

```python id="k7m2vx"
if flavor not in flavors:
```

---

## 🧠 Concept

* Check karte hain:

  * flavor allowed hai ya nahi

---

# 🚨 Raise Exception

```python id="z2p8qn"
raise ValueError("unsupported chai flavor")
```

---

## 🧠 Concept

* `raise`:

  * manually error throw karta hai
* `ValueError`:

  * wrong value ke liye use hota hai

---

# 🔁 Valid Case

```python id="x2m9vx"
print(f"brewing {flavor} chai")
```

---

## 🧠 Concept

* Agar flavor valid hai
* Chai prepare hoti hai

---

# 🧪 Function Call

```python id="n5k3rt"
brew_chai("coffee")
```

---

## ❌ Output

* ValueError → unsupported chai flavor

---

## 🧠 Observation

* Program error throw karta hai
* Custom message show hota hai

---

# 🔍 Important Insight

* Har error handle karna zaruri nahi
* Kabhi-kabhi error raise karna bhi useful hota hai

---

# 📌 Key Points

* `raise` → custom error throw karta hai
* ValueError → invalid input ke liye
* Condition check important hai
* Allowed values define karte hain
* Invalid input → error

---

# 🎯 Final Idea

* Custom exception:
  👉 control deta hai ki kab error throw karna hai

---

## 📎 Source

Based on transcript 


# 🧩 Custom Exception Classes in Python

---

## 📌 Introduction

* Hum predefined errors (ValueError, KeyError, etc.) use kar rahe the
* But kabhi-kabhi ye enough nahi hote
  👉 Tab hum apne **custom exception classes** bana sakte hain

---

# 🧠 Core Idea

* Custom exception = ek class
* Ye `Exception` se inherit karti hai

---

# 🛠️ Custom Exception Create

```python id="a1k9mz"
class OutOfIngredientsError(Exception):
    pass
```

---

## 🧠 Concept

* Class bana di
* `Exception` se inherit kiya
* `pass` → abhi kuch extra logic nahi

---

# 🔁 Function Example

```python id="p4d8xy"
def make_chai(milk, sugar):
```

---

## 🧠 Concept

* Function chai banata hai
* Inputs:

  * milk
  * sugar

---

# 🔁 Condition Check

```python id="k7m2vx"
if milk == 0 or sugar == 0:
```

---

## 🧠 Concept

* Agar milk ya sugar zero hai
  👉 chai nahi ban sakti

---

# 🚨 Raise Custom Exception

```python id="z2p8qn"
raise OutOfIngredientsError("missing milk or sugar")
```

---

## 🧠 Concept

* Apna custom error throw kar rahe hain
* Message bhi define kiya

---

# 🔁 Valid Case

```python id="x2m9vx"
print("chai is ready...")
```

---

## 🧠 Concept

* Agar sab sahi hai
  👉 chai ready

---

# 🧪 Function Call

```python id="n5k3rt"
make_chai(0, 1)
```

---

## ❌ Output

* OutOfIngredientsError → missing milk or sugar

---

## 🧠 Observation

* Custom error show hota hai
* Python ke default errors se different

---

# 🔍 Important Insight

* Custom exceptions:

  * frameworks me use hote hain
  * libraries me use hote hain

---

# ⚠️ Important Note

* Kabhi-kabhi program crash karna bhi sahi hota hai
* Example:

  * database connection fail ho jaye
  * to program stop karna better hai

---

# 📌 Key Points

* Custom exception = class
* `Exception` se inherit karte hain
* `raise` se use karte hain
* Message customize kar sakte hain
* Real-world apps me useful

---

# 🎯 Final Idea

* Custom exceptions:
  👉 control dete hain error handling par
  👉 meaningful errors create karne me help karte hain

---

## 📎 Source

Based on transcript 


# 🧾 Complete Exception Handling App (Chai Billing)

---

## 📌 Introduction

* Is section me ek **complete app build kiya gaya**
* Goal:
  👉 jitna bhi seekha hai sab use karna

---

## 🧠 Idea

* Ek simple **bill generation app**
* Saare validations + exception handling use kiye gaye

---

# 🧩 Custom Exception

```python id="a1k9mz"
class InvalidChaiError(Exception): pass
```

---

## 🧠 Concept

* Custom exception banaya
* One-line class definition

---

# 🛠️ Bill Function

```python id="p4d8xy"
def bill(flavor, cups):
```

---

## 🧠 Inputs

* flavor → chai type
* cups → number of cups

---

# 📦 Menu

```python id="k7m2vx"
menu = {
    "masala": 20,
    "ginger": 40
}
```

---

## 🧠 Concept

* Dictionary me chai + price

---

# 🔁 Check Flavor

```python id="z2p8qn"
if flavor not in menu:
    raise InvalidChaiError("chai is not available")
```

---

## 🧠 Concept

* Invalid flavor → custom error

---

# 🔁 Check Cups Type

```python id="x2m9vx"
if not isinstance(cups, int):
    raise TypeError("number of cups must be an integer")
```

---

## 🧠 Concept

* `isinstance()`:

  * type check karta hai
* Cups integer hona chahiye

---

# 💰 Calculate Total

```python id="n5k3rt"
total = menu[flavor] * cups
```

---

## 🧠 Concept

* Price × cups

---

# 🖨️ Print Bill

```python id="y8p2qs"
print(f"your bill for {cups} cups of {flavor} chai is rupees {total}")
```

---

## 🧠 Concept

* Formatted output

---

# ⚠️ Exception Handling

```python id="h9m2zx"
except Exception as e:
    print(e)
```

---

## 🧠 Concept

* Error catch karte hain
* `e` → error object

---

# 🔁 Finally Block

```python id="q1w7dv"
finally:
    print("thank you for visiting chai code!")
```

---

## 🧠 Concept

* Always execute hota hai

---

# 🧪 Test Cases

---

## Case 1

```python id="y4t8qs"
bill("mint", 2)
```

* Output:

  * chai is not available
  * thank you for visiting

---

## Case 2

```python id="r3k9fs"
bill("masala", "3")
```

* Output:

  * number of cups must be an integer
  * thank you for visiting

---

## Case 3

```python id="p1x7dv"
bill("ginger", 3)
```

* Output:

  * bill printed
  * thank you message

---

# 🔍 Observation

* Har case properly handle hua
* Errors bhi handle hue
* Valid case bhi work kiya

---

# 📌 Key Points

* Custom exception use kiya
* Type checking kiya
* Dictionary use ki
* Exception handling (`try-except-finally`)
* Formatted output
* Multiple test cases

---

# 🎯 Final Idea

* Real-world app me:
  👉 validation + exception handling zaruri hai
  👉 proper flow maintain hota hai

---

## 📎 Source

Based on transcript 


# 📂 File Handling in Python (Basics)

---

## 📌 Introduction

* Python me bahut types ke files handle karte hain:

  * PDFs
  * CSVs
  * JSON
  * Excel

* Libraries help karti hain (example: Pandas)

* But hume **basic file handling** bhi aana chahiye

---

# 🧠 Core Idea

* Python me file open karne ke liye:
  👉 `open()` function use hota hai

---

# 🛠️ Basic Syntax

```python id="a1k9mz"
file = open("order.txt", "w")
```

---

## 🧠 Concept

* `"order.txt"` → file name
* `"w"` → write mode

---

# ✍️ Writing to File

```python id="p4d8xy"
file.write("masala chai 2 cups")
```

---

## 🧠 Concept

* File me data write hota hai

---

# ⚠️ Problem (Crash Case)

* Agar program crash ho jaye:

  * file corrupt ho sakti hai
  * memory issues ho sakte hain

---

## 🧠 Reason

* File memory me load hoti hai
* Crash hone se:

  * data properly save nahi hota

---

# 🔁 Solution → try-finally

```python id="k7m2vx"
try:
    file = open("order.txt", "w")
    file.write("masala chai 2 cups")
finally:
    file.close()
```

---

## 🧠 Concept

* `finally`:

  * hamesha run hota hai
* File safely close hoti hai

---

# 🔍 Observation

* File automatically create hoti hai
* Agar exist nahi karti

---

# ⚡ Better Way → with

```python id="z2p8qn"
with open("order.txt", "w") as file:
    file.write("ginger tea 4 cups")
```

---

## 🧠 Concept

* `with`:

  * automatically file handle karta hai
  * close bhi automatically hota hai

---

## 📌 Important

* Try-finally ki zarurat nahi
* Cleaner syntax

---

# 🔍 Behind the Scene

---

## 🧠 Dunder Methods

* `__enter__`:

  * file open hone par run hota hai

* `__exit__`:

  * file close hone par run hota hai

---

## 🧠 Concept

* `with`:
  👉 internally ye methods call karta hai

---

# 📂 File Creation Example

* Agar file exist nahi:

  * automatically create ho jati hai

---

# 📌 Important Notes

* `"w"` mode → write
* File memory me load hoti hai
* Crash → data loss ho sakta hai
* `with` best practice hai
* Dunder methods automatically handle karte hain

---

# ⚠️ Libraries

* Binary files ke liye:

  * Pillow

* CSV / Excel:

  * Pandas

👉 Raw Python se sab handle nahi karte

---

# 🎯 Final Idea

* File handling:
  👉 safe tarike se karni chahiye
  👉 `with` use karna best practice hai

---

## 📎 Source

Based on transcript 
