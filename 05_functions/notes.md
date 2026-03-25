# 🔧 Functions in Python

## 📌 Introduction

* Functions ek **wrapper** hote hain
* Code ko wrap karke **reusable banate hain**
* Sirf reuse nahi, aur bhi advantages hain

👉 Functions ko alag-alag naam se bhi jana jata hai:

* functions
* methods

---

## 🎯 Goal of Section

* Functions ka **purpose aur benefits samajhna**
* `def` keyword se function banana
* Code ko:

  * readable
  * traceable
  * maintainable banana

---

## 🧠 Important Idea

* Functions se:

  * bada kaam → chhote parts me break hota hai
* Proper naming important hai
* Function ka naam uska kaam describe kare

---

# 🔁 Task 1: Reducing Code Duplication

## 📌 Problem

* Same code baar-baar likhna padta hai
* Isko avoid karna hai

👉 Solution:

* Function bana lo
* Jaha chahiye → call karo

---

## 🛠️ Function Create

```python id="a1k3mz"
def print_order(name, chaitype):
    print(f"{name} ordered {chaitype} chai")
```

---

## 🧠 Important Terms

* `name, chaitype` → parameters
* Function call me jo pass karte → arguments

---

## 🛠️ Function Call

```python id="p9d4xy"
print_order("aman", "masala")
print_order("hitesh", "ginger")
print_order("jia", "tulsi")
```

---

## ▶️ Output

* aman ordered masala chai
* hitesh ordered ginger chai
* jia ordered tulsi chai

---

## 🧠 Advantage

* Ek jagah change karo → sab jagah reflect hoga
* Code duplicate nahi hota

---

# 🔁 Task 2: Splitting Complex Task

## 📌 Problem

* Ek bada kaam hai (monthly report)
* Sab logic ek jagah nahi rakhna

👉 Break into smaller functions

---

## 🛠️ Step 1: Functions

```python id="z7m2ql"
def fetch_sales():
    print("fetching the sales data")
```

---

```python id="r5x8nt"
def filter_valid_sales():
    print("filtering valid sales data")
```

---

```python id="k3b9pw"
def summarize_data():
    print("summarizing sales data")
```

---

## 🛠️ Step 2: Main Function

```python id="y2c6hs"
def generate_report():
    fetch_sales()
    filter_valid_sales()
    summarize_data()
    print("report is ready")
```

---

## 🛠️ Step 3: Call Function

```python id="m8v1dk"
generate_report()
```

---

## ▶️ Output

* fetching the sales data
* filtering valid sales data
* summarizing sales data
* report is ready

---

## 🧠 Important Points

* `def` → function define karta hai
* Function tabhi run hota hai jab usse call karo
* Functions reusable hote hain
* Complex task ko chhote parts me tod sakte hain

---

## 📌 Notes

* Function naming important hai
* Code reusable + modular hota hai
* Team me kaam karne me easy hota hai

---

## 📎 Source

Based on transcript 


# 🔧 Functions – Advanced Concepts

---

# 🔒 Hiding Implementation Details

## 📌 Concept

* Function ka kaam:

  * Complexity ko hide karna
* User ko sirf result mile
* Kaise internally kaam ho raha → hidden

---

## 📌 Problem

User registration system banana hai:

### Steps:

1. Input lena
2. Validate karna
3. Database me save karna

👉 Complexity hide karni hai

---

## 🛠️ Functions

```python id="k1x9pz"
def get_input():
    print("getting user input")
```

---

```python id="v7m3ld"
def validate_input():
    print("validating the user info")
```

---

```python id="q4r8ty"
def save_to_db():
    print("saving to database")
```

---

## 🛠️ Main Function

```python id="w2n6cs"
def register_user():
    get_input()
    validate_input()
    save_to_db()
    print("user registration complete")
```

---

## 🛠️ Call

```python id="x8p1hv"
register_user()
```

---

## ▶️ Output

* getting user input
* validating the user info
* saving to database
* user registration complete

---

## 🧠 Notes

* Complexity hide ho gayi
* Sirf function call se kaam ho gaya
* Internal logic visible nahi

