# Python Loops — Lecture Notes (Hinglish)

## Loop Kya Hota Hai?
Loop ka matlab hai ek kaam ko **baar baar karna**. Conditionals (if/else) mein hum left ya right jaate the kisi condition ke basis pe, lekin loop mein hum **ek hi logic ko multiple baar repeat** karte hain.

## Loop Ki Zaroorat Kyun Hai?
Kabhi kabhi ek task ko 10 baar, 5 baar, ya pata nahi kitni baar karna padta hai. Ek real-world example:
- Tumne ek backend se web request ki aur **5 books** ka data aaya display karne ke liye.
- Ab baar baar same code likhne ki jagah, hum loop lagaate hain aur ek ek book display karte jaate hain.

> **Yaad rakho:** Programming mein counting **0 se** shuru hoti hai, 1 se nahi. Toh pehla item index `0` pe hoga, doosra `1` pe, aur aage bhi aise hi.

---

## Kaun Kaun Se Loops Hain?

| Loop | Kab Use Karein |
|------|----------------|
| `for` loop | Jab sequence ya range pata ho |
| `while` loop | Jab condition true ho tab tak repeat karna ho |

---

## Important Concepts

### `range()`
- Numbers ka ek sequence generate karta hai start se end tak.
- **Range mein end value kabhi include nahi hoti — yeh rule yaad rakhna!**
  - Example: `range(1, 11)` → `1` se `10` tak ke numbers milenge (`11` nahi).
- Yeh rule poore Python mein apply hota hai — strings, numbers, ranges — **end hamesha exclusive hota hai**.

### Sequence Producers
Yeh functions sequences banate hain jinhe hum loop kar sakte hain:
- `range` — numbers ka sequence deta hai
- `enumerate` — index aur value dono saath deta hai
- `zip` — do sequences ko combine karta hai

### Loop Control (Loop Ko Beech Mein Rokna)
Loop ke andar kuch conditions pe hum uska flow control kar sakte hain:
- **`break`** — poora loop band kar do jab condition meet ho jaye
- **`continue`** — current iteration skip karo, agle pe jaao

---

## `for` vs `while` Loop — Kab Kya Use Karein?
Dono loops ka kaam same lagta hai, lekin fark hai:
- **`for`** use karo jab iterations ki count pata ho (jaise list ke upar loop karna).
- **`while`** use karo jab pata na ho kitni baar loop chalega (jaise user input ka wait karna).

---

## Summary
- Loops se hum tasks efficiently repeat kar sakte hain — baar baar same code likhne ki zaroorat nahi.
- Python mein `for` aur `while` — yeh do main loops hain.
- `range()` bahut common hai, aur iska **end value hamesha exclusive** hota hai.
- `break` aur `continue` se loop ko control kar sakte hain beech mein.
- Practice karo — loops thoda zyada practice maangta hai conditionals se!

# Python For Loop — Examples (Hinglish Notes)

## Problem Statement: Tea Stall Token Dispenser 🍵
Ek chai stall ke owner ke paas ek **digital token display** hai.  
Har customer ke liye ek token number print hoga aur chai serve hogi.

**Task:** `for` loop aur `range` use karke **1 se 10 tak** token numbers generate karo aur print karo:
```
Serving chai to token #1
Serving chai to token #2
...
Serving chai to token #10
```

---

## For Loop Ka Syntax

```python
for token in range(1, 11):
    print(f"Serving chai to token #{token}")
```

### Line by Line Samjho:

| Part | Matlab |
|------|--------|
| `for` | Loop shuru karne ka keyword |
| `token` | Variable — har iteration mein current number store hoga |
| `in` | Keyword jo batata hai kahan se loop karna hai |
| `range(1, 11)` | 1 se 10 tak numbers generate karo (11 exclusive hai) |
| `:` | Colon lagao, phir enter — indentation automatic aayega |
| `print(...)` | Indented block = loop ka kaam |

> **Yaad rakho:** Variable ka naam kuch bhi ho sakta hai — `token`, `i`, `chai`, `index` — koi bhi chalega. Range wala number hi isme aata hai.

---

## Loop Kaise Kaam Karta Hai — Step by Step

```
range(1, 11) produce karta hai → [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]

Iteration 1 → token = 1 → "Serving chai to token #1"
Iteration 2 → token = 2 → "Serving chai to token #2"
Iteration 3 → token = 3 → "Serving chai to token #3"
...
Iteration 10 → token = 10 → "Serving chai to token #10"
11 aaya → range khatam → loop band ✅
```

---

## Common Mistake — F-String Bhool Gaye!

