# 🧱 Object Oriented Programming (OOP) – Basics

---

## 📌 Introduction

* New section start → **Object Oriented Programming (OOP)**
* OOP ko **OOPS** bhi bolte hain
* Ye ek **programming paradigm** hai

---

## 🧠 What is Paradigm?

* Paradigm = code likhne ka ek **way / style**
* Different ways exist:

  * Object Oriented Programming
  * Functional Programming

---

## 📌 Important

* OOP C era ke baad evolve hua
* Bahut languages use karti hain:

  * Java
  * JavaScript
  * Kotlin
  * Swift

---

## 🧠 Reality

* Production code me:

  * OOP + Functional programming mix hota hai
* Koi right ya wrong nahi hai

---

## 🎯 Why Learn OOP?

* New data structures samajhne ke liye
* New terminologies:

  * polymorphism
  * abstraction

👉 Ye normal English words jaise hi meaning rakhte hain

---

# 🧠 Core Idea

👉 OOP = objects ke through programming

---

## ☑️ Example (Blueprint Concept)

* Ek **blueprint** banate hain
* Usse multiple copies create karte hain

---

## 🧠 Mapping

* Blueprint → **Class**
* Copies → **Objects**

---

## 📌 Important

* Objects:

  * independent hote hain
  * apni properties change kar sakte hain
* Changes class me reflect nahi hote

---

# 🧱 Class

---

## 🛠️ Syntax

```python id="a1k9mz"
class Chai:
    pass
```

---

## 🧠 Concept

* `class` → keyword
* Name capital letter se start hota hai
* `pass` → empty class

---

# 🔍 Type Check

```python id="p4d8xy"
print(type(Chai))
```

---

## 🧠 Output

* class type

---

## ❗ Important

* Python me sab kuch **object hota hai**
* Class bhi internally object hai

---

# 🧪 Creating Object

```python id="k7m2vx"
ginger_tea = Chai()
```

---

## 🧠 Concept

* Class se object create hota hai
* Ye instance hai class ka

---

# 🔍 Object Type

```python id="z2p8qn"
print(type(ginger_tea))
```

---

## 🧠 Output

* object of class Chai

---

# 🔁 isinstance Check

---

## 🛠️ Example

```python id="x2m9vx"
print(isinstance(ginger_tea, Chai))
```

---

## ▶️ Output

* True

---

## 🛠️ Another Class

```python id="n5k3rt"
class ChaiTime:
    pass
```

---

```python id="y8p2qs"
print(isinstance(ginger_tea, ChaiTime))
```

---

## ▶️ Output

* False

---

## 🧠 Concept

* Object belong karta hai specific class se
* Dusri class ka instance nahi hota

---

# 📌 Key Points

* OOP = programming paradigm
* Class = blueprint
* Object = instance
* Python me sab object hai
* Class bhi object hai
* Object class se banta hai
* `isinstance()` se check karte hain

---

# 🎯 Final Idea

* Class define karo
* Object create karo
* Objects independent hote hain

---

## 📎 Source

Based on transcript 


# 📦 Classes & Namespaces in Python

---

## 📌 Introduction

* Topic: **Classes & Namespaces**
* Same diagram use karke concept samjhaya gaya

---

# 🧠 Core Idea

* Ek class hoti hai
* Usse multiple objects bante hain

👉 Har object ke paas apni **properties** hoti hain

---

## 🧠 Properties Example

* Color
* Size
* Shape

👉 Real world example:

* T-shirt:

  * color
  * size
  * fit

---

## 📌 Important Observation

* Sab objects class se bante hain
* But:

  * har object ki properties different ho sakti hain
  * ek dusre ko affect nahi karti

---

# 🧠 Namespace Concept

👉 Definition:

* Har object apni **separate identity** rakhta hai

👉 Isko bolte hain:

* **Namespace**

---

## 📌 Meaning

* Object ke paas:

  * apni properties
  * apni values

👉 Ye dusre objects ko affect nahi karta

---

# 🛠️ Example Class

