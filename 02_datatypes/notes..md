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

# Strings in Python — Indexing, Slicing & Encoding — Ep. 6

---

## 1. String kya hai?

```python
chai_type = "Ginger Chai"    # Double quotes
customer_name = "Priya"      # Single quotes bhi chalte hain

# F-string se print karna
print(f"Order for {customer_name}: {chai_type} please!")
# → Order for Priya: Ginger Chai please!
```

> Strings are **immutable** — in-place change nahi hoti, naya object banta hai

---

## 2. Indexing — Har character ka number hota hai

```
A  r  o  m  a  t  i  c
0  1  2  3  4  5  6  7

# Negative indexing (peeche se)
-8 -7 -6 -5 -4 -3 -2 -1
```

```python
chai_desc = "Aromatic and Bold"
print(chai_desc[0])   # A  (pehla character)
print(chai_desc[-1])  # d  (aakhri character)
```

---

## 3. Slicing — `[start : end : step]`

```python
chai_desc = "Aromatic and Bold"

# Basic slicing
first_word = chai_desc[0:8]    # "Aromatic" (0 se 7 tak — 8 include nahi)
last_word  = chai_desc[13:]    # "Bold" (13 se end tak)
all_text   = chai_desc[:]      # Poora string

# Step
every_second = chai_desc[0:8:2]  # "Arai" (har doosra character)

# Reverse karna — classic Python trick
reversed_str = chai_desc[::-1]   # "dloB dna citamorA"
```

> **Remember:** End index **inclusive nahi** hoti — `[0:8]` mein index 7 tak milega, 8 nahi

---

## 4. Slicing ke Rules

| Syntax | Matlab |
|---|---|
| `[0:8]` | Index 0 se 7 tak |
| `[13:]` | Index 13 se end tak |
| `[:8]` | Start se index 7 tak |
| `[:]` | Poora string |
| `[::2]` | Har doosra character |
| `[::-1]` | Reverse string |

---

## 5. String Methods (kuch examples)

```python
chai_type = "ginger chai"

chai_type.capitalize()  # "Ginger chai"
chai_type.upper()       # "GINGER CHAI"
chai_type.lower()       # "ginger chai"
chai_type.count("a")   # 2
len(chai_type)          # 11
```

---

## 6. Encoding & Decoding (Special Characters)

```python
label_text = "Café Chai"   # Special character é

# Encode karo
encoded_label = label_text.encode("utf-8")
print(encoded_label)  # b'Caf\xc3\xa9 Chai'

# Decode karo (wapas normal string)
decoded_label = encoded_label.decode("utf-8")
print(decoded_label)  # "Café Chai"
```

- **UTF-8** → sabse common encoding — Hindi, Japanese, Chinese sab handle karta hai
- Special characters wale strings mein encode/decode zaroori hota hai

---

## Next Video → Lists in Python

# Tuples in Python — Ep. 7

---

## 1. Tuple kya hai?

- **Immutable** collection — ek baar bana liya toh change nahi hoga
- **Parentheses** `()` se define hota hai

```python
masala_spices = ("cardamom", "clove", "cinnamon")
```

---

## 2. Tuple Unpacking

```python
masala_spices = ("cardamom", "clove", "cinnamon")

# Values nikalna (unpacking)
spice1, spice2, spice3 = masala_spices
print(spice1)   # cardamom
print(spice2)   # clove
print(spice3)   # cinnamon
```

> Number of variables = Number of elements hona chahiye

---

## 3. Variable Swap — Python ka Superpower ✨

```python
ginger_ratio = 2
cardamom_ratio = 1

# Dono variables swap karo — bina temporary variable ke!
ginger_ratio, cardamom_ratio = cardamom_ratio, ginger_ratio

print(ginger_ratio)    # 1
print(cardamom_ratio)  # 2
```

