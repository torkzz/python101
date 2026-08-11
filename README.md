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