```python id="a1k9mz"
class SimpleChai:
    origin = "India"
```

---

## 🧠 Concept

* Class ke andar variables → **properties** kehlate hain

---

# 🖨️ Access Property

```python id="p4d8xy"
print(SimpleChai.origin)
```

---

## ▶️ Output

* India

---

# 🔁 Add New Property

```python id="k7m2vx"
SimpleChai.ishot = True
```

---

## 🖨️ Print

```python id="z2p8qn"
print(SimpleChai.ishot)
```

---

## ▶️ Output

* True

---

# 🧠 Concept

* Dot (`.`) se properties access hoti hain
* New properties dynamically add kar sakte hain

---

# 🧪 Creating Object

```python id="x2m9vx"
masala = SimpleChai()
```

---

## 🧠 Concept

* Object class se banta hai
* Class ki properties inherit karta hai

---

# 🖨️ Access via Object

```python id="n5k3rt"
print(masala.origin)
print(masala.ishot)
```

---

## ▶️ Output

* India
* True

---

# 🔄 Modify Object Property

```python id="y8p2qs"
masala.ishot = False
```

---

# 🧠 Important Observation

```python id="h9m2zx"
print(SimpleChai.ishot)   # class value
print(masala.ishot)       # object value
```

---

## ▶️ Output

* Class → True
* Object → False

---

## 🧠 Concept

* Object ka change:

  * class ko affect nahi karta

---

# 🔥 Key Insight

👉 Each object has its own namespace

* Object change ≠ class change
* Object change ≠ other object change

---

# 🔁 Add New Property to Object

```python id="q1w7dv"
masala.flavor = "Masala"
```

---

## 🖨️ Print

```python id="y4t8qs"
print(masala.flavor)
```

---

## 🧠 Concept

* Object me extra properties add kar sakte hain
* Ye class me exist nahi karti

---

# 📌 Key Points

* Class → blueprint
* Object → instance
* Properties → variables inside class
* Dot operator → access properties
* Namespace → object ki own identity
* Object changes:

  * class ko affect nahi karte
  * dusre objects ko affect nahi karte

---

# 🎯 Final Idea

* Objects independent hote hain
* Har object apni properties maintain karta hai
* Namespace concept isi independence ko define karta hai

---

## 📎 Source

Based on transcript 


# 🌑 Attribute Shadowing in Python

---

## 📌 Introduction

* Topic: **Attribute Shadowing**
* Naam fancy lagta hai
* But concept aur implementation easy hai

---

# 🧠 Attribute kya hota hai?

* Attribute = variable
* Jab variable:

  * class ya object ke andar hota hai

👉 Tab use **attribute** bolte hain

---

## 📌 Important

* Variable = attribute (context pe depend karta hai)
* Functionality same hoti hai

---

# 🧱 Example Class

```python id="a1k9mz"
class Chai:
    temperature = "hot"
    strength = "strong"
```

---

## 🧠 Concept

* `temperature`, `strength` → attributes hain

---

# 🧪 Object Create

```python id="p4d8xy"
cutting = Chai()
```

---

# 🖨️ Access Attribute

```python id="k7m2vx"
print(cutting.temperature)
```

---

## ▶️ Output

* hot

---

# 🔄 Change Attribute (Object Level)

```python id="z2p8qn"
cutting.temperature = "mild"
```

---

## 🖨️ Print

```python id="x2m9vx"
print(cutting.temperature)
```

---

## ▶️ Output

* mild

---

# 🔍 Class vs Object Check

```python id="n5k3rt"
print(Chai.temperature)
```

---

## ▶️ Output

* hot

---

## 🧠 Concept

* Object change:

  * class ko affect nahi karta

---

# 🌑 Shadowing Concept

👉 Object ka attribute:

* class attribute ko **override (shadow)** kar deta hai

---

## 🧠 Meaning

* Object ka value → priority
* Class ka value → fallback

---

# 🔁 Delete Object Attribute

```python id="y8p2qs"
del cutting.temperature
```

---

## 🖨️ Print Again

```python id="h9m2zx"
print(cutting.temperature)
```