```python
# ❌ Galat — "token" literally print hoga, variable ki value nahi
print("Serving chai to token #token")

# ✅ Sahi — f-string lagao taaki variable ki value print ho
print(f"Serving chai to token #{token}")
```

> **Tip:** Agar output mein variable ka naam word ki tarah aa raha ho (value nahi), toh samjho `f` bhool gaye ho string ke pehle!

---

## Key Takeaways
- `for` loop hamesha **`for` keyword** se shuru hota hai.
- `range(start, stop)` mein **stop value kabhi include nahi hoti**.
- Loop ke andar ka code **indented** hona chahiye (4 spaces ya 1 tab).
- Loop variable ka naam **apni marzi se** rakho — koi rule nahi.
- Mistakes hoti hain — **panic mat karo**, bas fix karo! 😄

---

## Example 2: Chai Batch Simulator 🫖

### Problem Statement
Ek chai shop har 15 minute mein ek batch banati hai.  
**4 batches simulate karo** aur har batch ka number print karo.

```
Preparing chai for batch #1
Preparing chai for batch #2
Preparing chai for batch #3
Preparing chai for batch #4
```

### Code

```python
for batch in range(1, 5):
    print(f"Preparing chai for batch #{batch}")
```

### Range Ke Do Tarike

| Tarika | Example | Output |
|--------|---------|--------|
| Sirf end value | `range(4)` | 0, 1, 2, 3 |
| Start aur end dono | `range(1, 5)` | 1, 2, 3, 4 |

> **Tip:** Agar counting 1 se karni ho toh `range(1, n+1)` likho.  
> Agar 0 se karna ho toh sirf `range(n)` kaafi hai.

### Key Points
- Variable ka naam `batch` rakha — clearly samajh aata hai kya store ho raha hai.
- `range(1, 5)` diya kyunki 4 batches chahiye thi, 1 se start karke.
- Loop ke andar sirf ek print statement — lekin chahe 100 lines bhi ho sakti hain!
- **Variable ki value automatically badhti hai** — humein manually kuch nahi karna. 😄

---

## Example 3: Chai Order Queue 📋

### Problem Statement
Tumhare paas customers ke names ki ek list hai.  
Har naam ke liye print karo: `Order ready for <naam>`

### Code

```python
orders = ["Hitesh", "Aman", "Becky", "Carlos"]

for name in orders:
    print(f"Order ready for {name}")
```

### Output
```
Order ready for Hitesh
Order ready for Aman
Order ready for Becky
Order ready for Carlos
```

### Nayi Cheez: List Pe Loop Karna

Ab tak hum `range()` pe loop kar rahe the — ab directly **list** pe loop kar sakte hain!

| | Range wala | List wala |
|--|-----------|-----------|
| **Loop kya karta hai** | Numbers generate karta hai | List ke items ek ek deta hai |
| **Example** | `for i in range(1, 5)` | `for name in orders` |
| **Kab use karein** | Jab numbers chahiye ho | Jab data already list mein ho |

### Important Concept: Iterable
> **Iterable** = koi bhi cheez jiske upar loop chal sake.

Python mein bahut saari cheezein iterable hoti hain:
- `range()` ✅
- List `[]` ✅
- String `""` ✅ (aur bhi hain — aage seekhenge!)

### Key Point
- List mein **kitne bhi items** ho sakte hain — 4 ho, 400 ho, ya 0 — loop apne aap handle kar leta hai.
- Humein count jaanna zaroori nahi! Loop khud jaanta hai kab rukna hai. 😄

# 🍵 Tea Menu using Enumerate (Python)

## 📌 Problem Statement

Ek **tea menu board** banana hai jisme:

👉 Har item **numbered hona chahiye**

### Task:

* `enumerate` use karke menu ko numbers ke saath print karo

---

## 🧠 Problem Understanding

* Humare paas ek **list of items** hai (tea menu)
* Normal loop se items print ho jaate hain
* ❌ But numbering nahi aati automatically

---

## 🛠️ Step 1: Menu List banana

```python id="jv1g2k"
menu = ["green tea", "lemon tea", "spiced tea", "mint tea"]
```

---

## 🛠️ Step 2: Simple for loop

```python id="s8q1az"
for item in menu:
    print(f"menu item is {item}")
```

👉 Ye kaam karta hai
❌ But numbering nahi milti

---

## ❗ Problem

* List me index hote hain (0,1,2,3)
* But unko directly print nahi kar pa rahe

👉 Isi problem ke liye use hota hai:

### ✔ `enumerate`

---

## 🧠 Enumerate kya karta hai

* Har item ko **automatic number assign karta hai**
* Output me **(index, value)** pair deta hai

