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