---

# 📖 Improving Readability

## 📌 Problem

* Chai shop me bill calculate karna
* Formula baar-baar likhne ki jagah function use karo

---

## 🛠️ Function

```python id="m3q8zl"
def calculate_bill(cups, price_per_cup):
    return cups * price_per_cup
```

---

## 🧠 Important Concept

* `return` → value wapas deta hai
* `print` → sirf output show karta hai

👉 Dono alag concepts hain

---

## 🛠️ Usage

```python id="a9d2vx"
my_bill = calculate_bill(3, 15)
print(my_bill)
```

---

## ▶️ Output

* 45

---

## 🧠 Observation

* Function khud print nahi karta
* Value return hoti hai
* User decide karta hai print karna hai ya nahi

---

## 🛠️ Direct Print

```python id="p7k5bn"
print(calculate_bill(2, 50))
```

---

## 🧠 Notes

* Return value ko variable me store kar sakte hain
* Ya direct print me use kar sakte hain

---

# 🔍 Improving Traceability

## 📌 Concept

* Logic scattered nahi hona chahiye
* Ek jagah change → har jagah reflect

---

## 📌 Problem

* Har order par 10% VAT add karna hai

---

## 🛠️ Function

```python id="c2w9ft"
def add_vat(price, vat_rate):
    return price * (100 + vat_rate) / 100
```

---

## 🛠️ Orders List

```python id="u5r3nx"
orders = [100, 150, 200]
```

---

## 🛠️ Loop

```python id="z6m1ka"
for price in orders:
    final_amount = add_vat(price, 10)
    print(f"original {price}, final with VAT {final_amount}")
```

---

## ▶️ Output

* original 100 → 110
* original 150 → 165
* original 200 → 220

---

## 🧠 Notes

* VAT calculation ek function me defined hai
* Har jagah same logic use ho raha
* Easy to track & update

---

# 📌 Final Summary

* Functions help:

  * hide complexity
  * improve readability
  * improve traceability

* `return` ≠ `print`

* Code modular aur reusable ho jata hai

---

## 📎 Source

Based on transcript 


# 🌍 Scopes in Python (Functions)

---

## 📌 Introduction

* Topic: **Scopes**
* Zyada theory confusing ho sakti hai
* Isliye concept ko **example + code** se samjhaya gaya

---

## 🧠 Concept: Scope kya hota hai?

* Scope decide karta hai:

  * Variable **kahan accessible hai**
* Isko **name resolution** bhi bolte hain

👉 Matlab:

* Same naam ka variable → kaunsa use hoga?

---

## ☕ Example Analogy (Cafe)

* Cafe ka naam: **Global Sip**
* Owner ke paas ek **master notepad**
* Har worker ke paas apna **notepad**

👉 Important:

* Worker ka notepad ≠ master notepad
* Ek jagah change → dusri jagah affect nahi

---

## 🧠 Types of Scope

### 1️⃣ Local Scope

* Function ke andar defined
* Sirf function ke andar accessible

---

### 2️⃣ Enclosing Scope

* Outer function ka scope
* Nested functions me use hota hai

---

### 3️⃣ Global Scope

* Top level (file level)
* Pure program me accessible

---

### 4️⃣ Built-in Scope

* Predefined functions (jaise `print`)

---

# 🔹 Example 1: Local vs Global

## 🛠️ Code

```python id="l1x9pz"
def serve_chai():
    chai_type = "Masala"
    print(f"inside function {chai_type}")

chai_type = "Lemon"

serve_chai()

print(f"outside function {chai_type}")
```

---

## 🧠 Observation

* Inside function → Masala
* Outside function → Lemon

👉 Local variable sirf function ke andar use hota hai

---

## ❗ Case: Global variable remove

* Agar outside variable na ho → error aayega
* Kyunki function ke bahar us variable ka scope nahi

---

# 🔹 Example 2: Enclosing Scope (Nested Functions)

## 🛠️ Code