- Behind the scenes Python tuple use karta hai swap karne ke liye
- Doosri languages mein temporary variable chahiye — Python mein nahi!

---

## 4. Membership Testing — `in` keyword

```python
masala_spices = ("cardamom", "clove", "cinnamon")

print("cinnamon" in masala_spices)   # True
print("ginger" in masala_spices)     # False
print("Cinnamon" in masala_spices)   # False ← Case sensitive!
```

---

## 5. Tuple vs List — Key Difference

| | Tuple `()` | List `[]` |
|---|---|---|
| Mutable? | ❌ No | ✅ Yes |
| Use case | Fixed data (coordinates, colors) | Dynamic data (cart items) |
| Speed | Slightly faster | Slightly slower |

---

## 6. Summary

- `()` → Tuple (immutable)
- `[]` → List (mutable)
- `{}` → Set / Dict (curly braces)
- Unpacking → values seedha variables mein
- `in` → membership check

---

## Next Video → Lists in Python

# Lists in Python — Ep. 8

---

## 1. List kya hai?

- **Mutable** collection — baad mein change kar sakte ho
- **Square brackets** `[]` se define hota hai
- Doosri languages mein "array" kehte hain

```python
ingredients = ["water", "milk", "black tea"]
```

---

## 2. Common List Methods

```python
ingredients = ["water", "milk", "black tea"]

# Add karna
ingredients.append("sugar")         # End mein add karo
ingredients.insert(2, "black tea")  # Specific position pe add karo

# Remove karna
ingredients.remove("water")         # Value se remove karo (pehla match)
last = ingredients.pop()            # Last item remove karo + return karo

# Combine karna
spices = ["ginger", "cardamom"]
chai = ["water", "milk"]
chai.extend(spices)                 # chai mein spices add ho jaayenge
# Result: ["water", "milk", "ginger", "cardamom"]

# Reverse/Sort
ingredients.reverse()   # In-place reverse (kuch return nahi karta)
ingredients.sort()      # Alphabetically sort karo

# Min/Max
sugar_levels = [1, 2, 3, 4, 5]
print(max(sugar_levels))   # 5
print(min(sugar_levels))   # 1
```

---

## 3. Indexing — 0 se start hota hai

```python
chai = ["water", "milk", "black tea", "ginger"]
#        0        1       2            3

print(chai[0])    # water
print(chai[-1])   # ginger (peeche se)
```

---

## 4. `insert()` vs `append()`

```python
# append → hamesha end mein
ingredients.append("sugar")       # [..., "sugar"]

# insert → specific position pe
ingredients.insert(2, "black tea") # Index 2 pe add, baaki shift hote hain
```

---

## 5. `pop()` — Last Item Remove + Return

```python
last_added = chai.pop()   # Last item remove karo aur variable mein save karo
print(last_added)         # "ginger"
print(chai)               # ["water", "milk", "black tea"]
```

---

## 6. `reverse()` aur `sort()` — In-Place Operations

```python
# ❌ Wrong — None return hota hai
result = ingredients.reverse()   # None milega

# ✅ Sahi — directly call karo
ingredients.reverse()
print(ingredients)   # Reversed list
```

> Yeh methods list ko **modify** karte hain, kuch **return** nahi karte

---

## 7. Tuple vs List — Quick Recap

| | List `[]` | Tuple `()` |
|---|---|---|
| Mutable | ✅ Yes | ❌ No |
| Methods | Many (append, remove...) | Few |
| Use case | Dynamic data | Fixed data |

---

## Next Video → Lists — More Methods (continued)

# Lists — Operator Overloading & Bytearray — Ep. 9

---

## 1. Operator Overloading with Lists

