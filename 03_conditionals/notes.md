# Conditionals in Python — `if` Statement — Ep. 11

---

## 1. Conditionals kya hain?

Kisi condition ke basis pe decision lena — yes/no, true/false.

```
Kya ghar pe chai patti hai?
├── Haan → chai banao
└── Nahi → chai patti kharido
```

---

## 2. `if` Statement — Basic Syntax

```python
kettle_boiled = True

if kettle_boiled:               # Condition → True/False honi chahiye
    print("Kettle done!")       # ← Indentation zaroori (4 spaces)
    print("Time to make chai")
```

**Output:**
```
Kettle done!
Time to make chai
```

> ⚠️ **Indentation bahut important hai Python mein** — galat indentation = error

---

## 3. False hone pe kya hoga?

```python
kettle_boiled = False

if kettle_boiled:
    print("Kettle done!")   # Yeh print nahi hoga
```

**Output:** (kuch print nahi hoga)

---

## 4. `if` ke saath conditions

```python
# Boolean variable
if is_boiling:
    print("Water is hot!")

# Comparison expression
temperature = 100
if temperature >= 100:
    print("Boiling!")

# Any expression jo True/False evaluate ho
if kettle_boiled == True:   # Same as: if kettle_boiled:
    print("Done!")
```

---

## 5. Syntax Rules

```python
if condition:     # ← colon zaroori
    # code here   # ← 4 spaces indent zaroori
    # ...
# Yahan se indent khatam → if block khatam
```

---

## 6. Mini Story — Smart Kettle Notification

**Problem:** Ek notification system banao jo sirf tab message show kare jab kettle boil ho jaaye.

```python
# ministory1.py
kettle_boiled = True

if kettle_boiled:
    print("Kettle done! Time to make chai")
```

---

## Next Video → `if-else` and `elif` Conditionals

# Python — Mini Project: Snack Suggestion System

---

## Problem Statement

Local cafe ke liye ek program banana hai jo:
1. User se preferred snack pooche
2. Agar **cookies** ya **samosa** hai → order confirm karo
3. Warna → unavailability message dikhao

---

## 2 New Concepts — Is Project Mein

### 1. `input()` — User se Input Lena

```python
snack = input("Enter your preferred snack: ")
```

- Python mein command line input lena itna simple hai
- `input()` hamesha **string** return karta hai — numbers bhi string mein aate hain
- String mein question likhte hain — woh user ko prompt ke roop mein dikhta hai

### 2. `.lower()` — Case Problem Solve karna

User koi bhi case mein type kar sakta hai: `Samosa`, `SAMOSA`, `sAmOsA`

```python
snack = input("Enter your preferred snack: ").lower()
# Ab chahe kuch bhi type karo — lowercase mein convert ho jaayega
```

> ✅ Ek chhoti method se comparison bahut easy ho jaata hai

---

## Final Code

```python
# snack_suggestion.py

snack = input("Enter your preferred snack: ").lower()

if snack == "cookies" or snack == "samosa":
    print(f"Great choice! We will serve you {snack}.")
else:
    print("Sorry, we only serve cookies or samosa with tea.")
```

---

## Key Points

| Concept | Detail |
|---|---|
| `input()` | User se string input leta hai |
| `.lower()` | Input ko lowercase mein convert karo |
| `==` | Comparison (do equal) — assignment nahi |
| `=` | Assignment (ek equal) — value store karna |
| `or` | Dono conditions check karna |

---

## Real World Connection

> 💡 Early days mein AI nahi tha — suggestion systems exactly aise hi banate the: if-else + mapping. Aaj bhi chhote systems mein yahi hota hai.

---

## Next Video → Agle concept ki taraf

# Chai Price Calculator – Lecture Notes

## Topic
Building a **Chai Price Calculator** in Python using conditional statements (`if`, `elif`, `else`).

---

## Problem Statement
A tea stall offers different prices for different cup sizes. Write a program that:
1. Takes user input: `small`, `medium`, or `large`
2. Outputs the price based on the cup size
3. Handles invalid input with an "unknown cup size" message

