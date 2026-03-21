# Python Objects, Mutability & Immutability — Ep. 4

---

## 1. Python mein "Everything is an Object"

Har cheez jo Python mein hoti hai — number, string, list — sab **objects** hain.

Har object ke teen properties hote hain:

```
Object
├── Identity  → unique ID (memory address)
├── Type      → kya hai (int, str, list, set...)
└── Value     → actual data (2, "chai", [1,2,3]...)
```

---

## 2. Identity Check karna — `id()` function

```python
sugar_amount = 2
print(id(2))   # Ek unique number → memory address
print(id(12))  # Alag unique number
```

---

## 3. Mutable vs Immutable

| | Mutable | Immutable |
|---|---|---|
| Matlab | Memory mein badla ja sakta hai | Memory mein nahi badlta |
| Examples | `list`, `set`, `dict` | `int`, `float`, `str`, `tuple` |
| ID change hota hai? | ❌ Nahi | ✅ Haan (naya object banta hai) |

---

## 4. Immutable — Numbers ka Example

```python
sugar_amount = 2
print(id(sugar_amount))   # Example: ...680

sugar_amount = 12
print(id(sugar_amount))   # Example: ...360  ← ALAG ID!
```

**Kya hua behind the scenes:**
```
Pehle:  sugar_amount ──→ [2]  (memory mein)
Baad mein: sugar_amount ──→ [12]  (NAYA object bana)
                              [2] ab bhi memory mein hai — unchanged!
```

- Number `2` kabhi change nahi hua
- Sirf **reference** (pointer) badla — `sugar_amount` ab `12` ko point kar raha hai
- Yahi hai **immutability** — object nahi badla, reference badla

---

## 5. Mutable — Set ka Example

```python
spice_mix = set()
print(id(spice_mix))   # Example: ...944

spice_mix.add("ginger")
spice_mix.add("cardamom")
print(id(spice_mix))   # Example: ...944  ← SAME ID!
```

**Kya hua:**
```
spice_mix ──→ {  }        (pehle)
spice_mix ──→ { "ginger", "cardamom" }  (baad mein)
              ↑ SAME object, modified in-place
```

- Same object memory mein modify ho gaya
- ID nahi badla — yahi hai **mutability**

---

## 6. Golden Rule ⚠️

> **Mutability check karne ke liye value mat dekho — `id()` dekho!**

```python
# ❌ Wrong way — value se judge karna
x = 2
x = 12
# "value change ho gayi toh mutable hai" — GALAT!

# ✅ Right way — id() se check karo
print(id(x))  # Pehle aur baad ka ID compare karo
```

---

## 7. F-String (Formatted String)

```python
sugar_amount = 2
print(f"Initial sugar: {sugar_amount}")      # → Initial sugar: 2
print(f"ID of 2: {id(2)}")                   # → ID of 2: 140234...
```

---

## 8. Summary Table

| Data Type | Mutable? | Reason |
|---|---|---|
| `int`, `float` | ❌ Immutable | Value change hone pe naya object banta hai |
| `str` | ❌ Immutable | String in-place modify nahi hoti |
| `tuple` | ❌ Immutable | Elements change nahi ho sakte |
| `list` | ✅ Mutable | Elements add/remove — same ID |
| `set` | ✅ Mutable | Elements add/remove — same ID |
| `dict` | ✅ Mutable | Keys/values change — same ID |

---

## Next Video → Python Data Types in Detail

# Numbers & Booleans in Python — Ep. 5

---

## 1. Number Types in Python

| Type | Name | Example |
|---|---|---|
| Integer | `int` | `14`, `3`, `-5` |
| Float | `float` | `95.5`, `1.75` |
| Boolean | `bool` | `True`, `False` |
| Complex | `complex` | `2 + 3j` (rare use) |

---

## 2. Arithmetic Operators

```python
black_tea_grams = 14
ginger_grams = 3

total_grams = black_tea_grams + ginger_grams    # 17  → Addition
remaining   = black_tea_grams - ginger_grams    # 11  → Subtraction
result      = black_tea_grams * ginger_grams    # 42  → Multiplication

# Division
milk_liters = 7
servings = 4
milk_per_serving = milk_liters / servings       # 1.75  → True division (float)

# Floor Division (decimal ignore)
teabags = 7
pots = 4
bags_per_pot = teabags // pots                  # 1  → Sirf whole number

# Modulo (remainder)
cardamom_pods = 10
pods_per_cup = 3
leftover = cardamom_pods % pods_per_cup         # 1  → Bacha hua

# Exponent (power)
base = 2
scale = 3
powerful = base ** scale                        # 8  → 2³ = 8
```

---

## 3. Readability — Underscore in Numbers

```python
# Bade numbers mein underscore use karo — readability ke liye
total_leaves = 1_000_000_000   # 1 billion
# Underscore ignore hota hai — sirf visual aid hai
print(total_leaves)  # → 1000000000
```

---

## 4. Boolean — `True` / `False`

```python
is_boiling = True    # Capital T zaroori
tea_added = False    # Capital F zaroori

can_serve_chai = is_boiling and tea_added   # False (tea nahi add ki)
tea_added = True
can_serve_chai = is_boiling and tea_added   # True (ab dono True hain)
```

---

## 5. Boolean = Number (Upcasting)

```python
# True = 1, False = 0
stir_count = 5
is_boiling = True
total_actions = stir_count + is_boiling   # 5 + 1 = 6
```

---

## 6. `bool()` Conversion

```python
bool(0)        # False
bool(1)        # True
bool(11)       # True  ← 0 ke alawa sab True
bool("Hitesh") # True  ← non-empty string → True
bool(None)     # False
bool("")       # False ← empty string → False
```

> **Rule:** `0`, `None`, `""` (empty), `[]` (empty list) → **False**. Baaki sab → **True**

---

## 7. Logical Operators

| Operator | Matlab | Example |
|---|---|---|
| `and` | Dono True hona chahiye | `water_hot and tea_added` |
| `or` | Ek bhi True ho toh chalega | `tea or coffee` |
| `not` | Ulta karo | `not is_boiling` → `False` |

---

## 8. Float Precision Issue

```python
ideal_temp = 95.5
current_temp = 95.4999999

difference = ideal_temp - current_temp
print(difference)   # 9.e-08  ← Unexpected! Floating point precision issue

# Zyada precision ke liye → decimal module use karo
from decimal import Decimal
# ya
import sys
print(sys.float_info)   # Float ki limits dekho
```

---

## 9. Precision ke liye Special Modules

```python
from fractions import Fraction   # Exact fractions ke liye
from decimal import Decimal      # High precision decimals ke liye
```

---

## Next Video → Strings in Python