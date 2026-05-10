---
jupytext:
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

(label-matplotlib-inline)=
# `%matplotlib inline`

+++

de la bonne utilisation de `plt.figure()`, `plt.show()` en fonction du driver `%matplotlib` - épisode 1

+++

**take home message**

* c'est le mode par défaut
* plusieurs figures dans une cellule:  
  utiliser `plt.figure()` pour commencer une nouvelle figure  
  plutôt que `plt.show()` pour en terminer une

+++

***

```{code-cell} ipython3
# si on ne met rien c'est comme si on faisait
# %matplotlib inline
```

```{code-cell} ipython3
import matplotlib.pyplot as plt

# pour changer la taille des figures par défaut
plt.rcParams["figure.figsize"] = (4, 2)
```

## préparation

```{code-cell} ipython3
import numpy as np

X = np.linspace(0, 2*np.pi)
Y = np.sin(X)
Y2 = np.cos(X)
```

## un plot = une figure

```{code-cell} ipython3
:cell_style: split

# dans ce mode, pas besoin de créer une figure
plt.plot(X, Y);
```

```{code-cell} ipython3
:cell_style: split

plt.plot(X, Y2);
```

## plusieurs courbes

```{code-cell} ipython3
:cell_style: split

# et plusieurs courbes finissent
# dans la même figure
plt.plot(X, Y)
plt.plot(X, Y2);
```

```{code-cell} ipython3
:cell_style: split

# et si on veut mettre plusieurs
# graphiques différents
# on peut faire comme ceci
# qui fonctionne aussi avec le driver notebook
# plt.figure()     # le premier est toujours optionnel
plt.plot(X, Y)
plt.figure()
plt.plot(X, Y2);
```

```{code-cell} ipython3
:cell_style: split

# on aurait aussi pu utiliser plt.show()
# mais ça par contre ça ne marche pas
# avec le driver notebook
plt.plot(X, Y)
plt.show()
plt.plot(X, Y2);
# et le dernier n'est pas vraiment obligatoire
#plt.show()
```