```python id="n4m2cs"
def chai_counter():
    chai_order = "Lemon"

    def inner_function():
        chai_order = "Ginger"
        print("inner", chai_order)

    inner_function()
    print("outer", chai_order)
```

---

## 🧠 Observation

* Inner → Ginger
* Outer → Lemon

👉 Inner function apna variable use karta hai

---

# 🔹 Example 3: Global Scope

## 🛠️ Code

```python id="g7t1vk"
chai_order = "Tulsi"

chai_counter()

print("global", chai_order)
```

---

## 🧠 Output Flow

* inner → Ginger
* outer → Lemon
* global → Tulsi

---

## 🧠 Important Points

* Same variable name ho sakta hai
* Har scope ka apna version hota hai
* Ek dusre ko affect nahi karte

---

# 🧠 Key Concept

* Local → function ke andar
* Enclosing → outer function
* Global → file level
* Built-in → predefined

---

# 🏠 Final Analogy

* Global = pura ghar
* Functions = alag rooms

👉 Room ke andar jo hota hai → bahar visible nahi
👉 Bahar ka data → andar access ho sakta hai

---

## 📎 Source

Based on transcript 


# 🔄 Nonlocal & Global Keyword (Python)

---

## 📌 Introduction

* Topic: **nonlocal & global**
* Use hota hai jab:

  * Ek function ke andar se
  * Bahar wale variable ko access/update karna ho

---

## 🧠 Concept

👉 Normally:

* Inner function → outer variable access nahi kar pata (update nahi kar pata)

👉 Solution:

* `nonlocal`
* `global`

---

# 🔹 Nonlocal Keyword

## 📌 Purpose

* Inner function se **outer function ke variable ko access/update** karna

---

## 🛠️ Example

```python id="n1k4xp"
def update_order():
    chai_type = "Elaichi"

    def kitchen():
        nonlocal chai_type
        chai_type = "Kesar"

    kitchen()
    print("after kitchen update", chai_type)
```

---

## 🧠 Observation

* Pehle → Elaichi
* Kitchen ke baad → Kesar

👉 Value update ho gayi outer function me

---

## ❗ Without nonlocal

* Agar `nonlocal` hata diya:

  * Inner function new variable bana lega
  * Outer wala change nahi hoga

👉 Output → Elaichi hi rahega

---

## 🧠 Key Point

* `nonlocal` → **just outer function tak hi access deta hai**
* Global ko access nahi karta

---

# 🔹 Global Keyword

## 📌 Purpose

* Kisi bhi function ke andar se **global variable access/update** karna

---

## 🛠️ Example

```python id="g2v8rt"
chai_type = "Plain"

def front_desk():
    def kitchen():
        global chai_type
        chai_type = "Irani"

    kitchen()

front_desk()

print("final global chai", chai_type)
```

---

## 🧠 Observation

* Global value change ho gayi
* Plain → Irani

---

## ❗ Important

* `global` → pure file level variable access karta hai
* Kahin se bhi use ho sakta hai

---

# 🔁 Nonlocal vs Global

| Keyword  | Scope          |
| -------- | -------------- |
| nonlocal | outer function |
| global   | file level     |

---

## ❗ Error Case

* Agar `nonlocal` use kiya global variable ke liye → error
* Kyunki wo sirf outer function me search karta hai

---

# ⚠️ Caution with Global

## 📌 Problem

* Multiple functions same global variable use karte hain
* Har koi usse change kar sakta hai

👉 Result:

* Code break ho sakta hai

---

## 🧠 Example Idea

* Function A → expect karta hai value = True
* Function B → value change kar deta hai = "ginger"

👉 Function A ka logic fail

---

## 📌 Conclusion

* Global use karo:

  * **carefully**
  * **rare cases me**

---

## 🧠 Final Points

* nonlocal → outer function ke liye
* global → pure program ke liye
* Global dangerous ho sakta hai agar misuse ho

---

## 📎 Source

Based on transcript 


# 📥 Function Parameters & Arguments (Python)

---

## 📌 Introduction

* Function me jo values pass hoti hain → **parameters**
* Function call ke time jo actual values dete hain → **arguments**