Example:

* ("spring", 0)
* ("summer", 1)

---

## ⚙️ Default Behavior

* Index **0 se start hota hai**

---

## ⚙️ Custom Start

```python id="m9r3xs"
enumerate(menu, start=1)
```

👉 Index ab **1 se start hoga**

---

## 🛠️ Step 3: Enumerate with loop

```python id="a7p2mv"
for idx, item in enumerate(menu, start=1):
    print(f"{idx}. {item} chai")
```

---

## 🧠 Important Point

* enumerate **tuple return karta hai**
* Isliye humne 2 variables liye:

  * `idx` → index
  * `item` → value

---

## ▶️ Output

* 1 green tea chai
* 2 lemon tea chai
* 3 spiced tea chai
* 4 mint tea chai

---

## 📌 Notes

* enumerate ek powerful tool hai
* iterator/generator jaisa behavior bhi hota hai (later study hoga)
* next(), yield etc. future me cover hoga

---

## 📎 Source

Based on transcript 


# 🧾 Order Summary using zip (Python)

## 📌 Problem Statement

Ek **order summary** banana hai jisme:

👉 Customer ka naam + uska bill amount show ho

### Task:

* Do lists use karo:

  * ek **names**
  * ek **bills**

---

## 🛠️ Step 1: Lists banana

```python id="c8k2la"
names = ["Hitesh", "Meera", "Sam", "Ali"]
```

```python id="q1v8mx"
bills = [50, 70, 100, 55]
```

👉 Dono lists me same number of elements hone chahiye

---

## 🎯 Goal

Print karna hai:

* name + "paid" + amount + "rupees"

---

## ❗ Problem

* Dono lists ko ek saath iterate karna hai
* Simple loop se ye difficult ho jata hai

👉 Iske liye use hota hai:

### ✔ `zip`

---

## 🧠 zip kya karta hai

* Multiple lists ko **parallel iterate** karta hai
* Har step pe **tuple return karta hai**

Example:

* (item1, item2)

---

## 🛠️ Step 2: zip use karna

```python id="y8pz3v"
for name, amount in zip(names, bills):
```

👉 Yaha:

* `name` → names list se
* `amount` → bills list se

---

## 🛠️ Step 3: Print statement

```python id="2t4kfj"
print(f"{name} paid {amount} rupees")
```

---

## ▶️ Complete Code

```python id="o3q1vl"
names = ["Hitesh", "Meera", "Sam", "Ali"]
bills = [50, 70, 100, 55]

for name, amount in zip(names, bills):
    print(f"{name} paid {amount} rupees")
```

---

## ▶️ Output

* Hitesh paid 50 rupees
* Meera paid 70 rupees
* Sam paid 100 rupees
* Ali paid 55 rupees

---

## 🧠 Important Points

* zip ek function hai jo multiple lists leta hai
* Har iteration me tuple return karta hai
* Isliye humne 2 variables use kiye (name, amount)

---

## 📌 Notes

* enumerate ka concept pehle use hua tha
* uske upar zip ka concept add hua
* knowledge ek dusre pe build hota hai

---

## 📎 Source

Based on transcript 


# 🌡️ Tea Heating Simulation using While Loop

## 📌 Problem Statement

Tea heating simulate karna hai:

* Start temperature = **40°C**
* Boiling point = **100°C**

### Task:

* `while loop` use karo
* Har step me temperature **+15** increase karo
* Jab tak temperature **100 tak ya usse exceed** na kare
* Har step pe temperature print karo
* End me message print karo

---

## 🛠️ Step 1: Variable banana

```python id="g4p2zs"
temperature = 40
```

---

## 🛠️ Step 2: While Loop

```python id="w1n9kc"
while temperature < 100:
```

👉 Loop tab tak chalega jab tak condition **true** hai
👉 Jab condition false hogi → loop ruk jayega

---

## 🛠️ Step 3: Current temperature print karna

```python id="k9xv2m"
print("current temperature is", temperature)
```

---

## 🛠️ Step 4: Temperature increase karna

```python id="m7r5dz"
temperature = temperature + 15
```

👉 Short form:

```python id="p3h1bx"
temperature += 15
```

👉 Dono same kaam karte hain

---

## 🛠️ Step 5: Final message

```python id="z8q4nt"
print("Tea is ready to be served")
```

---

## ▶️ Complete Code

```python id="x2c7lm"
temperature = 40

while temperature < 100:
    print("current temperature is", temperature)
    temperature += 15

print("Tea is ready to be served")
```

---

## ▶️ Output Flow

* 40
* 55
* 70
* 85
* phir loop stop → message print