### Prices
| Cup Size | Price     |
|----------|-----------|
| Small    | ₹10       |
| Medium   | ₹15       |
| Large    | ₹20       |

---

## Key Concepts Covered

### 1. User Input
- Use `input()` to prompt the user to choose a cup size
- Convert input to lowercase using `.lower()` — good practice to handle case-insensitive input

```python
cup = input("Choose your cup size (small / medium / large): ").lower()
```

### 2. Conditional Statements — `if`, `elif`, `else`
- `if` — checks the first condition
- `elif` (else if) — checks additional conditions when the previous ones are `False`
- `else` — catches everything that doesn't match any condition

> **New concept:** `elif` is introduced here for handling **more than two conditions**, unlike the simple `if/else` seen before.

```python
if cup == "small":
    print("Price is 10 rupees")
elif cup == "medium":
    print("Price is 15 rupees")
elif cup == "large":
    print("Price is 20 rupees")
else:
    print("Unknown cup size")
```

### 3. Why `.lower()` Matters
- Ensures input like `"Small"`, `"SMALL"`, or `"small"` all match the same condition
- Always normalize user input to a single case (upper or lower)

---

## Key Takeaways
- Real-world problems are the best way to learn programming concepts
- `elif` lets you handle **multiple distinct conditions**, each with its own action
- Always handle invalid input gracefully using `else`
- Learning syntax in isolation is less effective than solving practical problems

# Smart Thermostat Alert System – Lecture Notes

## Topic
Building a **Smart Thermostat Alert System** in Python using **nested `if` statements**.

---

## Problem Statement
Build a program that:
1. Checks if the device status is `"active"` or `"offline"`
2. If active, checks whether the temperature is above 35°C
3. Outputs the appropriate alert or status message

### Logic
| Device Status | Temperature | Output                  |
|---------------|-------------|-------------------------|
| active        | > 35        | High temperature alert! |
| active        | ≤ 35        | Temperature is normal   |
| offline       | —           | Device is offline       |

---

## Key Concepts Covered

### 1. Nested `if` Statements
Checking a condition **inside** another condition — also called **nesting**.

```python
device_status = "active"
temperature = 38

if device_status == "active":
    if temperature > 35:
        print("High temperature alert!")
    else:
        print("Temperature is normal")
else:
    print("Device is offline")
```

> **Key idea:** The inner `if/else` only runs when the outer `if` is `True`. Each block is defined by its **indentation level**.

### 2. The `pass` Keyword
A placeholder that tells Python "I'll fill this in later" — prevents syntax errors while writing code incrementally.

```python
if device_status == "active":
    pass  # come back to this
else:
    print("Device is offline")
```

Useful when you want to write the `else` part first without Python complaining about an empty `if` block.

### 3. Indentation & Blocks
- Indentation defines which `else` belongs to which `if`
- The **outer** `else` pairs with the **outer** `if`
- The **inner** `else` pairs with the **inner** `if`
- You can nest as many levels deep as needed

---

## Key Takeaways
- Nested `if` statements let you check conditions **within** conditions
- `pass` is a handy placeholder when writing code incrementally
- Always pay attention to **indentation** — it determines the logic flow
- Complex problems are solved the same way: read carefully, break into steps, build piece by piece

# Delivery Fee Calculator – Lecture Notes

## Topic
Building a **Delivery Fee Calculator** in Python, introducing two key concepts:
- **Type conversion** (string → integer)
- **Ternary operator** (one-line if/else)

---

## Problem Statement
You run an online tea store. Write a program that:
1. Takes the order amount as input from the user
2. Decides the delivery fee using a **ternary operator**

### Pricing Rule
| Order Amount | Delivery Fee |
|--------------|--------------|
| > ₹300       | ₹0 (free)    |
| ≤ ₹300       | ₹30          |

---

## Key Concepts Covered

### 1. Type Conversion — `int()`
User input via `input()` always comes back as a **string**, even if the user types a number.