---

## 🧠 Basic Idea

* Function ek **mysterious box** jaisa hai
* Andar jo pass karoge → uske basis par output milega

---

## 🛠️ Example 1: Simple Function

```python id="a1v9kx"
chai = "ginger chai"

def prepare_chai(order):
    print("preparing", order)

prepare_chai(chai)
```

---

## 🧠 Observation

* String pass kiya
* Function ne sirf read kiya
* Original value change nahi hui

---

## ❗ Important

* Strings change nahi hote (immutable)
* Function sirf value read karta hai

---

# 🔁 Mutable vs Immutable

---

## 🛠️ Example 2: List (Mutable)

```python id="b4q8zp"
chai = [1, 2, 3]

def edit_chai(cups):
    cups[1] = 42

edit_chai(chai)
print(chai)
```

---

## 🧠 Observation

* Output → [1, 42, 3]
* Original list change ho gayi

---

## 📌 Conclusion

* List → mutable → change ho jati hai
* String → immutable → change nahi hoti

---

# 📌 Parameters vs Arguments

* Function define karte time → **parameter**
* Function call karte time → **argument**

---

# 🔁 Positional Arguments

## 🛠️ Example

```python id="c7m2rt"
def make_chai(tea, milk, sugar):
    print(tea, milk, sugar)

make_chai("Darjeeling", "yes", "low")
```

---

## 🧠 Concept

* Order matter karta hai
* Value position ke basis par assign hoti hai

---

# 🔁 Keyword Arguments

## 🛠️ Example

```python id="k9p3vx"
make_chai(tea="green", sugar="medium", milk="no")
```

---

## 🧠 Concept

* Order matter nahi karta
* Direct naam ke basis par assign hota hai

---

# 🔁 *args and **kwargs

---

## 🛠️ Example

```python id="m5z8qn"
def special_chai(*ingredients, **extras):
    print(ingredients)
    print(extras)
```

---

## 🛠️ Call

```python id="y2w6bx"
special_chai("cinnamon", "cardamom", sweetener="honey", foam="yes")
```

---

## 🧠 Observation

* `*ingredients` → tuple
* `**extras` → dictionary

---

## 📌 Concept

* Without name → args (tuple)
* With name → kwargs (key-value / dictionary)

---

# ⚠️ Default Parameter Trap

---

## 🛠️ Problem Code

```python id="t8n4pl"
def chai_order(order=[]):
    order.append("masala")
    print(order)

chai_order()
chai_order()
```

---

## 🧠 Observation

* Output → ["masala", "masala"]
* Same list reuse ho rahi hai

---

## ❗ Problem

* Default empty list mutable hai
* Har call me same list modify ho rahi hai

---

# ✅ Solution

```python id="r3k9fs"
def chai_order(order=None):
    if order is None:
        order = []
    print(order)
```

---

## 🧠 Concept

* Default value → `None`
* Har call me new list create hogi

---

## 📌 Notes

* Mutable default avoid karo
* None use karna safe hota hai

---

## 📎 Source

Based on transcript 


# 🔙 Return Keyword in Python

---

## 📌 Introduction

* `return` ek important keyword hai
* Function me use hota hai value **wapas dene ke liye**
* Ye print nahi karta → value return karta hai

---

## 🧠 Basic Concept

```python
def make_chai():
    return "hitesh"
```

👉 Iska matlab:

* Function ek value return karega
* Ye print nahi karega

---

## ☕ Analogy

* Chai banayi → but customer ko diya nahi
* Toh kaam ka fayda nahi

👉 Same:

* `return` → value ko bahar deta hai

---

# 🛠️ Example 1: Simple Return

```python id="a2k8mz"
def make_chai():
    return "here is your masala chai"
```

---

## 🛠️ Usage

```python id="p5d9xy"
print(make_chai())
```

---

## 🧠 Alternative

```python id="x3n7vt"
result = make_chai()
print(result)
```

---

## 🧠 Concept

* Function execute hota hai
* Jo return hota hai → variable me store hota hai

---

# ❗ Print vs Return

---