---

## ▶️ Output

* hot

---

## 🧠 Concept

* Object attribute delete hone par:
  👉 class attribute use hota hai

---

# ⚠️ Important Case

---

## 🛠️ Add New Attribute (Object only)

```python id="q1w7dv"
cutting.cup = "small"
```

---

## 🖨️ Print

```python id="y4t8qs"
print(cutting.cup)
```

---

## ▶️ Output

* small

---

# ❌ Delete and Access

```python id="r3k9fs"
del cutting.cup
print(cutting.cup)
```

---

## ▶️ Output

* Attribute Error

---

## 🧠 Concept

* Agar attribute:

  * object me nahi hai
  * class me bhi nahi hai

👉 To error aata hai

---

# 🔥 Key Insight

* Object attribute → shadow karta hai class attribute
* Delete hone par:

  * class value use hoti hai (fallback)
* Agar fallback nahi hai:

  * error aata hai

---

# 📌 Key Points

* Attribute = variable inside class/object
* Object override kar sakta hai class value
* Delete karne par fallback hota hai
* Fallback nahi → error
* Shadowing = object attribute > class attribute

---

# 🎯 Final Idea

* Attribute shadowing:

  * object apni value use karta hai
  * class backup ki tarah kaam karti hai

---

## 📎 Source

Based on transcript 


# 🔑 Self Argument in Python (Methods)

---

## 📌 Introduction

* Topic: **self argument**
* Ab tak hum properties dekh rahe the
* Ab methods (functions inside class) dekhte hain

---

# 🧠 Method kya hota hai?

* Function jo class ke andar ho
  👉 Usse **method** bolte hain

---

## 📌 Important

* Function = method (context pe depend karta hai)
* Class ke andar → method

---

# 🧱 Example Class

```python id="a1k9mz"
class ChaiCup:
    size = 150
```

---

## 🧠 Concept

* `size` → property (milliliters me)

---

# 🔁 Method Create

```python id="p4d8xy"
def describe(self):
    return f"a {self.size} ML Chai Cup"
```

---

## 🧠 Important

* Har method me first argument → `self`
* Ye reference hota hai:

  * object ka
  * properties ka

---

## ❗ Important Rule

* Class ke andar kisi variable ko access karna ho →
  👉 `self.variable` use karna padega

---

# ❌ Wrong

```python id="k7m2vx"
return size
```

---

# ✔ Correct

```python id="z2p8qn"
return self.size
```

---

# 🧪 Object Create

```python id="x2m9vx"
cup = ChaiCup()
```

---

# 🖨️ Call Method

```python id="n5k3rt"
print(cup.describe())
```

---

## ▶️ Output

* a 150 ML Chai Cup

---

# 🧠 Concept

* Object method call karta hai
* `self` automatically pass hota hai

---

# ⚠️ Direct Class Call

```python id="y8p2qs"
ChaiCup.describe()
```

---

## ❌ Error

* Missing argument → self

---

## 🧠 Reason

* Class ko nahi pata:

  * kaunsa object call kar raha hai

---

# ✔ Fix

```python id="h9m2zx"
ChaiCup.describe(cup)
```

---

## 🧠 Concept

* Manually object pass karna padta hai
* Ye hi `self` ban jata hai

---

# 🔁 Multiple Objects

```python id="q1w7dv"
cup2 = ChaiCup()
cup2.size = 100
```

---

## 🖨️ Call

```python id="y4t8qs"
print(cup.describe())
print(cup2.describe())
```

---

## ▶️ Output

* 150 ML
* 100 ML

---

## 🧠 Concept

* Har object apna data use karta hai
* `self` correct object ko point karta hai

---

# 🔍 Important Idea

👉 `self`:

* Reference hota hai current object ka
* Method ko context deta hai

---

# 📌 Key Points

* Method = function inside class
* `self` = object reference
* `self.variable` se access karte hain
* Object call → auto self pass
* Class call → manually pass karna padta hai

---

# 🎯 Final Idea

