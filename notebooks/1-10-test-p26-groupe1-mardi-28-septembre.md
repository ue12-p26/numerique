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
  pygments_lexer: ipython3
  nbconvert_exporter: python
---

# Test de niveau `numpy`

```{code-cell} ipython3
import numpy as np
from matplotlib import pyplot as plt
```

+++ {"tags": ["framed_cell"]}

1. créez un tableau `tab1` de 30 valeurs espacées de 1 entre -15, 15  
   (borne supérieure non comprise)

    - affichez la forme du tableau
    - affichez le type des éléments
    - affichez la dimension du tableau
    - Sur combien d'octets est codé un élément de ce tableau ?

```{code-cell} ipython3
# votre code
```

```{code-cell} ipython3
f = -15
t = 15
s = 1
tab1 = np.arange(f, t, s)
tab1
```

```{code-cell} ipython3
tab1.shape
```

```{code-cell} ipython3
tab1.dtype
```

```{code-cell} ipython3
# 8 octets
```

+++ {"tags": ["framed_cell"]}

2. à partir de ce tableau, créez un tableau `tab2`
   dont le type des éléments est le plus petit type entier sans conversion
    - Les deux tableaux partagent-ils l'espace créé en mémoire ? Montrez-le !
    - Est-il possible de modifier la taille des éléments d'un tableau existant ?
    - Essayez d'ajouter `200` à une case de `tab2`. Que se passe-t-il ? Pourquoi ?

```{code-cell} ipython3
# votre code
```

```{code-cell} ipython3
tab2 = tab1.astype(dtype=np.int8)
tab2
```

```{code-cell} ipython3
# non
print(tab1[0], tab2[0])
tab1[0] = 2000
print(tab1[0], tab2[0])
```

```{code-cell} ipython3
# non
```

```{code-cell} ipython3
# on ne peut pas faire des opérations avec des valeurs en dehors du type du tableau
try:
    tab2[0] + 200
except OverflowError as e:
    print(e)
```

+++ {"tags": ["framed_cell"]}

3. montrez que les tableaux `tab1` et `tab2` contiennent bien les mêmes valeurs

```{code-cell} ipython3
# votre code
```

```{code-cell} ipython3
np.all(tab1 == tab2)
```

+++ {"tags": ["framed_cell"]}

4. créez `f1` un tableau de 100 floats linéairement distribués entre -`pi` et `pi`  
   le type des éléments doit être des floats sur 32 bits       
   - Redimentionnez ce tableau pour créer un nouveau tableau `f2` de taille `(4, 25)`  
     (sans que la forme de `f1` soit modifiée)
   - `f1` et `f2` partagent-ils l'espace créé en mémoire ?
   - appliquez la fonction `sinus`

```{code-cell} ipython3
# votre code
```

```{code-cell} ipython3
f1 = np.linspace(-np.pi, np.pi, 100, dtype=np.float32)
f2 = f1.reshape((4, 25))
# ou laisser numpy calculer la "bonne" taille
f2 = f1.reshape((4, -1))
```

```{code-cell} ipython3
f1.dtype
```

```{code-cell} ipython3
f1.base is f2.base
```

+++ {"tags": ["framed_cell"]}

5. écrivez la fonction `relu`:
    * qui prend un argument et retourne la valeur de l'argument si il est positif sinon 0
    - appliquez cette fonction à `tab1`
    - Y-a-t-il un problème ?
    - Si oui expliquez pourquoi ?
    - Corrigez-le ?

```{code-cell} ipython3
# votre code
```

```{code-cell} ipython3
def relu1 (x):
    if x > 0:
        return x
    return 0
```

```{code-cell} ipython3
try:
    relu1(tab1)
except ValueError as e:
    print(e)
```

```{code-cell} ipython3
# sans décorateur
def relu (x):
    if x > 0:
        return x
    return 0

relu = np.vectorize(relu)
```

```{code-cell} ipython3
# avec décorateur - plus "python"
@np.vectorize
def relu (x):
    if x > 0:
        return x
    return 0
```

```{code-cell} ipython3
relu(tab1)
```

+++ {"tags": ["framed_cell"]}

6. créez un tableau `tab3` des 30 premiers entiers pairs à partir de 2  
   en lui donnant la forme `(5, 6)`
   * transformez ce tableau **sans boucle for** en le tableau:
```
array([[   2,    4,    6,    8,   10,   12],
       [  14, 1600, 1800, 2000, 2200,   24],
       [  26, 2800, 3000, 3200, 3400,   36],
       [  38, 4000, 4200, 4400, 4600,   48],
       [  50,   52,   54,   56,   58,   60]])
```

```{code-cell} ipython3
tab3 = np.arange(2, 62, 2).reshape(5, 6)
tab3[1:-1, 1:-1] = 100*tab3[1:-1, 1:-1]
tab3
```

+++ {"tags": ["framed_cell"]}

7. créez le tableau `tab4` suivant **sans boucle for** pour un tuple `(l, c)` d'entiers positifs quelconques  
```
array([[0, 1, 2, 3],
       [1, 2, 3, 4],
       [2, 3, 4, 5],
       [3, 4, 5, 6],
       [4, 5, 6, 7],
       [5, 6, 7, 8]])
```
   * bonus : et celui-là ? (de nom de variable `tab5`)
```
array([[ 0,  3,  6,  9],
       [ 2,  5,  8, 11],
       [ 4,  7, 10, 13],
       [ 6,  9, 12, 15],
       [ 8, 11, 14, 17],
       [10, 13, 16, 19]])
```
hint: utilisez `np.indices`  
que vous avez dû voir lors des révisions

```{code-cell} ipython3
l, c = 6, 4
I, J = np.indices((l, c))
tab4 = I + J
tab5 = 2*I + 3*J
```

+++ {"tags": ["framed_cell"]}

8. Faites un tableau `tab6` des 120 entiers entre `-60` et `60`
   * faites une division entière par `3` de tous les entiers multiples de 3 entre `-20` et `20` bornes comprises

```{code-cell} ipython3
tab6 = np.arange(-60, 60)
tab6[(tab6 >= -20) & (tab6 <= 20) & (tab6%3==0)] // 3
```

+++ {"tags": ["framed_cell"]}

9. créez:
     * à partir de la liste Python `[1, 2, 3, 4, 5]` créez un tableau `t1` de 1 ligne et 5 colonnes
     * à partir de la liste Python `[10, 20, 30, 40]` créez un tableau `t2` de 4 lignes et 1 colonnes
     * ajoutez-les
     * que constatez vous ?

```{code-cell} ipython3
:scrolled: true

t1 = np.array([1, 2, 3, 4, 5]).reshape((1, 5))
t2 = np.array([10, 20, 30, 40]).reshape((4, 1))
t1 + t2
```

+++ {"tags": ["framed_cell"]}

10. faites un tableau de `0` à `120` (non compris)   
    de forme `(2, 3, 4, 5)`
    * sélectionnez les lignes des secondes matrices
    * multipliez les par 100

```{code-cell} ipython3
tab6 = np.arange(0, 120).reshape((2, 3, 4, 5))
tab6[:, 1, :, :] = tab6[:, 1, :, :]*100
```

```{code-cell} ipython3
(tab6 > 0)
```

```{code-cell} ipython3

```

```{code-cell} ipython3

```

```{code-cell} ipython3

```

*end*