## 🛠️ Example

```python id="b7q2lp"
def make_chai():
    print("here is your masala chai")
```

---

## 🧠 Observation

* Function print karta hai
* But return nahi karta

👉 Is case me:

* Return value = `None`

---

# 🔁 Important Rule

* Agar kuch return nahi kiya → default return = `None`
* Isko bolte hain:

👉 **implicitly returns None**

---

# 🛠️ Example: No Return

```python id="k4m8rt"
def chaiwala():
    pass

print(chaiwala())
```

---

## 🧠 Output

* None

---

# 🔢 Return Single Value

## 🛠️ Example

```python id="n9p3vx"
def sold_cups():
    return 120
```

---

## 🛠️ Usage

```python id="c2w6bx"
total = sold_cups()
print(total)
```

---

## 🧠 Output

* 120

---

# ⚡ Early Return

---

## 🛠️ Example

```python id="y8z4qn"
def chai_status(cups_left):
    if cups_left == 0:
        return "sorry chai over"
    return "chai is ready"
```

---

## 🛠️ Usage

```python id="m1k5fs"
print(chai_status(0))
print(chai_status(5))
```

---

## 🧠 Concept

* Jaise hi `return` hit hua → function stop
* Baaki code execute nahi hota

---

## ❗ Important

* Return ke baad ka code kabhi run nahi hota

---

# 🔁 Multiple Return Values

---

## 🛠️ Example

```python id="t6r2pl"
def chai_report():
    return 120, 30
```

---

## 🛠️ Usage

```python id="r3k9fs"
sold, remaining = chai_report()
```

---

## 🧠 Concept

* Multiple values return ho sakti hain
* Unpack karke variables me store karte hain

---

# ⚠️ Extra Values Case

* Agar function 3 values return kare
* Aur aap 2 variables use karo → error

---

## 🛠️ Handle using `_`

```python id="q1w7dv"
sold, remaining, _ = chai_report()
```

---

## 🧠 Concept

* `_` → value ignore karne ke liye use hota hai

---

# 📌 Important Points

* `return` value deta hai
* `print` sirf output show karta hai
* Default return = None
* Function ek ya multiple values return kar sakta hai
* Return ke baad code execute nahi hota

---

## 📎 Source

Based on transcript 


# ⚙️ Types of Functions in Python

---

## 📌 Introduction

* Functions Python me **large scale projects ka core** hain
* Different types hote hain functions ke
* Ye strict types nahi hain, but understanding ke liye use hote hain

---

# 🔹 Types of Functions

* Pure vs Impure Functions
* Recursive Functions
* Anonymous Functions (Lambdas)

---

# 🔁 Pure vs Impure Functions

---

## 🧠 Pure Function

```python id="p1x9mz"
def pure_chai(cups):
    return cups * 10
```

---

## 🧠 Concept

* Sirf input pe depend karta hai
* Global variable ko change nahi karta

---

## 🛠️ Example Global

```python id="g4k8zp"
totalchai = 0
```

👉 Pure function is value ko touch nahi karta

---

## 🧠 Key Point

* No global manipulation
* Safe & predictable

---

# 🔁 Impure Function

---

## 🛠️ Example

```python id="i7q2lp"
def impure_chai(cups):
    global totalchai
    totalchai += cups
```

---

## 🧠 Concept

* Global variable ko modify karta hai
* Side effects create karta hai

---

## ❗ Important

* **Not recommended**
* Avoid karna chahiye

---

# 🔁 Recursive Functions

---

## 📌 Concept

* Function khud ko call karta hai
* Base condition hona zaroori hai

---

## 🛠️ Example

```python id="r3n8vx"
def pour_chai(n):
    if n == 0:
        return "all cups poured"
    return pour_chai(n - 1)
```

---

## 🧠 Flow (n = 3)

* 3 → 2 → 1 → 0
* Jab 0 → return

---

## 🧠 Important

* Base condition zaroori hai
* Infinite recursion avoid hota hai
* Complex problems me use hota hai

---

# 🔁 Anonymous Functions (Lambda)

---

## 📌 Concept

