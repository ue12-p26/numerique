---
jupytext:
  encoding: '# -*- coding: utf-8 -*-'
  text_representation:
    extension: .md
    format_name: myst
kernelspec:
  display_name: Python 3 (ipykernel)
  language: python
  name: python3
language_info:
  name: python
  nbconvert_exporter: python
  pygments_lexer: ipython3
---

# instructions

+++

Certaines de ces instructions seront décrites dans le notebook sur les itérations.

+++

## le branchement `if`

+++ {"cell_style": "split"}

forme générale

```python
if exp1:
    ...
    ...
elif exp2:
    ...
    ...
else:
    ...
    ...
```

```{code-cell} ipython3
:cell_style: split

note = 14
appreciation = None

if note >= 16:
    appreciation = 'félicitations'
elif note >= 10:
    appreciation = 'reçu'
else:
    appreciation = 'recalé'
```

```{code-cell} ipython3
appreciation
```

+++ {"cell_style": "split"}

## la boucle `while`

forme générale  

```python
while exp:
    ...
    ...
```

```{code-cell} ipython3
:cell_style: split

n = 132
log = 0

while n >= 1:
    log = log + 1
    n = n // 2
```

```{code-cell} ipython3
:cell_style: split

log
```

## `for`, `break` et `continue`

+++

voir le notebook sur les `iterations`

+++

## `try`, `raise` et `except`

+++

voir le notebook sur les `fonctions`