```python
base_liquid = ["water", "milk"]
extra_flavor = ["ginger"]

# + operator → Lists combine karo (concatenation)
liquid_mix = base_liquid + extra_flavor
print(liquid_mix)   # ["water", "milk", "ginger"]

# * operator → List repeat karo
strong_brew = ["black tea"] * 3
print(strong_brew)  # ["black tea", "black tea", "black tea"]

# Multiple elements ke saath multiply
brew = ["black tea", "water"] * 3
print(brew)
# ["black tea", "water", "black tea", "water", "black tea", "water"]
# Poori list repeat hoti hai — ek element nahi
```

---

## 2. Operator Overloading kya hai?

- Ek operator (`+`, `*`) jo originally numbers ke liye tha
- Lists ke saath use karo → different kaam karta hai
- Yahi hai **operator overloading**

---

## 3. `itemgetter` from `operator` module (Advanced)

```python
from operator import itemgetter
# Complex sorting ke liye use hota hai — source code mein dikhega
# Abhi ke liye sirf jaanna kafi hai ki exist karta hai
```

---

## 4. `bytearray` — String ko Bytes mein Convert karna

```python
# String ko bytearray mein convert karo
raw_spice_data = bytearray(b"cinnamon")

# Replace karna
raw_spice_data = raw_spice_data.replace(b"cinnamon", b"cardamom")
print(raw_spice_data)   # bytearray(b'cardamom')
```

**Important gotcha:**
```python
# ❌ Wrong — original nahi badlega
raw_spice_data.replace(b"cinnamon", b"cardamom")
print(raw_spice_data)   # Abhi bhi "cinnamon" dikhega!

# ✅ Sahi — return value save karo
raw_spice_data = raw_spice_data.replace(b"cinnamon", b"cardamom")
```

> `bytearray` mostly character-level operations ke liye use hota hai — rarely needed

---

## 5. List Methods — Full Summary

| Method | Kaam |
|---|---|
| `append(x)` | End mein add |
| `insert(i, x)` | Index i pe add |
| `remove(x)` | Pehla match remove |
| `pop()` | Last item remove + return |
| `extend(list)` | Doosri list merge karo |
| `reverse()` | In-place reverse (None return) |
| `sort()` | In-place sort (None return) |
| `+` operator | New list banao (concatenation) |
| `*` operator | List repeat karo |
| `max(list)` | Maximum value |
| `min(list)` | Minimum value |

---

## Next Video → Dictionaries in Python

# Sets in Python — Ep. 10

---

## 1. Set kya hai?

- **Unique** elements ka collection — duplicates allowed nahi
- **Curly braces** `{}` se define hota hai
- Mathematical sets jaise kaam karta hai

```python
essential_spices = {"cardamom", "ginger", "cinnamon"}
optional_spices  = {"cloves", "ginger", "black pepper"}
```

---

## 2. Set Operations

### Union `|` — Sab kuch, duplicates hatao

```python
all_spices = essential_spices | optional_spices
print(all_spices)
# {"cardamom", "ginger", "cinnamon", "cloves", "black pepper"}
# Ginger ek baar hi aaya — duplicate nahi!
```

### Intersection `&` — Common elements only

```python
common_spices = essential_spices & optional_spices
print(common_spices)   # {"ginger"}
```

### Difference `-` — A mein hain, B mein nahi

```python
only_in_essential = essential_spices - optional_spices
print(only_in_essential)   # {"cardamom", "cinnamon"}
# Ginger common tha → remove ho gaya
```

---

## 3. Visual Summary

```
essential = {cardamom, ginger, cinnamon}
optional  = {cloves, ginger, black pepper}

Union (|)        → {cardamom, ginger, cinnamon, cloves, black pepper}
Intersection (&) → {ginger}
Difference (-)   → {cardamom, cinnamon}  (essential - optional)
```

---

## 4. Membership Test — `in` keyword

```python
print("cloves" in optional_spices)    # True
print("cloves" in essential_spices)   # False
# Case sensitive hai!
```

---

## 5. Frozen Set — Immutable Set

```python
frozen = frozenset({"cardamom", "ginger"})
# frozen.add("cinnamon")  ← ❌ Error — frozen set change nahi hota
```