* `self` bina method kaam nahi karega properly
* Ye batata hai:
  👉 kaunsa object method call kar raha hai

---

## 📎 Source

Based on transcript 


# ⚙️ **init** Constructor in Python

---

## 📌 Introduction

* Topic: **`__init__` function**
* Important aur interesting function hai
* Object create hote hi automatically call hota hai

---

# 🧠 Core Idea

* Jab object create hota hai:

  * usko initial values deni hoti hain

👉 Is process ko bolte hain:

* **Initialization**

---

## 📌 Terminology

* Initialization → init
* `__init__` → constructor

---

# 🧱 Constructor Concept

* Python me constructor:
  👉 `__init__` method se banta hai

---

## 🧠 Important

* Ye ek **reserved method** hai
* Name fix hota hai

```python
def __init__(self):
```

---

# 🛠️ Example Class

```python id="a1k9mz"
class ChaiOrder:

    def __init__(self, type_, size):
        self.type = type_
        self.size = size
```

---

## 🧠 Concept

* `type_` → chai type (argument)
* `size` → chai size

👉 Values assign ho rahi hain:

* `self.type = type_`
* `self.size = size`

---

## 📌 Important

* Variables directly create ho rahe hain constructor me
* Ye allowed hai

---

# 🔁 Method Example

```python id="p4d8xy"
def summary(self):
    return f"{self.size} ML of {self.type} chai"
```

---

## 🧠 Concept

* Object ki properties use ho rahi hain
* `self` se access ho raha hai

---

# 🧪 Object Creation

```python id="k7m2vx"
order = ChaiOrder("masala", 200)
```

---

## 🧠 Concept

* Arguments pass ho rahe hain
* Constructor automatically run hota hai

---

# 🖨️ Call Method

```python id="z2p8qn"
print(order.summary())
```

---

## ▶️ Output

* 200 ML of masala chai

---

# 🔁 Multiple Objects

```python id="x2m9vx"
order2 = ChaiOrder("ginger", 220)
print(order2.summary())
```

---

## ▶️ Output

* 220 ML of ginger chai

---

## 🧠 Concept

* Har object apni values rakhta hai
* Constructor har object ke liye run hota hai

---

# 🔍 Important Concept

* Object = instance of class
* Arguments → parameters me convert hote hain
* Values assign hoti hain properties me

---

# ⚠️ Special Case (type_)

👉 `type_` kyu use kiya?

* `type` Python me built-in function hai
* Isliye underscore use kiya

---

## 🧠 Concept

* Naming conflict avoid karne ke liye `_` use karte hain
* Production me common practice hai

---

# 📌 Key Points

* `__init__` = constructor
* Object create hote hi run hota hai
* Values initialize karta hai
* `self` se properties assign hoti hain
* Multiple objects → separate values
* `_` naming conflict avoid karta hai

---

# 🎯 Final Idea

* `__init__` object ko initial state deta hai
* Har object ke liye alag values set karta hai

---

## 📎 Source

Based on transcript 


# 🔗 Inheritance & Composition in Python

---

## 📌 Introduction

* Topic: **Inheritance + Composition**
* Inheritance commonly use hota hai
* Composition production me kaafi use hota hai

---

# 🧠 Inheritance Concept

👉 Real life analogy:

* Property inherit hoti hai
* Start from scratch nahi karna padta

👉 Same programming me:

* Ek class ka kaam reuse kar sakte hain

---

## 📌 Definition

* Ek class dusri class se:
  👉 properties + methods inherit karti hai

---

# 🧱 Base Class Example

```python id="a1k9mz"
class BaseChai:

    def __init__(self, type_):
        self.type = type_

    def prepare(self):
        print(f"preparing {self.type} chai....")
```

---

## 🧠 Concept

* Constructor → type assign karta hai
* Method → chai prepare karta hai

---

# 🔁 Inheritance Example

```python id="p4d8xy"
class MasalaChai(BaseChai):

    def add_spices(self):
        print("adding cardamom, ginger and cloves")
```

---

## 🧠 Concept