---

## 🔄 Important Observation

* Agar print pehle likha → current value print hoti hai
* Agar increase pehle karo → updated value print hoti hai

👉 Execution order important hai

---

## 🧠 While Loop Concept

* Condition check karta rehta hai
* Jab tak condition true → loop chalta rahega
* False hote hi loop stop

---

## 📌 Notes

* for loop → list iterate karne ke liye use hota hai
* while loop → condition based execution ke liye
* indentation important hai

---

## 📎 Source

Based on transcript 


# 🔁 Continue, Break & For-Else (Python)

## 📌 Problem Statement

Chai flavors ka system hai:

* Kuch flavors **out of stock** hain → skip karo
* Kuch flavors **discontinued** hain → loop stop karo

### Task:

* out of stock → `continue`
* discontinued → `break`

---

## 🧠 Concepts

### 🔹 continue (skip)

* Current iteration skip karta hai
* Loop next iteration pe chala jata hai

---

### 🔹 break

* Poora loop turant stop kar deta hai

---

## 🛠️ Step 1: Flavors list

```python id="q1f9lz"
flavors = ["ginger", "out of stock", "lemon", "discontinued", "tulsi"]
```

---

## 🛠️ Step 2: Loop

```python id="h3m8ks"
for flavor in flavors:
```

---

## 🛠️ Step 3: Conditions

### Skip (continue)

```python id="b9r4vx"
if flavor == "out of stock":
    continue
```

---

### Stop (break)

```python id="z2k6np"
if flavor == "discontinued":
    break
```

---

## 🛠️ Step 4: Print

```python id="x7p1dw"
print(flavor, "item found")
```

---

## 🛠️ Step 5: Outside loop

```python id="c6y2qs"
print("outside of loop")
```

---

## ▶️ Complete Code

```python id="m4w8pl"
flavors = ["ginger", "out of stock", "lemon", "discontinued", "tulsi"]

for flavor in flavors:
    if flavor == "out of stock":
        continue
    if flavor == "discontinued":
        break
    print(flavor, "item found")

print("outside of loop")
```

---

## ▶️ Flow

* ginger → print
* out of stock → skip (no print)
* lemon → print
* discontinued → break (loop stop)
* tulsi → kabhi execute nahi hota

---

## 🧠 Important Points

* continue → sirf ek iteration skip
* break → pura loop stop
* indentation important hai

---

# 🔁 For-Else Concept

## 📌 Example Setup

```python id="n8t3xv"
staff = [("Amit", 16), ("Zara", 17), ("Raj", 15)]
```

---

## 🛠️ Loop with condition

```python id="y5u2km"
for name, age in staff:
    if age >= 18:
        print(f"{name} is eligible")
        break
```

---

## 🛠️ Else block

```python id="v9q1wr"
else:
    print("No one is eligible")
```

---

## ▶️ Complete Code

```python id="d2k8fs"
staff = [("Amit", 16), ("Zara", 17), ("Raj", 15)]

for name, age in staff:
    if age >= 18:
        print(f"{name} is eligible")
        break
else:
    print("No one is eligible")
```

---

## ▶️ Behavior

* Agar koi bhi condition match nahi kare → else chalega
* Agar break execute ho gaya → else nahi chalega

---

## 🧠 Important Point

👉 `else` yaha **if ka part nahi hai**
👉 Ye **for loop ka part hai**

---

## 📌 Rule

* loop complete hua (no break) → else run
* loop break hua → else skip

---

## 📎 Source

Based on transcript 


# 🐘 Walrus Operator (:=) in Python

## 📌 Introduction

* Ye topic loops ka part nahi hai
* Standalone concept hai
* Python me kaafi time se hai (Python 3.8 se)

---

## 🧠 Basic Concept

### 🔹 Statement vs Expression

```python id="s1xk2p"
x = 5
```

👉 Ye **statement** hai
👉 Value assign karta hai
👉 Return kuch nahi karta

---

```python id="v8d3ql"
3 + 3
```

👉 Ye **expression** hai
👉 Value return karta hai (6)

---

## 🧠 Walrus Operator

* Syntax: `:=`
* Assignment + expression ek saath

---

## 🛠️ Without Walrus

```python id="m3a8xj"
value = 13
remainder = value % 5

if remainder:
    print(f"not divisible, remainder is {remainder}")
```

---

## 🛠️ With Walrus

```python id="k9z2wr"
value = 13

if (remainder := value % 5):
    print(f"not divisible, remainder is {remainder}")
```

---

## 🔍 Observation

* Pehle:

  * value calculate
  * variable me store
  * fir check

