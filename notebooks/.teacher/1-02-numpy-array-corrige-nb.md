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

# les tableaux

+++

## contenu de ce notebook (sauter si déjà acquis)

````{admonition} fonctions de création de tableaux numpy

| les fonctions | ce qu'elles font |
|-:|-|
| `np.array` | renvoie la version ndarray d'un tableau existant |
| `np.empty` | renvoie un ndarray vide (éléments non initialisés) |
| `np.zeros` | renvoie un ndarray rempli de *0.* (float) |
| `np.ones` | renvoie un ndarray rempli de *1.* (float) |
| `numpy.arange` | tableau de valeurs régulièrement espacées|
| `np.linspace` | un vecteur de valeurs bien espacées entre deux bornes |
| `np.random.randint` | entiers aléatoirement générés |
| `np.random.randn` | flottants aléatoirement générés |
````

````{admonition} attributs/méthodes de manipulation de tableaux numpy

| attributs/méthodes | ce qu'ils font |
|-:|-|
| `np.ndarray.shape`    | la forme du tableau (tuple) |
| `np.ndarray.size`     | le nombre d'éléments du tableau |
| `np.ndarray.ndim`     | le nombre de dimensions du tableau |
| `np.ndarray.dtype`    | le type des éléments |
| `np.ndarray.itemsize` | la taille en octet d'un élément |
| `np.ndarray.nbytes`   | la taille totale du tableau sous-jacent en octet |
| `np.ndarray.astype`   | copie tableau avec autre type pour les éléments |
````


