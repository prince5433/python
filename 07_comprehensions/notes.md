# 🔁 Comprehensions in Python (Introduction)

---

## 📌 Introduction

* Topic: **Comprehensions**
* Python me ek important concept hai
* Production code me kaafi use hota hai

---

## 🧠 Important Observations

* Jo kaam comprehensions se hota hai → wo loops se bhi ho sakta hai
* Comprehensions sirf ek **stylized way** hai code likhne ka

---

## 📌 Why Use Comprehensions?

* Code short ho jata hai
* Ek line me kaam ho jata hai
* Kabhi-kabhi English jaisa feel hota hai

---

## ❗ Reality

* Starting me logon ko samajh nahi aata
* Kaafi log skip kar dete hain
* But production code me kaafi use hota hai

---

# 📖 Definition

👉 Comprehensions:

* Ek **concise way** hai banane ka:

  * lists
  * sets
  * dictionaries
  * generators

👉 Sirf **single line of code** me

---

## 🎯 Focus

* Single line me kaam karna

---

# 📍 Where are they used?

---

## 🔹 1. Filtering Items

* Example:

  * Hot tea select karna
  * Iced tea select karna

👉 Condition based filtering

---

## 🔹 2. Transforming Data

* Example:

  * INR → USD conversion

👉 Data modify karna

---

## 🔹 3. Creating New Collection

* Example:

  * Tea names → price mapping

👉 New structure create karna

---

## 🔹 4. Flatten Nested Structure

* Example:

  * Nested recipe se ingredients extract karna

👉 Complex structure ko simple banana

---

# 🎯 Purpose

---

## 🧠 Main Benefits

### ✔ Cleaner Code

* Readable hota hai
* Loop se better structure

---

### ✔ Faster Execution

* Kuch cases me faster hota hai
* Less memory use karta hai

---

## ❗ Note

* Easy nahi hota initially
* Practice se clear hota hai

---

# 🔁 Types of Comprehensions

---

## 🔹 1. List Comprehension

---

## 🔹 2. Set Comprehension

---

## 🔹 3. Dictionary Comprehension

---

## 🔹 4. Generator

* Ye alag concept hai
* Data type nahi hai

---

## 🧠 Notes

* Generator pe later detail me study hoga

---

# 📌 Final Notes

* Comprehensions powerful concept hai
* Production code me use hota hai
* Short + clean code likhne me help karta hai
* Practice required hai

---

## 📎 Source

Based on transcript 


# 📋 List Comprehension in Python

---

## 📌 Introduction

* Topic: **List Comprehension**
* Comprehensions ka pehla type
* Syntax samajhna important hai

---

# 🧠 Syntax

```python
[expression for item in iterable if condition]
```

---

## 🧠 Breakdown

* `[]` → list banane ke liye
* `expression` → kya store karna hai
* `for item in iterable` → loop
* `if condition` → filtering

---

# 🛠️ Example Setup

## 🧾 Menu List

```python
menu = [
    "masala chai",
    "iced lemon tea",
    "green tea",
    "iced peach tea",
    "ginger tea"
]
```

---

## 🎯 Goal

👉 Sirf **iced tea items filter karne hain**

---

# 🛠️ List Comprehension Code

```python
iced_tea = [tea for tea in menu if "iced" in tea]
```

---

## 🖨️ Print

```python
print(iced_tea)
```

---

## ▶️ Output

* iced lemon tea
* iced peach tea

---

# 🧠 Explanation

* `tea` → har item (string)
* `menu` → iterable (list)
* `"iced" in tea` → condition check
* Result → sirf matching items

---

# 🔍 Important Concept

* Strings bhi iterable hote hain
* Isliye `"iced" in tea` possible hai

---

# ⚠️ Variable Naming Rule

* Variable same hona chahiye

❌ Wrong:

```python
[tea for myt in menu if "iced" in tea]
```

✔ Correct:

```python
[myt for myt in menu if "iced" in myt]
```

---

## 🧠 Reason

* Variable loop se aata hai
* Same variable use karna zaroori hai

---

# 🔁 Changing Condition

## 🛠️ Example

```python
result = [tea for tea in menu if len(tea) > 12]
```

---

## 🧠 Concept

* Length check kar rahe hain
* Condition change kar sakte hain

---

## 🧪 Observation

* Condition ke basis par output change hota hai

---

# 🔍 Syntax Mapping

```python
[expression for item in iterable if condition]
```

👉 Mapping:

* expression → `tea`
* item → `tea`
* iterable → `menu`
* condition → `"iced" in tea`

---

# 📌 Key Points

* Loop internally use hota hai
* Condition optional hoti hai
* List comprehension = short + clean code
* Practice se easy ho jata hai

---

## 📎 Source

Based on transcript 

# 🔁 Set Comprehension in Python

---

## 📌 Introduction

* Next topic: **Set Comprehension**
* List comprehension jaisa hi hota hai
* Bas brackets change hote hain

---

# 🧠 Syntax

```python id="x8k3pl"
{expression for item in iterable if condition}
```

---

## 🧠 Important

* List → `[]`
* Set → `{}`

👉 Baaki sab same hai

---

# 📌 Key Idea

* Same syntax use hota hai
* Difference sirf bracket ka hai
* Set automatically **unique values** deta hai

---

# 🛠️ Example 1: Unique Chai

## 🧾 Data

```python id="a1m9vx"
favorite_chai = [
    "masala chai",
    "green tea",
    "masala chai",
    "lemon tea",
    "green tea",
    "lichi chai"
]
```

---

## 🎯 Goal

👉 Unique chai find karni hai

---

## 🛠️ Code

```python id="k5p2rt"
unique_chai = {chai for chai in favorite_chai}
```

---

## 🖨️ Print

```python id="n7d3qs"
print(unique_chai)
```

---

## 🧠 Concept

* Set duplicates remove kar deta hai
* Isliye unique values milti hain

---

# 🔁 With Condition

## 🛠️ Example

```python id="b2w8zx"
result = {chai for chai in favorite_chai if len(chai) > 8}
```

---

## 🧠 Observation

* Condition apply ho sakti hai
* Result change hota hai

---

# 📌 Important

* `if condition` optional hai
* Without condition bhi use kar sakte hain

---

# 🔥 Complex Example (Important)

---

## 🧾 Data: Dictionary

```python id="m8r4yt"
recipes = {
    "masala chai": ["ginger", "cardamom", "clove"],
    "elaichi chai": ["cardamom", "milk"],
    "spicy chai": ["ginger", "black pepper", "clove"]
}
```

---

## 🎯 Goal

👉 Sab **unique spices** nikalne hain

---

# 🛠️ Step 1: Outer Loop

```python id="c3k9lp"
for ingredients in recipes.values()
```

---

## 🧠 Concept

* `.values()` → list of ingredients
* Har iteration me ek list milegi

---

# 🛠️ Step 2: Inner Loop

```python id="z6p2mv"
for spice in ingredients
```

---

## 🧠 Concept

* Har ingredient list ke andar iterate kar rahe hain

---

# 🛠️ Final Set Comprehension

```python id="q1w7dv"
unique_spices = {spice for ingredients in recipes.values() for spice in ingredients}
```

---

## 🖨️ Print

```python id="y4t8qs"
print(unique_spices)
```

---

## ▶️ Output

* ginger
* cardamom
* clove
* black pepper
* milk

---

# 🧠 Important Concept

👉 Expression kya hoga?

* Final value jo collect karni hai → `spice`

---

## ❗ Important Point

* `ingredients` → temporary variable
* `spice` → final value

👉 Expression me **final value aati hai**, na ki middle variable

---

# 🔍 Syntax Mapping

```python id="h9m2zx"
{expression for item in iterable if condition}
```

👉 Mapping:

* expression → `spice`
* item → `spice`
* iterable → `ingredients`
* outer iterable → `recipes.values()`

---

# 📌 Key Points

* Set comprehension = list comprehension + `{}`
* Unique values automatically milte hain
* Nested loops possible hain
* Expression me final output value likhte hain
* `if condition` optional hai

---

## 📎 Source

Based on transcript 


# 📘 Dictionary Comprehension in Python

---

## 📌 Introduction

* Comprehensions ka next step → **Dictionary Comprehension**
* Ye dictionaries ko deeply samajhne me help karta hai
* Concept simple hai, bas ek difference samajhna hai

---

# 🧠 Key Concept

* Set aur Dictionary dono `{}` use karte hain

👉 Difference:

* Agar expression me sirf value → set
* Agar expression me **key:value pair** → dictionary

---

# 🧠 Important Idea

* Expression decide karta hai:

  * set banega ya dictionary

👉 Key + value pair → dictionary

---

# 🛠️ Example Setup

## 🧾 Tea Prices (INR)

```python id="a1m9vx"
tea_prices = {
    "masala chai": 40,
    "green tea": 50,
    "lemon tea": 200
}
```