- Regular set → mutable
- `frozenset` → immutable (tuple jaisa, but set ki uniqueness ke saath)

---

## 6. Summary Table

| Operation | Symbol | Matlab |
|---|---|---|
| Union | `\|` | Sab elements (no duplicates) |
| Intersection | `&` | Common elements only |
| Difference | `-` | A mein hain, B mein nahi |
| Membership | `in` | Element hai ya nahi |

---

## Next Video → Dictionaries in Python

# Python — Dictionary (Chapter 10)

---

## 1. Dictionary kyun exist karta hai?

- **List** mein data index se access hota hai (0, 1, 2...)
- But kabhi kabhi number se access karna awkward lagta hai
- Dictionary mein **named indexing** hoti hai — number ki jagah naam se access karo

```python
# List — index se access karna padta hai
items = ["Ginger", "Lemon"]
items[0]   # Ginger — but kaise pata 0 pe kya hai?

# Dictionary — naam se access karo ✅
chai_order = {"type": "Masala Chai", "size": "Large", "sugar": 2}
chai_order["type"]   # "Masala Chai" — clear hai!
```

> ✅ Dictionary = **named indexing** — data ko meaningful naam se store karo

---

## 2. Dictionary banana — 2 Ways

```python
# Way 1 — curly braces (most common)
chai_order = {
    "type": "Masala Chai",
    "size": "Large",
    "sugar": 2
}

# Way 2 — dict() function
chai_order = dict(type="Masala Chai", size="Large", sugar=2)
```

---

## 3. Data Add karna

```python
chai_recipe = {}   # empty dictionary

chai_recipe["base"] = "Black Tea"     # key: base, value: Black Tea
chai_recipe["liquid"] = "Milk"        # key: liquid, value: Milk
```

> ⚠️ Same key pe dobara assign karo toh **overwrite** ho jaayega

---

## 4. Data Access karna

```python
# Square brackets se access karo
print(chai_recipe["base"])    # Black Tea

# Sirf base milega, liquid nahi
```

---

## 5. Data Delete karna

```python
# del keyword se delete karo
del chai_recipe["liquid"]

print(chai_recipe)   # sirf base bachega
```

---

## 6. Keys, Values, Items

```python
chai_order = {"type": "Ginger Chai", "size": "Medium", "sugar": 1}

print(chai_order.keys())    # dict_keys(['type', 'size', 'sugar'])
print(chai_order.values())  # dict_values(['Ginger Chai', 'Medium', 1])
print(chai_order.items())   # dict_items([('type', 'Ginger Chai'), ('size', 'Medium'), ('sugar', 1)])
```

- `.keys()` → sirf keys ki list
- `.values()` → sirf values ki list
- `.items()` → **(key, value) tuples** ki list — loop mein useful

---

## 7. pop() — Item Remove karna

```python
last_item = chai_order.popitem()   # last item remove karta hai
print("Removed:", last_item)       # ('sugar', 1)

# Specific key pop karna
removed = chai_order.pop("sugar")
print("Removed sugar:", removed)   # 1
```

---

## 8. update() — Dictionary Merge/Update karna

```python
spices = {"cardamom": "crushed", "ginger": "sliced"}

chai_recipe.update(spices)   # spices ke keys-values chai_recipe mein add ho jaayenge

print(chai_recipe)
# {'base': 'Black Tea', 'cardamom': 'crushed', 'ginger': 'sliced'}
```

---

## 9. Membership Testing

```python
# 'in' keyword se check karo key exist karti hai ya nahi
print("sugar" in chai_order)    # True
print("milk" in chai_order)     # False
```

---

## 10. `.get()` — Safe Access ⚠️