* Ab:

  * ek hi line me assignment + check

---

## ⚠️ Without Walrus Error

* Direct assignment inside condition allowed nahi hai
* Error aata hai (syntax / undefined variable)

---

## 📚 Definition

👉 Walrus operator:

* Expression ke andar hi value assign karta hai
* Variable ko value bhi milti hai + evaluate bhi hota hai

---

# 🍵 Example: Chai Size Check

## 🛠️ Code

```python id="n2b7ty"
available_sizes = ["small", "medium", "large"]

if (request_size := input("Enter your chai cup size: ")) in available_sizes:
    print(f"serving {request_size} chai")
else:
    print(f"size is unavailable {request_size}")
```

---

## ▶️ Behavior

* Input bhi wahi pe liya
* Check bhi wahi pe hua
* Agar match → serve
* nahi → unavailable

---

# 🔁 Example: Loop + Walrus

## 🛠️ Flavors

```python id="h4k8mv"
flavors = ["masala", "ginger", "lemon", "mint"]
```

---

## 🛠️ Code

```python id="y7p1qs"
print("available flavors:", flavors)

while (flavor := input("choose your flavor: ")) not in flavors:
    print(f"sorry {flavor} is not available")

print(f"you chose {flavor} chai")
```

---

## ▶️ Flow

* User se input lo
* Agar flavor list me nahi → loop chalta rahega
* Jab valid input mile → loop stop
* final print

---

## 🧠 Important Points

* Walrus operator code ko short banata hai
* Assignment + check ek hi line me
* Har jagah use nahi hota
* Thoda confusing ho sakta hai

---

## 📌 Notes

* Ye alternative way hai code likhne ka
* Input separate line me bhi le sakte the
* Walrus se direct condition me le liya

---

## 📎 Source

Based on transcript 


# 📊 Dictionary Based Discount System (Python)

## 📌 Concept

* Ye koi new topic nahi hai
* Ye **code likhne ka ek style** hai
* Industry level / production code me use hota hai

👉 Instead of:

* if-else
* match-case

👉 Use:

* **dictionary mapping**

---

## 🛠️ Step 1: Users Data

```python id="u1p8dx"
users = [
    {"id": 1, "total": 100, "coupon": "P20"},
    {"id": 2, "total": 150, "coupon": "F10"},
    {"id": 3, "total": 80, "coupon": "P50"}
]
```

---

## 🧠 Problem

* Har user ke paas:

  * total amount
  * coupon code

👉 Hume pata nahi:

* P20 kya karta hai
* F10 kya karta hai

---

## 🛠️ Step 2: Discount Mapping (Dictionary)

```python id="v4k9qz"
discounts = {
    "P20": (0.2, 0),
    "F10": (0.5, 0),
    "P50": (0, 10)
}
```

---

## 🧠 Meaning

* Tuple = `(percent, fixed)`
* Example:

  * P20 → 20% discount
  * F10 → 50% discount
  * P50 → flat 10

---

## 🛠️ Step 3: Loop

```python id="g7t2mx"
for user in users:
```

---

## 🛠️ Step 4: Discount Extract

```python id="b3w8lp"
percent, fixed = discounts.get(user["coupon"], (0, 0))
```

---

## 🧠 Important

* `.get(key, default)`
* Agar coupon na mile → `(0, 0)` milega

---

## 🛠️ Step 5: Calculate Discount

```python id="n9r4sz"
discount = user["total"] * percent + fixed
```

---

## 🛠️ Step 6: Print

```python id="k2m7dv"
print(user["id"], "paid", user["total"], "got discount", discount)
```

---

## ▶️ Complete Code

```python id="x5c1hz"
users = [
    {"id": 1, "total": 100, "coupon": "P20"},
    {"id": 2, "total": 150, "coupon": "F10"},
    {"id": 3, "total": 80, "coupon": "P50"}
]

discounts = {
    "P20": (0.2, 0),
    "F10": (0.5, 0),
    "P50": (0, 10)
}

for user in users:
    percent, fixed = discounts.get(user["coupon"], (0, 0))
    discount = user["total"] * percent + fixed
    print(user["id"], "paid", user["total"], "got discount", discount)
```

---

## ▶️ Output

* 100 → discount 20
* 150 → discount 75
* 80 → discount 10

---

## 🧠 Important Points

* Dictionary se mapping easy hoti hai
* if-else ki need nahi
* scalable code hai
* new coupon add karna easy

---

## 📌 Notes

* Real world me isi tarah coupon system banta hai
* Database se values aati hain
* mapping use karke process hota hai

---

## 📎 Source

Based on transcript 