* Parent class → `BaseChai`
* Child class → `MasalaChai`
* Parent ke methods bhi milte hain

---

## 📌 Important

* Inheritance syntax:

```python id="k7m2vx"
class Child(Parent):
```

---

# 🔍 Key Observation

* Object of `MasalaChai`:

  * parent methods use kar sakta hai
  * own methods bhi use kar sakta hai

---

# 🧠 Composition Concept

👉 Definition:

* Class ke andar:
  👉 dusri class ka object use karna

---

## 📌 Important

* Inheritance ≠ Composition
* Composition = reference hold karna

---

# 🧱 Composition Example

```python id="z2p8qn"
class ChaiShop:

    def __init__(self):
        self.chai = BaseChai("regular")

    def serve(self):
        print(f"serving {self.chai.type} chai")
        self.chai.prepare()
```

---

## 🧠 Concept

* `self.chai` → object of BaseChai
* Methods access ho rahe hain

---

# 🔍 Observation

* `self.chai.type` → property access
* `self.chai.prepare()` → method call

---

# 🧠 Important Idea

* Composition me:

  * direct inheritance nahi hota
  * object reference use hota hai

---

# 🔁 Fancy Chai Shop

```python id="x2m9vx"
class FancyChaiShop(ChaiShop):
    pass
```

---

## 🧠 Concept

* Inheritance + Composition dono use ho rahe hain

---

# 🔍 Important Observation

* FancyChaiShop:

  * ChaiShop inherit karta hai
  * indirectly BaseChai access karta hai

---

# ⚠️ Important Issue

* Kabhi error aata hai:
  👉 missing `self` / context

---

## 🧠 Reason

* Method ko object context chahiye
* Direct call me context missing hota hai

---

## ✔ Fix

* Object create karke call karo

---

# 🔥 Key Insights

* Inheritance:

  * code reuse
  * parent → child

* Composition:

  * object reference
  * flexibility

* Constructor:

  * always involved hota hai

---

# 📌 Key Points

* `class Child(Parent)` → inheritance
* Parent methods automatically milte hain
* Composition me object use hota hai
* `self.object.method()` use hota hai
* Context important hai (`self`)
* Constructor always exist karta hai

---

# 🎯 Final Idea

* Inheritance → "is-a" relationship
* Composition → "has-a" relationship
* Dono combine hoke production code banta hai

---

## 📎 Source

Based on transcript 


# 🔁 Accessing Base Class in Python

---

## 📌 Introduction

* Topic: **Accessing Base Class**
* Inheritance ke saath use hota hai
* Important concept hai

---

# 🧠 Core Idea

👉 Base class ko access karne ke multiple ways hain:

1. Code Duplication
2. Explicit Call
3. super() method

---

## 📌 Important

* Koi single "right" way nahi hai
* Situation pe depend karta hai
* super() commonly use hota hai

---

# 🧱 Base Class Example

```python id="a1k9mz"
class Chai:

    def __init__(self, type_, strength):
        self.type = type_
        self.strength = strength
```

---

## 🧠 Concept

* `type_` → chai type
* `strength` → chai strength

---

# 🔁 Child Class (Code Duplication)

```python id="p4d8xy"
class GingerChai(Chai):

    def __init__(self, type_, strength, spice_level):
        self.type = type_
        self.strength = strength
        self.spice_level = spice_level
```

---

## 🧠 Concept

* Parent ka code repeat ho raha hai
* Ye hai **code duplication**

---

## ❗ Problem

* Code repetition
* Maintain karna difficult

---

# 🔁 Explicit Call

```python id="k7m2vx"
class GingerChai(Chai):

    def __init__(self, type_, strength, spice_level):
        Chai.__init__(self, type_, strength)
        self.spice_level = spice_level
```

---

## 🧠 Concept

* Direct parent constructor call kiya
* Parent ka logic reuse ho gaya

---

## 📌 Important

* Isko bolte hain **explicit call**
* Commonly use hota hai

---

# 🔁 Using super()