```python
order_amount = input("Enter order amount: ")
print(type(order_amount))  # <class 'str'>
```

To use it in numeric comparisons, wrap it with `int()`:

```python
order_amount = int(input("Enter order amount: "))
print(type(order_amount))  # <class 'int'>
```

> **Note:** If the user types something non-numeric (e.g. "hello"), `int()` will crash. Error handling will be covered later.

Other conversion functions: `float()`, `str()`

---

### 2. Ternary Operator
A way to write a simple `if/else` in **one line**.

**Standard if/else:**
```python
if order_amount > 300:
    delivery_fees = 0
else:
    delivery_fees = 30
```

**Ternary equivalent:**
```python
delivery_fees = 0 if order_amount > 300 else 30
```

**Syntax pattern:**
```
variable = value_if_true  if  condition  else  value_if_false
```

> Python reads almost like English here — "delivery fees is 0 **if** order amount > 300, **else** 30."

---

## Full Program

```python
order_amount = int(input("Enter order amount: "))

delivery_fees = 0 if order_amount > 300 else 30

print(f"Delivery fees is: {delivery_fees}")
```

**Sample runs:**
- Order = 100 → Delivery fees = 30
- Order = 400 → Delivery fees = 0

---

## Key Takeaways
- `input()` always returns a **string** — use `int()` or `float()` to convert for numeric use
- The **ternary operator** condenses a simple `if/else` into one readable line
- Python syntax often reads close to plain English, but the logic still requires careful thought
- Real-world problems are the best way to discover and understand new syntax

# Train Seat Info System – Lecture Notes

## Topic
Building a **Railway Ticket Info System** in Python using the **`match/case`** statement — a cleaner alternative to long `if/elif/else` chains.

---

## Problem Statement
Build a program that:
1. Takes seat type as input: `sleeper`, `ac`, `general`, or `luxury`
2. Displays the features of the chosen seat
3. Shows "Invalid seat type" for unrecognized input

### Seat Features
| Seat Type | Features                        |
|-----------|---------------------------------|
| sleeper   | No AC, beds available           |
| ac        | Air conditioned, comfy ride     |
| general   | Cheapest option, no reservation |
| luxury    | Premium seats with meals        |
| other     | Invalid seat type               |

---

## Key Concept: `match/case` Statement

An alternative to `if/elif/else` when checking **one variable against many possible values**. Much more readable for multiple cases.

**Standard if/elif approach:**
```python
if seat_type == "sleeper":
    print("No AC, beds available")
elif seat_type == "ac":
    print("Air conditioned, comfy ride")
# ...and so on
```

**match/case equivalent:**
```python
match seat_type:
    case "sleeper":
        print("No AC, beds available")
    case "ac":
        print("Air conditioned, comfy ride")
    case "general":
        print("Cheapest option, no reservation")
    case "luxury":
        print("Premium seats with meals")
    case _:
        print("Invalid seat type")
```

> **`case _`** is the wildcard/default — matches anything that didn't match above. Equivalent to `else`.

---

## Full Program

```python
seat_type = input("Enter seat type (sleeper / ac / general / luxury): ").lower()

match seat_type:
    case "sleeper":
        print("No AC, beds available")
    case "ac":
        print("Air conditioned, comfy ride")
    case "general":
        print("Cheapest option, no reservation")
    case "luxury":
        print("Premium seats with meals")
    case _:
        print("Invalid seat type")
```

---

## Key Takeaways
- `match/case` is a clean alternative to long `if/elif/else` chains
- Behind the scenes, `case "sleeper"` is doing `seat_type == "sleeper"`
- `case _` is the default/fallback — always put it last
- Can match integers, floats, and strings
- `.lower()` on input keeps matching simple — no need to handle `"AC"`, `"Ac"`, etc.

---

## Conditionals Summary (so far)
| Situation | Use |
|-----------|-----|
| Simple true/false | `if / else` |
| Condition within a condition | Nested `if` |
| Short one-liner decision | Ternary operator |
| Many values of one variable | `match / case` |