* Function without name
* One-time use
* `lambda` keyword se banta hai

---

## 🛠️ Example Setup

```python id="l2m7zt"
chai_types = ["light", "kadak", "ginger", "kadak"]
```

---

## 🛠️ Filter using Lambda

```python id="k8p3vx"
strong_chai = list(filter(lambda chai: chai == "kadak", chai_types))
```

---

## 🧠 Concept

* Lambda ek short function hai
* Condition check karta hai
* Filter sirf true values return karta hai

---

## ▶️ Output

* ["kadak", "kadak"]

---

## 🔁 Reverse Condition

```python id="m5z8qn"
strong_chai = list(filter(lambda chai: chai != "kadak", chai_types))
```

---

## ▶️ Output

* ["light", "ginger"]

---

## 🧠 Important Points

* Lambda = no name function
* filter = condition apply karta hai
* Sirf true values list me aati hain

---

## 📌 Notes

* Lambda use-and-throw type function hai
* Mostly ek baar ke use ke liye
* Simple logic ke liye useful

---

## 📎 Source

Based on transcript 


# ⚙️ Built-in Functions & Docstrings in Python

---

## 📌 Introduction

* Python me bohot saari cheezein **built-in hoti hain**
* Hume khud se likhne ki zarurat nahi hoti
* Python interpreter me already available hoti hain

👉 Ye sab **built-in functions & types** hote hain

---

## 🧠 Built-in Functions

* Python me bohot saare functions already defined hote hain
* Ye alphabetical order me documentation me listed hote hain

👉 Example:

* len
* filter
* zip
* type
* min / max

---

## 📌 Important Point

* Sab functions yaad nahi hote
* Hum unhe **jab zarurat ho tab use karte hain**

---

# 🔧 Function Example with Default Parameter

```python id="p4k8mz"
def chai_flavor(flavor="masala"):
    return flavor
```

---

## 🧠 Concept

* Default parameter diya gaya hai
* Agar user value na de → default use hoga

---

# 📖 Docstring (Triple Quotes)

---

## 🛠️ Example

```python id="a7n2vx"
def chai_flavor(flavor="masala"):
    """return the flavor of chai"""
    return flavor
```

---

## 🧠 Concept

* Triple quotes (`""" """`) use hote hain
* Function ke description ke liye
* Isko **docstring** bolte hain

---

## ❗ Important Rule

* Docstring **first line me hona chahiye**
* Agar pehle kuch aur likh diya → kaam nahi karega

---

# 🔍 Dunder Methods

---

## 📌 Concept

* Double underscore wale methods → **dunder methods**
* Example:

  * `__doc__`
  * `__name__`

---

## 🛠️ Example

```python id="k9p3vx"
print(chai_flavor.__doc__)
```

👉 Docstring print ho jayega

---

```python id="m5z8qn"
print(chai_flavor.__name__)
```

👉 Function ka naam print hoga

---

## 🧠 Meaning

* `__doc__` → documentation
* `__name__` → function name

---

# 🔁 Help Function

---

## 🛠️ Example

```python id="r2t6pl"
help(len)
```

---

## 🧠 Concept

* Kisi bhi function ke baare me info deta hai
* Documentation show karta hai

---

## ❗ Note

* Output thoda complex hota hai
* Exit karne ke liye → `q` press karo

---

# 📚 Documentation

* Best way → Python documentation use karo
* Built-in functions list waha milti hai

---

# 🧾 Writing Good Functions

---

## 📌 Suggestion

* Agar function bada hai → documentation likho
* Dusre log use karenge → samajhna easy hoga

---

# 🛠️ Example: Proper Documented Function

```python id="t6r2pl"
def generate_bill(chai=0, samosa=0):
    """
    calculate the total bill for chai and samosa

    param chai: number of chai cups (10 rupees each)
    param samosa: number of samosa (15 rupees each)

    returns total amount and thank you message
    """
    total = chai * 10 + samosa * 15
    return total, "thank you for visiting chaicode.com"
```

---

## 🧠 Concept