```python id="z2p8qn"
class GingerChai(Chai):

    def __init__(self, type_, strength, spice_level):
        super().__init__(type_, strength)
        self.spice_level = spice_level
```

---

## 🧠 Concept

* `super()` → base class ko refer karta hai
* Automatically parent constructor call karta hai

---

## 📌 Important

* Ye preferred approach hai
* Simple aur readable hai

---

# 🔍 Comparison

---

## 🧠 Code Duplication

* Same code repeat
* Not efficient

---

## 🧠 Explicit Call

* Parent constructor manually call
* Thoda verbose

---

## 🧠 super()

* Clean syntax
* Easy to use
* Most preferred

---

# ⚠️ Important Idea

* Constructor me extra parameters ho sakte hain
* Unko manually handle karna padta hai

---

# 📌 Key Points

* Base class access karne ke 3 ways:

  * Code duplication
  * Explicit call
  * super()
* super() most common hai
* Explicit call bhi valid hai
* Code duplication avoid karna chahiye

---

# 🎯 Final Idea

* Inheritance me:
  👉 base class ka constructor reuse karte hain

* Best practice:
  👉 `super()` use karo

---

## 📎 Source

Based on transcript 


# 🔁 Multiple Inheritance & MRO in Python

---

## 📌 Introduction

* Topic: **Multiple Inheritance**
* Ek class multiple classes se inherit kar sakti hai
* Zyada classes use karna prefer nahi hota
* 2 classes sufficient hoti hain

---

## ⚠️ Important

* Multiple inheritance kabhi-kabhi problems create karta hai

---

# 🧠 New Concept

👉 **Method Resolution Order (MRO)**

---

## 📌 Definition

* MRO decide karta hai:
  👉 method / attribute kaha se pick hoga

---

## 🧠 Important

* Fancy concept hai
* Beginners ke liye tough lag sakta hai
* Python me use hota hai (Python 2.3 se)
* Python 3 me bhi use hota hai

---

# 🧱 Example Structure

* Class A
* Class B → inherits A
* Class C → inherits A
* Class D → inherits B and C

---

## 🧠 Question

👉 Agar D me method call karein:

* B se aayega?
* C se aayega?
* A se aayega?

---

# 🛠️ Example Code

```python id="a1k9mz"
class A:
    label = "base class"
```

---

```python id="p4d8xy"
class B(A):
    label = "Masala Blend"
```

---

```python id="k7m2vx"
class C(A):
    label = "Herbal Blend"
```

---

```python id="z2p8qn"
class D(B, C):
    pass
```

---

# 🧪 Usage

```python id="x2m9vx"
cup = D()
print(cup.label)
```

---

## ▶️ Output

* Masala Blend

---

# 🧠 Concept

* D me label nahi hai
* B aur C dono me hai

👉 Python check karega:

* Pehle B
* Fir C
* Fir A

---

# 🔥 Important Rule

👉 **Left to right order matter karta hai**

* `class D(B, C)` → B first
* Isliye B ka method use hua

---

## 🔁 Swap Case

👉 Agar:

```python id="n5k3rt"
class D(C, B):
```

👉 Output:

* Herbal Blend

---

# 🧠 Trick

👉 First inherited class → priority

---

# 🔍 MRO Check

```python id="y8p2qs"
print(D.__mro__)
```

---

## 🧠 Output Structure

* D
* B / C (order based)
* A
* object

---

## 🧠 Concept

* Ye batata hai:
  👉 search order kya hai

---

# 📌 Key Points

* Multiple inheritance possible hai
* Order important hota hai
* MRO decide karta hai:

  * method kaha se aayega
* Left to right priority hoti hai
* `__mro__` se check kar sakte hain

---

# 🎯 Final Idea

* Python method search karta hai:
  👉 defined order me

* Order change → result change

---

## 📎 Source

Based on transcript 


# ⚙️ Static Methods in Python

---

## 📌 Introduction

* Topic: **Static Methods**
* Easy aur fun concept hai
* Utility functions ke liye use hota hai

---

## 🧠 Core Idea

* Static methods:
  👉 class ke andar hote hain
  👉 but object pe depend nahi karte

