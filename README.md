# python101
# How to Import Built-in Modules

There are **4 common ways** to import something from Python's `math` module.

### 1. Import the whole module

```python
import math

print(math.pi)
```

Output:

```text
3.141592653589793
```

You access things using:

```python
math.pi
math.sqrt()
math.floor()
```

---

### 2. Import with an alias

```python
import math as m

print(m.sqrt(25))
print(m.pi)
```

Output:

```text
5.0
3.141592653589793
```

`m` is simply a shorter name for `math`.

So:

```python
math.sqrt(25)
```

becomes:

```python
m.sqrt(25)
```

---

### 3. Import specific functions/variables

```python
from math import sqrt, pi

print(sqrt(49))
print(pi)
```

Output:

```text
7.0
3.141592653589793
```

Now you **don't need**:

```python# python101

math.sqrt()
math.pi
```

because you imported `sqrt` and `pi` directly.

---

### 4. Import everything

```python
from math import *

print(sqrt(36))
print(pi)
```

Output:

```text
6.0
3.141592653589793
```

The `*` means:

> Import everything from the module.

⚠️ **Generally avoid `from math import *`** in real projects because it can make it unclear where names came from and can cause naming conflicts.

---

## 🧠 The main difference

Think of `math` as a **toolbox**:

```text
math
├── pi
├── sqrt()
├── floor()
├── ceil()
├── sin()
└── cos()
```

### Whole toolbox

```python
import math

math.sqrt(25)
```

### Toolbox with nickname

```python
import math as m

m.sqrt(25)
```

### Take only specific tools

```python
from math import sqrt

sqrt(25)
```

### Take everything out of the toolbox

```python
from math import *

sqrt(25)
pi
```

For your current lesson, I'd remember these three first:

```python
import math
math.sqrt(25)
```

```python
import math as m
m.sqrt(25)
```

```python
from math import sqrt
sqrt(25)
```

These are the patterns you'll use most often.



### Virtual Environment — simplified explanation

A **virtual environment (`venv`)** is an isolated Python environment created for a specific project.

Think of it like this:

```text
System Python
│
├── Project A
│   └── venv
│       └── requests 2.31
│
├── Project B
│   └── venv
│       └── requests 2.32
│
└── Project C
    └── venv
        └── requests 2.28
```

Each project can have its **own Python dependencies and versions** without interfering with the others.

### Why use it?

Without a virtual environment:

```text
Project A ──┐
            ├── System Python ── package conflicts ❌
Project B ──┘
```

With virtual environments:

```text
Project A ──> venv A ──> dependencies A
Project B ──> venv B ──> dependencies B
Project C ──> venv C ──> dependencies C
```

So your drawing is essentially showing:

> **One project → one isolated environment → its own package/version set.**

### Create one

```bash
python -m venv .venv
```

Activate it on Linux/macOS:

```bash
source .venv/bin/activate
```

Then:

```bash
pip install requests
```

That `requests` installation belongs to **that project's `.venv`**, rather than being installed globally. 🔒

To leave the environment:

```bash
deactivate
```

**Important distinction:** a `venv` does not completely virtualize the operating system. It primarily isolates the **Python interpreter environment and installed Python packages**.
This slide is showing **Step 2: Create the virtual environment**.

### Command

On Windows, from inside your project folder:

```bash
python -m venv .venv
```

For example:

```text
C:\Users\Kevin Paul\Desktop\PyProject>python -m venv .venv
```

### What each part means

```text
python
  ↓
Run Python

-m
  ↓
Run a Python module

venv
  ↓
Use Python's built-in virtual-environment module

.venv
  ↓
Create the virtual environment in a folder named .venv
```

So:

```bash
python -m venv .venv
```

essentially means:

> **"Python, use the `venv` module to create an isolated Python environment inside `.venv`."**

### What gets created?

After running it, you'll typically see:

```text
PyProject/
├── .venv/
│   ├── Include/
│   ├── Lib/
│   ├── Scripts/
│   └── pyvenv.cfg
│
└── your_python_files.py
```

On **Windows**, the important executable is:

```text
.venv\Scripts\python.exe
```

and the activation script is:

```text
.venv\Scripts\activate
```

### Next step: activate it

In **Windows CMD**:

```cmd
.venv\Scripts\activate
```

In **PowerShell**:

```powershell
.venv\Scripts\Activate.ps1
```

After activation, you'll normally see:

```text
(.venv) C:\Users\Kevin Paul\Desktop\PyProject>
```

Now `pip install ...` installs packages into **this project's environment**, rather than the global Python installation. 🔒