* Triple quotes me:

  * Description
  * Parameters
  * Return value

---

## 📌 Notes

* Documentation likhna good practice hai
* Especially jab code production level ka ho
* Dusre developers ke liye helpful hota hai

---

## 📎 Source

Based on transcript 


# 📦 Importing in Python (Modules & Objects)

---

## 📌 Introduction

* Python me ek important concept hai → **importing**
* Dusre files se code use karna
* Guesswork nahi hona chahiye → proper understanding zaroori hai

---

## 🧠 Concept

* Python me sab kuch **object** hota hai
* Functions bhi object hi hote hain
* Isliye importing objects = importing functions

---

# ☕ Analogy

* Ek file me masala chai recipe likhi hai → `masalachai.py`
* Dusri file → `newbranch.py`

👉 Har baar code likhne ki jagah:

* Us file ko **import kar lo**

---

# 🔁 Method 1: Full Import

## 🛠️ Code

```python id="a1k9mz"
import masalachai
```

---

## 🛠️ Usage

```python id="p4d8xy"
masalachai.brew()
```

---

## 🧠 Concept

* Puri file import hoti hai
* Dot (`.`) se methods access karte hain

---

# 🔁 Method 2: Specific Import

## 🛠️ Code

```python id="k7m2vx"
from masalachai import brew
```

---

## 🛠️ Usage

```python id="n5q3rt"
brew()
```

---

## 🧠 Concept

* Sirf required function import hota hai
* Direct use kar sakte hain

---

# 🔁 Method 3: Alias Import

## 🛠️ Code

```python id="z2p8qn"
from masalachai import brew as start_brewing
```

---

## 🛠️ Usage

```python id="x6w1fs"
start_brewing()
```

---

## 🧠 Concept

* Function ka naam change kar sakte hain
* Useful jab naming conflict ho

---

# 📦 Multiple Imports

```python id="m3t9pl"
from masalachai import brew, prepare
```

---

## 🧠 Concept

* Ek se zyada functions import kar sakte hain

---

# 🔁 Built-in Imports

---

## 🛠️ Example

```python id="r2k6dv"
from datetime import datetime
```

---

## 🛠️ Example

```python id="y8p4qs"
from requests import get
```

---

## 🧠 Concept

* Python libraries se bhi import kar sakte hain

---

# 📂 Folder Structure Import

---

## 📌 Structure

* chai_business/

  * main.py
  * recipes/

    * flavor.py
  * utils/

    * discounts.py

---

## 🛠️ Import

```python id="c1w7bx"
import recipes.flavor
```

---

## 🛠️ Usage

```python id="v9k2mz"
recipes.flavor.elaichi_chai()
```

---

## 🧠 Concept

* Folder name + file name use hota hai
* `.py` likhne ki zarurat nahi

---

# 🔁 Named Import from Folder

```python id="t5n3qs"
from recipes.flavor import ginger_chai
```

---

## 🧠 Concept

* Direct function use kar sakte hain

---

# 🔁 Relative Import

---

## 🛠️ Example

```python id="b8p4vx"
from .recipes import flavor
```

---

## 🛠️ Example

```python id="m6z1rt"
from ..recipes import flavor
```

---

## 🧠 Concept

* `.` → current directory
* `..` → one level up

---

# ⚠️ Avoid This

```python id="q3w9pl"
from masalachai import *
```

---

## 🧠 Reason

* Sab kuch import ho jata hai
* Control nahi rehta
* Bugs aa sakte hain

---

# 📦 **init**.py (Dunder Init)

---

## 📌 Concept

* File: `__init__.py`
* Folder ko Python package banata hai

---

## 🧠 Important

* Python 3.3+ me required nahi hai
* Phir bhi log use karte hain

---

## 📌 Notes

* Usually empty file hoti hai
* Internal Python structure ke liye

---

# 📌 Key Points

* Import ke multiple ways hain
* Full import vs specific import
* Alias use kar sakte hain
* Relative import possible hai
* `*` import avoid karo
* `__init__.py` optional hai (Python 3.3+)

---

## 📎 Source

Based on transcript 