---

## 📌 Use Case

* Utility functions ko class ke andar group karna
* Without depending on instance

---

# 🧱 Example Class

```python id="a1k9mz"
class ChaiUtils:
```

---

# 🛠️ Method Example

```python id="p4d8xy"
def clean_ingredients(text):
```

---

## 🧠 Concept

* Input: text string
* Work:

  * comma se split karna
  * spaces remove karna

---

# 🔁 Logic

```python id="k7m2vx"
[item.strip() for item in text.split(",")]
```

---

## 🧠 Concept

* `split(",")` → comma ke basis pe divide
* `strip()` → extra spaces remove

---

# 📊 Example Input

```python id="z2p8qn"
" water , milk , ginger , honey "
```

---

## 🧠 Output

* water
* milk
* ginger
* honey

---

# 🔁 Normal Method Use

```python id="x2m9vx"
obj = ChaiUtils()
obj.clean_ingredients(raw)
```

---

## 🧠 Concept

* Object create karna padta hai
* Fir method call hota hai

---

# ⚡ Static Method Use

```python id="n5k3rt"
@staticmethod
def clean_ingredients(text):
```

---

## 🧠 Concept

* Decorator use hota hai
* Method object pe depend nahi karta

---

# ▶️ Call Without Object

```python id="y8p2qs"
ChaiUtils.clean_ingredients(raw)
```

---

## 🧠 Concept

* Direct class se call kar sakte hain
* Object ki zarurat nahi

---

# 🔍 Observation

* Same functionality
* But cleaner approach

---

# 📌 Important Points

* Static method:

  * object pe depend nahi karta
* `@staticmethod` decorator use hota hai
* Direct class se call kar sakte hain
* Utility functions ke liye best hai

---

# 🧠 Final Idea

* Agar method:

  * object data use nahi karta
    👉 to static method bana do

---

# ⚠️ Important

* Decorator use karna mat bhoolna
* Warna method normal method treat hoga

---

## 📎 Source

Based on transcript 


# 🏗️ Class Methods in Python

---

## 📌 Introduction

* Static methods dekhe the last video me
* Ab baat karenge **Class Methods** ki
* Static methods initialization ke liye useful nahi hote

---

# 🧠 Problem

* Python me:
  👉 sirf **1 constructor (`__init__`)** hota hai

👉 Multiple constructors directly possible nahi

---

## 🧠 Goal

* Different ways se object create karna:

  * Direct values
  * Dictionary
  * String

---

# 🧱 Example Class

```python id="a1k9mz"
class ChaiOrder:

    def __init__(self, tea_type, sweetness, size):
        self.tea_type = tea_type
        self.sweetness = sweetness
        self.size = size
```

---

## 🧠 Concept

* Constructor values assign karta hai
* Standard object creation

---

# 🔁 Class Method (Dictionary Input)

```python id="p4d8xy"
@classmethod
def from_dict(cls, order_data):
    return cls(
        order_data["tea_type"],
        order_data["sweetness"],
        order_data["size"]
    )
```

---

## 🧠 Concept

* `cls` → class reference
* `cls(...)` → constructor call
* Dictionary se values extract ho rahi hain

---

# 🔁 Class Method (String Input)

```python id="k7m2vx"
@classmethod
def from_string(cls, order_str):
    tea_type, sweetness, size = order_str.split("-")
    return cls(tea_type, sweetness, size)
```

---

## 🧠 Concept

* String split ho rahi hai
* Values assign ho rahi hain
* Constructor call ho raha hai

---

# 🧪 Object Creation

---

## 📦 From Dictionary

```python id="z2p8qn"
order1 = ChaiOrder.from_dict({
    "tea_type": "masala",
    "sweetness": "medium",
    "size": "large"
})
```

---

## 📦 From String

```python id="x2m9vx"
order2 = ChaiOrder.from_string("ginger-low-small")
```

---

## 📦 Normal Constructor

```python id="n5k3rt"
order3 = ChaiOrder("black", "low", "large")
```

---