la taille (en nombre d'octets) des éléments d'un `numpy.ndarray` existant est constante  
une modification peut causer une conversion de la valeur ou une erreur


calculs de temps d'exécution avec `%timeit`

+++ {"tags": ["framed_cell"]}

## rappels

````{admonition} →

Python ne possède pas, de base, de type adapté aux tableaux multi-dimensionnels


ceux-ci sont proposés par la librairie numérique `numpy`  
qu'il faut installer séparément (`pip install numpy` dans le terminal)
````

```{code-cell} ipython3
import numpy as np
```

+++ {"tags": ["framed_cell"]}

## tableaux  multi-dimensionnels `numpy`

````{admonition} →

créés par la méthode `numpy.array`  
(ici plus précisément `np.array` comme l'identifiant utilisé lors de l'import est `np` mais on reste genéral)


leur type est `numpy.ndarray` (tableau en dimension n)

attributs et méthodes que nous allons utiliser souvent

| nom                      | comportement                                     |
|-------------------------:|--------------------------------------------------|
| `numpy.ndarray.shape`    | la forme du tableau (tuple)                      |
| `numpy.ndarray.dtype`    | le type des éléments                             |
| `numpy.ndarray.astype`   | crée tableau avec nouveau type d'éléments        |


ou moins souvent

| nom                      | comportement                                     |
|-------------------------:|--------------------------------------------------|
| `numpy.ndarray.ndim`     | le nombre de dimensions du tableau               |
| `numpy.ndarray.itemsize` | la taille en octet d'un élément                  |
| `numpy.ndarray.nbytes`   | la taille totale du tableau sous-jacent en octets |
````

+++

***

+++ {"tags": ["framed_cell"]}

### création d'un tableau multi-dimensionnel

````{admonition} →
reprenons notre matrice en Python brut

```python
matrice = [
    [1, 2, 3, 4, 5],
    [6, 7, 8, 9, 10],
    [11, 12, 13, 14, 15],
    [16, 17, 18, 19, 20]
]
```


avec la fonction `numpy.array` nous créons un tableau multi-dimensionnel initialisé avec notre matrice

```python
mat = np.array(matrice)
```


nous n'avons indiqué

* ni la forme du tableau
* ni le type des éléments

`numpy.array` a tout déduit

**type** de `mat` est `numpy.ndarray` i.e. *n-dimensional-array*

```python
type(mat)
    -> <class 'numpy.ndarray'>
```
````

+++

le code

```{code-cell} ipython3
matrice = [
    [1, 2, 3, 4, 5],
    [6, 7, 8, 9, 10],
    [11, 12, 13, 14, 15],
    [16, 17, 18, 19, 20]
]

mat = np.array(matrice)

print(mat)

print(type(mat))
```

+++ {"tags": ["framed_cell"]}

###  type et taille mémoire des éléments du tableau

````{admonition} →
```python
matrice = [
    [1, 2, 3],
    [4, 5, 6]
]
mat = np.array(matrice)
```

l'attribut `numpy.ndarray.dtype` donne le **type des éléments** du tableau

```python

mat.dtype
-> dtype('int64')
```
ou bien
```python

mat.dtype
-> dtype('int32')
```

tous les éléments sont du même type et de la même taille  
(ici des entiers signés codés sur 64 bits = 8 octets ou bien 32 bits = 4 octets)


l'attribut `numpy.ndarray.itemsize` donne le nombre d'octets d'un élément du tableau

```python
mat.itemsize
-> 8 # chaque élément fait 8 octets dans le cas int64
```


l'attribut `numpy.ndarray.nbytes`  donne le nombre d'octets total du tableau

```python
mat.nbytes
-> 48 # 6 éléments de 8 octets chacun dans le cas int64
```
````

```{code-cell} ipython3
# le code
matrice = [
    [1, 2, 3],
    [4, 5, 6]
]
mat = np.array(matrice)
mat.dtype, mat.itemsize, mat.nbytes
```

+++ {"tags": ["framed_cell"]}

### taille, forme, dimension du tableau

````{admonition} →
```python
matrice = [
    [1, 2, 3],
    [4, 5, 6]
]
mat = np.array(matrice)
```

l'attribut `numpy.ndarray.shape` donne la forme d'un tableau sous la forme d'un tuple

```python
mat.shape
-> (2, 3) # 2 lignes et 3 colonnes
```




l'attribut `numpy.ndarray.size` donne le nombre d'éléments du tableau

```python

mat.size # mat.shape[0] * mat.shape[1]
-> 6
```


l'attribut `numpy.ndarray.ndim` donne la dimension d'un tableau

```python
mat.ndim # len(mat.shape)
-> 2
```
````

```{code-cell} ipython3
# le code
print(mat.shape)
print(mat.size, mat.shape[0] * mat.shape[1])
print(mat.ndim, len(mat.shape))
```

+++ {"tags": ["framed_cell"]}

### création d'un tableau avec le type des éléments

````{admonition} →
on peut laisser `numpy` décider du type des éléments

```python
matrice = [
    [-128, -78, -32],
    [17, 5, 127]
]
mat = np.array(matrice)
mat.dtype
-> int64
```


calculons l'élément minimum et l'élément maximum d'un tableau

```python
mat.min(), mat.max()
-> -128 127
```


Combien faut-il d'octets, au minimum, pour stocker des entiers entre `-128` et `127` ?  
un seul octet


Quel type d'entier dois-je utiliser ?


**rappel avec n bits**, on représente $2^n$ valeurs entières
- soit des entiers signés $\in [ -2^{n-1}$, $2^{n-1}-1]$
- soit des entiers non signés $\in [0, 2^n-1]$




on peut donc utiliser le type  

* `numpy.int8` pour le type des entiers signés sur 8 bits  
  `256` valeurs de `-128` à `127`

* le type correspondant sera `numpy.int8` (entier signé sur 8 bits)



avec le paramètre `dtype` on indique, à la fonction `numpy.array`, le type des éléments

```python
matrice = [
    [-128, -78, -32],
    [17, 5, 127]
]
mat = np.array(matrice, dtype=np.int8)
mat.dtype
-> int8
```


**trompons-nous** et demandons un type `numpy.uint8`  
- ancienne librairie `numpy` vous obéit et,  
si elle rencontre un problème avec une valeur: elle modifie la valeur !

```python
mat = np.array(matrice, dtype=np.uint8)
mat
-> [[128, 178, 224], # ouh là là ! 128 = 256 - 128
                     # (complément à 2)
    [ 17,   5, 127]], dtype=uint8
```
- nouvelle librairie `numpy`  
   la conversion implicite n'est plus effectuée: le code échoue
````

```{code-cell} ipython3
# le code
matrice = [
    [-128, -78, -32],
    [17, 5, 127]
]
mat = np.array(matrice)

print(mat.min(), mat.max())
print(mat.dtype)
```

```{code-cell} ipython3
# le code avec type
matrice = [
    [-128, -78, -32],
    [17, 5, 127]
]
mat = np.array(matrice, dtype=np.int8)
mat
```

```{code-cell} ipython3
# le code avec erreur
matrice = [
    [-128, -78, -32],
    [17, 5, 127]
]
try:
    mat = np.array(matrice, dtype=np.uint8)
    # soit affichage du tableau avec les négatifs convertis implicitement par complément à 2
    # soit échec: "Python integer -128 out of bounds for uint8"
    mat
except OverflowError as e:
    print(e)
```

**exercice**

1. créez un tableau pour stocker la matrice ci-dessous avec le plus petit type entier non signé

```python
l = [[  0,   8,  34,   8],
     [255,  61, 128, 254]]
```

```{code-cell} ipython3
# votre code ici
```

```{code-cell} ipython3
:tags: [raises-exception]

# prune-cell
l = [[  0,   8,  34,   8],
     [255,  61, 128, 254]]
print(    np.array(l, dtype=np.uint8)    )

print(    np.array(l, dtype=np.int8)    )
# note that new version of NumPy "will stop allowing conversion of out-of-bound Python integers to integer arrays.
# The conversion of -128 to uint8 will fail in the future."
```

+++ {"tags": ["framed_cell"]}

### modifier le type des éléments d'un tableau existant

````{admonition} →
la méthode `numpy.ndarray.astype` crée un nouveau tableau de la même forme que le tableau initial  
avec la taille indiquée pour les éléments

```python
l = [[  0,   8,  34,   8],
     [255,  61, 128, 254]]

mat = np.array(l)
mat1 = mat.astype(np.int8)
mat1
```


`mat` et `mat1` ne partagent **pas** le tableau d'éléments sous-jacent  
`mat1` est **une copie indépendante** avec la nouvelle taille et les éventuelles conversions  
l'ancien `mat` existe toujours avec sa taille initiale
````

```{code-cell} ipython3
# le code
l = [[  0,   8,  34,   8],
     [255,  61, 128, 254]]

mat = np.array(l)
print(    mat     )
mat1 = mat.astype(np.int8) # des conversions sont effectuées
print(    mat1    )
print(    mat     )
```

+++ {"tags": ["framed_cell"]}

## `numpy` calcule à taille constante

````{admonition} →
créons un tableau avec des éléments de type entier (type par défaut)

```python
l = [-1, 2, 3]
mat = np.array(l)
mat
    -> [-1, 2, 3]
```

multiplions les éléments du tableau `mat` par `100`



```python
mat*100
-> [-100,  200,   300]
```


créons maintenant un tableau avec des éléments de type *entier signé sur 8 bits* (1 octet)

```python
l = [-1, 2, 3]
mat = np.array(l, np.int8)
mat
    -> [-1, 2, 3]
```

multiplions les éléments du tableau `mat` par `100`



```python
mat*100
-> [-100,  -56,   44]
```

**et non pas** `[-100,  200,  300]`


le problème ?

* `numpy` ne modifie jamais la taille (le type) des éléments d'un tableau existant
* il calcule donc à taille-mémoire constante
* et convertit au-besoin les valeurs



pour éviter tout problème restez sur le type inféré par `numpy`  
vos entiers seront le plus souvent des `numpy.int64` ou des `numpy.int32`
````

```{code-cell} ipython3
# le code
l = [-1, 2, 3]
mat = np.array(l) # vous laissez numpy inférer le type
print(    mat    )
print(    mat*100    )
print(    mat.dtype    )
```

```{code-cell} ipython3
# le code
l = [-1, 2, 3]
mat = np.array(l, np.int8) # vous imposez le type
print(    mat    )
print(    mat*100    )
```

+++ {"tags": ["framed_cell"]}

## autres constructeurs de  `numpy.ndarray`

````{admonition} →

| les méthodes | ce qu'elles font |
| --------------------------- | ------------------------------------------- |
| `numpy.zeros` | renvoie un ndarray rempli de *0.* (float) |
| `numpy.ones` | renvoie un ndarray rempli de *1.* (float) |
| `numpy.empty` | renvoie un ndarray vide i.e. sans initialiser ses éléments |
| | |
| `numpy.arange` | tableau de valeurs régulièrement espacées|
| `numpy.linspace` |  tableau de valeurs régulièrement espacées|
| | |
| `numpy.random.randint` | entiers aléatoirement générés |
| `numpy.random.randn` | flottants aléatoirement générés |
````

+++

***

+++ {"tags": ["framed_cell"]}

### tableau de zéros `numpy.zeros`

````{admonition} →

vous devez indiquer à la fonction `numpy.zeros` la forme du tableau


```python
zorro = np.zeros(shape=(4, 5))
zorro
-> [[0., 0., 0., 0., 0.],
    [0., 0., 0., 0., 0.],
    [0., 0., 0., 0., 0.],
    [0., 0., 0., 0., 0.]]
```


on peut donner d'autres paramètres, comme le type des éléments...

```python
zorro1 = np.zeros(shape=(4, 5), dtype=np.uint64)
zorro1
-> [[0, 0, 0, 0, 0],
    [0, 0, 0, 0, 0],
    [0, 0, 0, 0, 0],
    [0, 0, 0, 0, 0]
```
````

```{code-cell} ipython3
# le code
zorro = np.zeros(shape=(4, 5))
zorro
```

```{code-cell} ipython3
# le second code
zorro1 = np.zeros(shape=(4, 5), dtype=np.uint64)
zorro1
```

+++ {"tags": ["framed_cell"]}

````{admonition} exercice

* affichez le type des éléments de `zorro`

* créez le tableau multi-dimensionnel des entiers positifs 8 bits suivant

```python
array([[[0, 0, 0],
        [0, 0, 0],
        [0, 0, 0],
        [0, 0, 0],
        [0, 0, 0]],

       [[0, 0, 0],
        [0, 0, 0],
        [0, 0, 0],
        [0, 0, 0],
        [0, 0, 0]]])
```
````

```{code-cell} ipython3
# votre code ici
```

```{code-cell} ipython3
# prune-cell
print(    zorro.dtype    )
np.zeros(shape=(2, 5, 3), dtype=np.uint8)
```

+++ {"tags": ["framed_cell"]}

### tableau non-initialisé `numpy.empty`

````{admonition} →

la fonction `numpy.empty`


**utilité ?**

* ne pas perdre de temps à initialiser inutilement un tableau
* quand vous n'allez jamais utiliser la valeur initiale des éléments
````

+++

**exercice**

1. créez un tableau de forme `(3, 5)` de valeurs non-initialisées  
   de type entiers signés sur 8 bits
1. affichez-le
1. que contient-il ?

```{code-cell} ipython3
# votre code ici
```

```{code-cell} ipython3
# prune-cell
tab = np.empty(shape=(3, 5), dtype=np.int8)
print(tab) # n'importe quelles valeurs entre -128 et 127
```

+++ {"tags": ["framed_cell"]}

### tableau de valeurs régulièrement espacées

````{admonition} →

`numpy.arange(from, to, step)`

* ressemble un peu au `range` de Python
* nombres équidistants de `step` sur l'intervalle `[from, to[`  
* en général `step` est entier (mais pas obligatoire)

`numpy.linspace(from-included, to-included, n)`

* `n` réels régulièrement espacés dans un intervalle
* la valeur supérieure de l'intervalle **est** incluse (par défaut)
````

```{code-cell} ipython3
# exemple avec arange
# comme avec le range() de Python
# la deuxième borne est exclue
np.arange(0, 5)
```

```{code-cell} ipython3
# exemple avec linspace
from matplotlib import pyplot as plt

X = np.linspace(-np.pi, np.pi, 30)
Y = np.sin(X)
plt.plot(X, Y)
```

````{admonition} astuce
:class: tip

pour éviter de voir apparaitre la ligne avec le vilain `[<matplotlib.lines.Line2D at 0x...>]`, on ajoute habituellement un `;` à la fin de la dernière ligne de la cellule
````

```{code-cell} ipython3
# pour éviter l'affichage superflu, ajoutez un ;
plt.plot(X, Y);
```

## tableaux de valeurs aléatoires

+++ {"tags": ["framed_cell"]}

### générateur de valeurs aléatoires entières

````{admonition} →

`numpy.random.randint` permet de tirer un nombre entier aléatoirement entre deux bornes  
(la seconde est exclue)
```python
borne_inf = 10
borne_sup = 20
np.random.randint(borne_inf, borne_sup)
```

passez lui le paramètre `size` (et non pas `shape`)
pour générer un tableau-multi-dimensionnel d'une forme donnée

```python
np.random.randint(10, 20, size=(2, 3, 5))
->
array([[[11, 18, 14, 19, 16],
        [17, 14, 15, 11, 11],
        [13, 17, 11, 10, 13]],

       [[12, 14, 10, 13, 17],
        [11, 17, 18, 19, 18],
        [19, 15, 10, 17, 18]]])
```
````

```{code-cell} ipython3
# le code
borne_inf = 10
borne_sup = 20
np.random.randint(borne_inf, borne_sup)
```

```{code-cell} ipython3
# le code
np.random.randint(10, 20, size=(2, 3, 5))
```

+++ {"tags": ["framed_cell"]}

### générateur de valeurs aléatoires réelles

````{admonition} →

`numpy.random.randn` renvoie un échantillon  
de la loi normale centrée-réduite (moyenne 0, écart-type 1)

```python
np.random.randn()
-> 0.19176811586596798
```


`numpy.random.randn(d0, ..., dn)` génére un tableau de `shape` $(d_1, ..., d_n)$

```python
np.random.randn(2, 3, 1)
->
array([[[-0.91543618],
        [-2.12493972],
        [ 0.93155056]],

       [[-0.17198904],
        [-0.69164236],
        [-0.43321452]]])
```


la librairie `numpy.random`

* contient plus de fonctionnalités pour le calcul scientifique que `random.random`
* sait manipuler efficacement des tableaux `numpy.ndarray`
````

```{code-cell} ipython3
# le code
np.random.rand()
```

```{code-cell} ipython3
# le code
np.random.randn(2, 3, 1)
```

**exercice** génération aléatoire et affichage *couleur*


avec la fonction `numpy.random.randint`
dont l'aide est obtenue en tapant
```python
np.random.randint?
```

1. construisez une image de `10 x 10` pixels en format RBG  
i.e. chaque pixel est composé de 3 valeurs entières entre 0 et 255 inclus


2. affichez l'image avec `plt.imshow`

```{code-cell} ipython3
# votre code ici
```

```{code-cell} ipython3
# prune-cell
img = np.random.randint(0, 256, size=(10, 10, 3), dtype=np.uint8)
plt.imshow(img);
```

+++ {"tags": ["level_intermediate", "framed_cell"]}

## comparaison des temps de création tableaux

(avancé)

````{admonition} →

`%timeit` permet d'évaluer le temps d'exécution d'une ligne de code  
`%%timeit` permet d'évaluer le temps d'exécution d'une cellule de code  


```python
%timeit 1 + 1
-> 8.16 ns ± 0.124 ns per loop (mean ± std. dev. of 7 runs, 100000000 loops each)
```
la moyenne et l'écart-type des temps d'exécution de l'instruction `1 + 1` ont été calculés  
(cela a été fait 7 fois et le meilleur résultat a été pris, voir le help)

* avec `-n` vous pouvez baisser le nombre de calculs, ce sera donc moins précis

```python
%timeit -n 10000 1 + 1
-> 12.5 ns ± 3.4 ns per loop (mean ± std. dev. of 7 runs, 10000 loops each)
```

`ns` = nano-seconde

calcul du temps d'exécution d'une cellule

```python
%%timeit
a = 1
a + 1
```
````

```{code-cell} ipython3
:tags: [level_intermediate]

# le code
%timeit 1 + 1
```

```{code-cell} ipython3
:tags: [level_intermediate]

# le code
%timeit -n 10000 1 + 1
```

```{code-cell} ipython3
:tags: [level_intermediate]

%%timeit
a = 1
a + 1
```

+++ {"tags": ["level_intermediate"]}

**exercice**

comparez les temps d'exécution de

* la création d'un `numpy.ndarray` à partir d'une liste Python comportant 10.000 floats initialisés à 0  
ne pas mettre la création de la liste Python dans le calcul du temps

* la création d'un `numpy.ndarray` de 10.000 éléments initialisés à 0

* la création d'un `numpy.ndarray` de 10.000 éléments non-initialisés

* lequel est le plus rapide ?

```{code-cell} ipython3
:lines_to_next_cell: 0
:tags: [level_intermediate]

# votre code ici
```

```{code-cell} ipython3
# prune-cell
n = 10000
l = [0]*n
```

```{code-cell} ipython3
# prune-cell
%timeit np.array(l)
```

```{code-cell} ipython3
# prune-cell
%timeit np.zeros(shape=(n))
```

```{code-cell} ipython3
# prune-cell
%timeit np.empty(shape=(n))
```