```python
# ❌ Key exist nahi karta toh crash ho jaata hai
note = chai_order["customer_note"]   # KeyError!

# ✅ .get() se safely access karo — crash nahi hoga
note = chai_order.get("customer_note", "No note given")
print(note)   # No note given

# Key exist karti ho toh value milegi
size = chai_order.get("size", "Unknown")
print(size)   # Medium
```

> ✅ `.get()` ka second argument = **default value** — key na mile toh yeh return hoga

---

## Summary

| Operation | Code |
|---|---|
| Create | `d = {"key": "value"}` |
| Add / Update | `d["key"] = "value"` |
| Access | `d["key"]` |
| Safe Access | `d.get("key", default)` |
| Delete | `del d["key"]` |
| Pop last | `d.popitem()` |
| Pop specific | `d.pop("key")` |
| All keys | `d.keys()` |
| All values | `d.values()` |
| All pairs | `d.items()` |
| Merge | `d.update(other_dict)` |
| Membership test | `"key" in d` |

---

> 💡 Dictionary mein order matter nahi karta — hum naam se access karte hain, index se nahi

# Python — Advanced Data Types (Bonus)

> ⚠️ **Yeh beginner ke liye nahi hai** — 6 months Python experience ke baad revisit karna. Abhi sirf awareness ke liye padho.

---

## 1. Advanced Data Types kahan se aate hain?

- Yeh Python ke **default** mein nahi hote
- **Import** karna padta hai — ya toh built-in modules se ya third-party packages se
- Ab tak jo bhi likha — koi `import` nahi kiya — kyunki basic types (str, list, dict) import nahi chahiye

---

## 2. Date & Time Related Types

Python mein built-in date/time modules hain:

| Module | Kaam |
|---|---|
| `datetime` | Date aur time dono saath |
| `time` | Sirf time |
| `calendar` | Calendar operations |
| `timedelta` | Do times ke beech ka **fark** (difference) |

### timedelta kab use hoga?
- Order place kiya — order deliver hua — kitna time laga?
- Program run hone mein kitna time laga?

---

## 3. Third-Party Date Libraries

Yeh built-in nahi hain — `pip install` karna padega:

```python
import arrow      # timezone conversion easy karta hai
import dateutil   # date parsing aur manipulation
```

### arrow — Example

```python
import arrow

brewing_time = arrow.utcnow()   # current UTC time

# Timezone convert karo
rome_time = brewing_time.to("Europe/Rome")
```

---

## 4. `collections` Module — Advanced Data Types

Python ka built-in module hai — import karna padta hai:

```python
from collections import namedtuple   # ya jo chahiye woh import karo
```

### Available Types in `collections`:

| Type | Kaam |
|---|---|
| `namedtuple` | Tuple jisme fields ka naam ho |
| `deque` | Double-ended queue (dek — "deck" nahi) |
| `Counter` | Items count karna |
| `OrderedDict` | Order maintain karne wala dict |
| `defaultdict` | Missing keys pe default value |
| `ChainMap` | Multiple dicts ko ek mein chain karna |

---

## 5. namedtuple — Example

```python
from collections import namedtuple

# Define karo — tuple ka naam aur fields
ChaiProfile = namedtuple("ChaiProfile", ["flavor", "aroma", "color"])

# Use karo
my_chai = ChaiProfile(flavor="spicy", aroma="strong", color="brown")
print(my_chai.flavor)   # spicy — naam se access karo, index se nahi
```

> Regular tuple mein `my_tuple[0]` karna padta — namedtuple mein `my_chai.flavor` — zyada readable

---

## Summary

| Category | Examples |
|---|---|
| Built-in modules | `datetime`, `time`, `calendar`, `timedelta` |
| Third-party | `arrow`, `dateutil` |
| `collections` module | `namedtuple`, `deque`, `Counter`, `OrderedDict` |

---

> 💡 **Abhi inhe deeply seekhne ki zaroorat nahi** — jab real use case aaye tab seekhna. Bas itna yaad rakho ki yeh exist karte hain!