# 🧠 Concept

* 3 ways se object create ho raha hai
* But actual constructor same hi hai

---

# 🔍 **dict** Usage

```python id="y8p2qs"
print(order1.__dict__)
```

---

## 🧠 Output

* Object ke saare attributes dictionary form me milte hain

---

# ⚡ Static Method Comparison

```python id="h9m2zx"
@staticmethod
def is_valid_size(size):
    return size in ["small", "medium", "large"]
```

---

## 🧠 Concept

* Static method:

  * class ya object pe depend nahi
  * utility function hai

---

# 🔍 Usage

```python id="q1w7dv"
ChaiUtils.is_valid_size("medium")
```

---

# 🔥 Difference (Important)

---

## 🧠 Class Method

* `cls` use hota hai
* Class pe operate karta hai
* Object create kar sakta hai

---

## 🧠 Static Method

* `self` / `cls` nahi hota
* Independent utility function
* Object create nahi karta

---

# 📌 Key Points

* Python me 1 constructor hota hai
* Class method → multiple creation ways deta hai
* `@classmethod` decorator use hota hai
* `cls` = class reference
* Static method → utility functions
* `__dict__` → object data show karta hai

---

# 🎯 Final Idea

* Class method:
  👉 constructor ko control karta hai

* Static method:
  👉 helper utility hota hai

---

## 📎 Source

Based on transcript 


# 🏷️ Property Decorators in Python

---

## 📌 Introduction

* Topic: **Property Decorators**
* Purpose: properties ko control karna

---

# 🧠 Problem

* Normal property:

  * koi bhi read kar sakta hai
  * koi bhi update kar sakta hai

👉 Example:

* age = -10 bhi set ho sakta hai (invalid)

---

# 🎯 Goal

* Property ko control karna:

  * kaise read ho
  * kaise update ho

---

# 🧱 Example Class

```python id="a1k9mz"
class TeaLeaf:

    def __init__(self, age):
        self._age = age
```

---

## 🧠 Concept

* `_age`:

  * underscore → special meaning
  * directly access nahi karna chahiye

---

# 🔁 Getter (Read Control)

```python id="p4d8xy"
@property
def age(self):
    return self._age + 2
```

---

## 🧠 Concept

* `@property`:

  * method ko property bana deta hai
* Value read karte waqt modify ho sakti hai

---

# 🔁 Setter (Write Control)

```python id="k7m2vx"
@age.setter
def age(self, value):
    if 1 <= value <= 5:
        self._age = value
    else:
        raise ValueError("Tea leaf age must be between 1 and 5 years")
```

---

## 🧠 Concept

* Setter:

  * value set karte waqt validation
* Invalid value → error

---

# 🧪 Usage

```python id="z2p8qn"
leaf = TeaLeaf(2)
print(leaf.age)
```

---

## ▶️ Output

* 4

---

## 🧠 Concept

* Actual value = 2
* Getter → +2 add kar raha hai

---

# 🔁 Update Value

```python id="x2m9vx"
leaf.age = 4
print(leaf.age)
```

---

## ▶️ Output

* 6

---

## 🧠 Concept

* Setter accept karta hai (valid range)
* Getter modify karke return karta hai

---

# ❌ Invalid Case

```python id="n5k3rt"
leaf.age = 6
```

---

## ▶️ Output

* ValueError

---

## 🧠 Concept

* Setter validation fail → error throw

---

# 🔍 Important Insight

* Property call aise hota hai:

  ```python
  leaf.age
  ```
* But internally:
  👉 method call ho raha hota hai

---

# 🧠 Key Terms

* Getter → value read control
* Setter → value write control
* Property → dono ko combine karta hai

---

# 📌 Important Notes

* `_age` → internal variable
* `age` → controlled access
* Getter & setter same name use karte hain
* Validation possible hai
* Error handling possible hai

---

# 🎯 Final Idea

* Property decorators:
  👉 data access control karte hain

* Direct access ke bajaye:
  👉 controlled access use hota hai

---

## 📎 Source

Based on transcript 