---

## 🎯 Goal

👉 Sab prices ko INR → USD convert karna

* Conversion: divide by 80

---

# 🧠 Approach

* New dictionary banana padega
* Comprehension use karenge

---

# 🛠️ Loop Setup

```python id="k5p2rt"
for tea, price in tea_prices.items()
```

---

## 🧠 Concept

* `.items()`:

  * key + value dono deta hai
* `tea` → key
* `price` → value

---

# 🛠️ Dictionary Comprehension

```python id="n5k9rt"
tea_prices_usd = {tea: price/80 for tea, price in tea_prices.items()}
```

---

## 🧠 Expression

```python id="z6p3mv"
tea: price/80
```

👉 Key = tea
👉 Value = converted price

---

## 🖨️ Print

```python id="x2d7qs"
print(tea_prices_usd)
```

---

## ▶️ Output

* masala chai → 0.5
* green tea → 0.625
* lemon tea → 2.5

---

# 🔍 Important Observations

* Direct `tea_prices` iterate nahi kar sakte
* `.keys()` ya `.values()` alag-alag deta hai
* `.items()` se dono milte hain

---

# 🧠 Key Idea

👉 Comprehension ko samajhne ka best way:

* Pehle **for loop padho**
* Fir **expression samjho**

---

# 📌 Meaning in Simple Words

* Har tea ke liye
* Uska price lo
* Divide by 80
* New dictionary me store karo

---

# 📌 Key Points

* `{}` use hota hai
* Expression me key:value hona chahiye
* `.items()` important hai
* Expression me transformation hota hai
* Code short + clean ho jata hai

---

## 📎 Source

Based on transcript 

# ⚡ Generator Comprehension in Python

---

## 📌 Introduction

* Final type of comprehension → **Generator Comprehension**
* Ye generators ka intro hai
* Main purpose → **memory save karna**

---

## 🧠 Important Idea

* Generators ka main use:
  👉 **memory efficient code likhna**

* Large data (millions records) me useful hota hai

* Good software engineer memory ka dhyaan rakhta hai

---

# 🧠 Key Concept

* List comprehension → pura data memory me store karta hai
* Generator → ek-ek value deta hai (stream ki tarah)

---

# 🧠 Syntax

```python id="x8k3pl"
(expression for item in iterable if condition)
```

---

## 📌 Difference

* List → `[]`
* Generator → `()`

👉 Bas bracket ka difference hai

---

# 🔁 Comparison

## 🛠️ List Comprehension

```python id="a1m9vx"
[x for x in items]
```

👉 Entire list memory me ban jati hai

---

## 🛠️ Generator

```python id="k5p2rt"
(x for x in items)
```

👉 Ek-ek item generate hota hai

---

## 🧠 Concept

* List → full data ek saath
* Generator → stream (one by one)

---

# 📊 Example Setup

## 🧾 Daily Sales

```python id="n7d3qs"
daily_sales = [5, 10, 12, 7, 3, 8, 9, 15]
```

---

## 🎯 Goal

👉 Sirf wo values chahiye:

* jo **5 se badi ho**
  👉 Unka total sum nikalna hai

---

# 🛠️ Generator Comprehension

```python id="q1w7dv"
(sale for sale in daily_sales if sale > 5)
```

---

## 🧠 Observation

* Direct print karoge → generator object milega
* Ye list nahi hota

---

## 🖨️ Output Type

👉 Generator object

* Direct usable nahi
* Consume karna padta hai

---

# 🔁 Using List Instead

```python id="y4t8qs"
[sale for sale in daily_sales if sale > 5]
```

👉 Ye list return karega

---

# ⚡ Best Use (Important)

## 🛠️ Using sum()

```python id="h9m2zx"
sum(sale for sale in daily_sales if sale > 5)
```

---

## 🧠 Concept

* Generator → values ek-ek karke deta hai
* `sum()` → unhe process karta hai

👉 Memory efficient

---

# 🧠 Important Difference

### List:

* Full data memory me store
* Heavy ho sakta hai

---

### Generator:

* One-by-one data
* Memory efficient
* Stream jaisa behavior

---

# 📌 Key Points

* Generator → `()` use karta hai
* Memory save karta hai
* Large data ke liye best
* Direct print → generator object
* `sum()` jaise functions ke saath useful

---

# 📌 Final Idea

* List → fast access but heavy
* Generator → slow access but memory efficient

---

## 📎 Source

Based on transcript 
