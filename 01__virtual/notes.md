# Virtual Environment in Python — Ep. 1

---

## 1. Virtual Environment kya hai aur kyun chahiye?

Agar hum ek hi system pe multiple Python projects karte hain, toh har project ki dependencies alag ho sakti hain. Ek project ko library ka version 1.0 chahiye, doosre ko 2.0 — agar sab ek jagah install karein toh conflict hoga.

**Solution → Virtual Environment:**
- Har project ko apna alag Python environment milta hai
- Ek project ki dependencies doosre ko affect nahi karti
- Code kisi bhi machine pe easily run ho sakta hai

---

## 2. Traditional Way — `venv`

### Step 1 — Virtual Environment banao
```bash
# Mac/Linux
python3 -m venv .venv

# Windows
python -m venv .venv
```

### Step 2 — Activate karo
```bash
# Mac/Linux
source .venv/bin/activate

# Windows
.venv\Scripts\activate
```

Activate hone ke baad terminal mein `(.venv)` dikhega.

### Step 3 — Packages install karo
```bash
pip install flask
pip install requests
```

### Step 4 — Deactivate karo
```bash
deactivate
```

---

## 3. `requirements.txt` — Dependencies Share karna

```bash
# requirements.txt
flask
requests==3.0.0   # Specific version bhi de sakte ho
```

```bash
# Sab install karo ek baar mein
pip install -r requirements.txt
```

- Doosron ko sirf `requirements.txt` de do
- Woh apna virtual environment banayenge aur install kar lenge
- `.venv` folder GitHub pe push mat karo → `.gitignore` mein daalo

---

## 4. New Way — `uv` (Modern, Fast)

- `venv` se zyada fast aur powerful
- Aajkal kaafi popular ho raha hai
- Agli video mein detail mein dekhenge

---

## 5. Best Practice

> **Hamesha virtual environment mein kaam karo** — har project ke liye alag environment banao

---

## Next Video → `uv` tool + Project structure in Python

# Python Code Organization — Ep. 2

---

## 1. Project Structure — Basic Layout

```
chai_shop/          ← Top-level folder (project root)
├── run.py          ← App start karne wali file (main.py / index.py bhi chalega)
├── chai.py         ← Main functional code
├── utils/          ← Package (has __init__.py)
│   ├── __init__.py
│   └── helpers.py
└── processing/     ← Sirf folder (no __init__.py) — package nahi hai
    └── ml_model.py
```

---

## 2. Module vs Package — Important Difference

| | Module | Package |
|---|---|---|
| Kya hai | `.py` file | Folder with `__init__.py` |
| Example | `chai.py`, `run.py` | `utils/` folder |
| `__init__.py` | Nahi hota | **Zaroori** — empty bhi ho sakta hai |

```python
# Module → normal .py file
chai.py

# Package → folder + __init__.py
utils/
└── __init__.py   ← yeh file folder ko "package" banati hai
```

---

## 3. `__init__.py` — Kya hota hai?

- Aksar **empty** file hoti hai
- Sirf iske hone se folder ek Python **package** ban jaata hai
- Bina iske → sirf ek folder hai, package nahi

---

## 4. Namespace aur Scope — "Ghar" wala concept

```
City (Global scope)
├── Public park  → koi bhi access kar sakta hai
├── Ghar A       → andar ka saman sirf ghar wale use karein
│   ├── item1    ← sirf Ghar A ke log use karein
│   └── item2
└── Ghar B
    └── item3    ← Ghar A wale directly nahi le sakte
```

**Matlab:**
- Bahar ki cheez (global) → koi bhi access kar sakta hai ✅
- Kisi function/class ke andar ki cheez → sirf wahi access kar sakta hai ❌ (unless explicitly diya ho)

```python
x = 10  # Global — koi bhi use kar sakta hai

def ghar_a():
    y = 20  # Local — sirf ghar_a ke andar

def ghar_b():
    print(y)  # ❌ Error — y ghar_a ka andar ka hai
    print(x)  # ✅ OK — x global hai
```

---

## 5. Best Practices

- Entry point file ka naam → `main.py`, `run.py`, ya `app.py`
- Reusable helper code → `utils/` package mein rakho
- Har folder ko package banana zaroor nahi — sirf jab import karna ho
- Classes aur functions → `.py` module files mein rakho

---

## Next Video → uv tool (Modern Python environment manager)

# PEP 8 & Zen of Python — Ep. 3

---

## 1. PEP 8 kya hai?

Python ke creator ne ek style guide banaya hai — **PEP 8**. Yeh guide batati hai ki Python code properly kaise likhein taaki woh readable aur maintainable ho.

> Beginners ke liye zaroori nahi — lekin jaanna chahiye ki yeh exist karta hai. Comfortable hone ke baad padho.

---

## 2. PEP 8 — Key Rules

| Rule | Detail |
|---|---|
| Indentation | **4 spaces** use karo — tabs avoid karo |
| Naming | Meaningful names do (`chai` na ki `c1`) |
| Formatters | `black`, `ruff`, `flake8` — code auto-format karte hain |

---

## 3. Zen of Python — `import this`

Terminal mein Python open karo aur yeh type karo:

```python
python3   # Mac/Linux
python    # Windows

>>> import this
```

Output — Python ki philosophy:

```
Beautiful is better than ugly.
Explicit is better than implicit.
Simple is better than complex.
Complex is better than complicated.
Flat is better than nested.
...
```

**Core message:** Sabse achha code woh hota hai jo **sabse simple aur readable** ho — jise koi bhi padh ke samajh le.

---

## 4. "Pythonic" Code kya hai?

- Simple aur readable likho
- Unnecessary complexity avoid karo
- Python ki built-in features ka use karo
- PEP 8 follow karo

---

## Next Video → uv tool (Modern Python package manager)