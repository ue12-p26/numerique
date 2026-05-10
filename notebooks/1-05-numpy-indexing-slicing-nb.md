---
jupytext:
  cell_metadata_json: true
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

# indexation et *slicing*

```{code-cell} ipython3
import numpy as np
from matplotlib import pyplot as plt
```

+++ {"tags": ["framed_cell"]}

## contenu de ce notebook (sauter si déjà acquis)

* les manières d'accéder à des éléments et de slicer un tableau `numpy`
* les slices sont des vues et non des copies
* la notion de `numpy.ndarray.base`
* voir les `exercices avancés pour les rapides`

+++ {"tags": ["framed_cell"]}

## accès aux éléments d'un tableau

````{admonition} →

*accéder à des éléments ou à des sous-tableaux  
va nous permettre de leur appliquer des fonctions vectorisées*


la manière d'accéder aux éléments d'un tableau `numpy`  
dépend de la forme du tableau (`shape`)


la forme d'un `numpy.ndarray` est donnée par une indexation  
sur le segment mémoire sous-jacent continu de votre tableau

par exemple  
un `numpy.ndarray` de `12` éléments

<div class="memory">

```
☐☐☐☐☐☐☐☐☐☐☐☐
```

</div>

peut être indexé sous différentes dimensions et formes

* dimension 1, par exemple `(12,)`
* dimension 2, par exemple `(1, 12)` `(6, 2)` `(3, 4)` `(4, 3)`
* dimension 3, par exemple `(2, 3, 2)`...
````

+++

***

+++ {"tags": ["framed_cell"]}

### accès à un tableau de dimension 1

``````{admonition} →
vous avez besoin d'**un seul index**

```python
tab = np.arange(12)
tab[0] = np.pi
```


Quelle est le type de `tab[0]` ?  
Quelle est la valeur de `tab[0]` ?

rappelez-vous

* les éléments d'un tableaux `numpy` sont typés et leur taille est fixe

pour mettre des réels dans un tableau  
il faut que le type des éléments corresponde

```python
tab1 = tab.astype(np.float64)
tab1[0] = np.pi # 3.141592653589793
```

`````{admonition} quiz pour les forts
:class: dropdown
à votre avis est-ce qu'on pourrait écrire aussi ceci ?
```python
tab1[0,]
```
````{admonition} réponse
:class: dropdown tip
OUI on peut, parce que  
- pour indexer un tableau de dimension par exemple 2, on peut utiliser un tuple de taille 2
- du coup par continuité si on veut, on peut aussi indexer un tableau de dimension 1 avec un tuple de taille 1
- or en Python `0,` ça représente justement un tuple avec un seul élément `0` dedans  
````
`````
``````

```{code-cell} ipython3
# le code
tab = np.arange(12)
tab[0] = np.pi
tab[0].dtype, tab[0]
```

```{code-cell} ipython3
# le code
tab1 = tab.astype(np.float64)
tab1[0] = np.pi
tab1[0].dtype, tab1[0]
```

+++ {"tags": ["framed_cell"]}

### accès à un tableau de dimension > à 1

`````{admonition} →
l'accès à un élément du tableau dépend de la forme du tableau  

il y aura - au plus - un indice par dimension (voir plus bas pourquoi *au plus*)

***

en dimension 2
```python
tab = np.arange(12).reshape((2, 6))

# première ligne, deuxième colonne
line, col = 0, 1

tab[line, col] = 1000
tab
-> array([[ 0, 1000,  2,  3,  4,  5],
          [ 6,    7,  8,  9, 10, 11]])
```

***

en dimension 3
```python
tab.resize((2, 3, 2))

# deuxième matrice, troisième ligne, première colonne
mat, line, col = 1, 2, 0

tab[mat, line, col] = 2000
tab
-> array([[[   0, 1000],
           [   2,    3],
           [   4,    5]],
    
          [[   6,    7],
           [   8,    9],
           [2000,   11]]])
```

````{admonition} rappel
:class: seealso

le nombre d'éléments dans chaque dimension est donné par `tab.shape`
````

````{admonition} pourquoi "au plus" ?

on a dit qu'il peut y avoir **au plus** un indice par dimension, car on peut en donner moins  
dans ce cas vous obtenez un sous-tableau au lieu d'une valeur scalaire 

par exemple si le tableau `a` a pour `shape=(2, 3, 4, 5)`  
alors `a[i, j]` va, bien sûr, désigner .. un tableau de `shape=(4, 5)`  
````

````{admonition} rappel: lignes et colonnes
:class: dropdown

* en dimension >=2, les deux dernières dimensions sont les lignes et les colonnes, dans cet ordre  
  (enfin plus exactement, c'est la convention pour l'affichage des tableaux)  

* du coup en dimension 2, voici un idiome pour ranger ça dans deux variables:  
  ```python
  rows, columns = tab.shape
  ```
````
`````

```{code-cell} ipython3
# le code en dimension 2

tab = np.arange(12).reshape((2, 6))

# première ligne, deuxième colonne
line, col = 0, 1

tab[line, col] = 1000
tab
```

```{code-cell} ipython3
# le code en dimension 3
tab.resize((2, 3, 2))

# deuxième matrice, troisième ligne, première colonne
mat, line, col = 1, 2, 0

tab[mat, line, col] = 2000
tab
```

```{code-cell} ipython3
:lines_to_next_cell: 2

[tab.shape[i] for i in range(tab.ndim)]
```

```{code-cell} ipython3
tab.shape
```

### exercices

+++

**accès à un élément**  
1. créez un tableau des 30 valeurs paires à partir de 2 (utilisez `numpy` pas `Python`)


2. donnez lui la forme de 2 matrices de 5 lignes et 3 colonnes


3. accédez à l'élément qui est à la 3ème colonne de la 2ème ligne de la 1ère matrice


4. obtenez-vous 12 ?

```{code-cell} ipython3
# votre code
```

+++ {"cell_style": "center"}

**exercice**

1. faites un `np.ndarray` de forme `(3, 2, 5, 4)`  
   avec des nombre aéatoires entiers entre 0 et 100


2. affichez-le et
   vous voyez trois groupes et 2 matrices de 5 lignes et 4 colonnes



3. affichez le nombre des éléments des deux dernières dimensions


````{admonition} indice
:class: tip dropdown

* voyez `np.random.randint` pour créer un tableau aléatoire
* tapez `np.random.randint?` pour avoir de l'aide en ligne
````

```{code-cell} ipython3
# votre code ici
```

## accéder à un sous-tableau (slicing)

+++ {"tags": ["framed_cell"]}

### différence slicing `python` et `numpy`

````{admonition} →

le **slicing** `numpy` est *syntaxiquement équivalent* à celui des listes `Python`

la **grande** différence est que

* quand vous slicez un **tableau `numpy`** vous obtenez une **vue** sur le tableau initial  
(avec une nouvelle indexation)

* quand vous slicez une **liste `python`** vous obtenez une **copie** de la liste initiale


le slicing `numpy` va

* regrouper des éléments du tableau initial
* dans un sous-tableau `numpy.ndarray` avec l'indexation adéquate
* la mémoire sous-jacente reste la même

la seule structure informatique qui sera créée est l'indexation  

vous pourrez ensuite, par exemple, modifier ces éléments  
et donc ils seront modifiés dans le tableau initial
````

+++

***

+++ {"tags": ["framed_cell"]}

### rappel du slicing Python

````{admonition} →
**rappel du slicing Python**


* `l[from:to-excluded:step]`


* paramètres tous optionnels  
par défaut: `from = 0` `to-excluded = len(l)`et `step=1`


* indices négatifs ok `-1` est le dernier élément, `-2` l'avant dernier ...


la liste python des 10 premiers entiers

```python
l = [0, 1, 2, 3, 4, 5, 6, 7, 8, 9]

# un élément sur 2 en partant du début de la liste (copie)
l[::2]

# un élément sur 3 en partant du premier élément de la liste (copie)
l[1::3]

# la liste en reverse (copie)
l[::-1]

# la liste entière (copie)
l[::]
# ou
l[:]
```
````

```{code-cell} ipython3
# le code
l =  [0, 1, 2, 3, 4, 5, 6, 7, 8, 9 ]
print(l[::2])
print(l[1::3])
print(l[::-1])
print(l[:])
```

+++ {"tags": ["framed_cell"]}

### slicing en dimension 1

````{admonition} →
on crée un `numpy.ndarray` de dimension 1 de taille 10

* on prend un élément sur 2 en partant du début de la liste  
* on modifie les éléments du sous-tableau obtenu  
* le tableau initial est modifié



```python
vec = np.arange(10) # [0 1 2 3 4 5 6 7 8 9]
print(vec[::2])     # [0 2 4 6 8]
vec[::2] = 100
print(vec)          # [100, 1, 100, 3, 100, 5, 100, 7, 100, 9]
```
````

```{code-cell} ipython3
# le code
vec = np.arange(10)
print(vec[::2])
vec[::2] = 100
vec
```

+++ {"tags": ["framed_cell"]}

### slicing en dimension > à 1 (a)

````{admonition} →
on crée un `numpy.ndarray` en dimension 4, de forme `(2, 3, 4, 5)`  
on l'initialise avec les `120`  premiers entiers

```python
tab = np.arange(120).reshape(2, 3, 4, 5)
```

on a 2 groupes de 3 matrices de 4 lignes et 5 colonnes

* on accède au premier groupe de matrices
```python
tab[0]
```

* on accède à la deuxième matrice du premier groupe de matrices
```python
tab[0, 1]
```

* on accède à la troisième ligne de la deuxième matrice du premier groupe de matrices

```python
tab[0, 1, 2]
```

* on accède à la quatrième colonne de la deuxième matrice du premier groupe de matrices

```python
tab[0, 1, :, 3] # remarquez le ':' pour indiquer toutes les lignes
```
````

```{code-cell} ipython3
# le code
tab = np.arange(120).reshape(2, 3, 4, 5)
print(    tab    )
print(    tab[0]    )
print(    tab[0, 1]    )
print(    tab[0, 1, 2]    )
print(    tab[0, 1, :, 3]    )
```

+++ {"tags": ["framed_cell"]}

### slicing en dimension > à 1 (b)

````{admonition} →
on crée un `numpy.ndarray` en dimension 4, de forme `(2, 3, 4, 5)`  
on l'initialise avec les `120`  premiers entiers

```python
tab = np.arange(120).reshape(2, 3, 4, 5)
```

on peut combiner les slicing des 4 dimensions, ici  
`tab[from:to:step, from:to:step, from:to:step, from:to_step]`  

de l'indice `from` à l'indice `to` (exclus) avec un pas `step`  

à savoir

* quand vous voulez la valeur par défaut de `from`, `to` et `step` vous ne mettez rien
* quand les valeurs par défaut sont en fin d'expression, elles sont optionnelles
* du coup pour prendre tous les éléments dans une dimension  
  on peut mettre simplement la slice universelle `::`, que généralement on abrège encore en juste `:`

**exemples**

la première matrice de tous les groupes de matrice, c'est-à-dire:
- tous les groupes  
- la première matrice  
- toutes les lignes  
- toutes les colonnes

```python
# en version longue où on épelle bien tout
tab[::, 0, ::, ::]

# en version courte on abrège et ça donne simplement
tab[:, 0]        
```
````

```{code-cell} ipython3
tab = np.arange(120).reshape(2, 3, 4, 5)
```

```{code-cell} ipython3
# en version longue

tab[::, 0, ::, ::]
```

```{code-cell} ipython3
# en version courte

tab[:, 0]
```

**exercices**

1. extrayez du tableau `tab` précédent  
```python
tab = np.arange(120).reshape(2, 3, 4, 5)
```

la sous-matrice au milieu des premières matrices de tous les groupes, ici ça doit donner:

$\begin{bmatrix}\begin{bmatrix} 6 & 7 & 8\\ 11 & 12 & 13 \end{bmatrix}, \begin{bmatrix} 66 & 67 & 68 \\ 71 & 72 & 73 \end{bmatrix}\end{bmatrix}$  

**indices**  
on a 2 groupes de 3 matrices de 4 lignes et 5 colonnes

donc

* pour les 2 groupes de matrices
* dans la première matrice
* la sous-matrice du milieu
(obtenue en enlevant une épaisseur de largeur 1 sur le pourtour)  

donc

* tous les groupes `:`
* la première matrice (indice `0`)
* de la première ligne (indice `1`) à l'avant dernière ligne (indice `-1`) step par défaut
* idem pour les colonnes

```{code-cell} ipython3
# votre code
```

+++ {"tags": ["framed_cell"]}

## les sous-tableaux sont des vues, et non des copies

````{admonition} →
le slicing calcule une nouvelle indexation sur le segment mémoire du tableau existant


si à chaque slicing, `numpy` faisait une copie du tableau sous-jacent, les codes seraient inutilisables  
parce que coûteux (pénalisés) en place mémoire


**donc lors d'un slicing**

* un nouvel objet `np.ndarray` est bien créé
* son indexation est différente de celle de l'objet `np.ndarray` initial
* mais ils **partagent** la mémoire (le segment unidimensionnel sous-jacent)

si un utilisateur veut une copie, il la fait avec la méthode `copy`

```python
tab1 = tab[:, 0, 1:-1, 1:-1].copy()
```
````

+++

***

+++ {"tags": ["framed_cell", "level_intermediate"]}

## partage du segment sous-jacent ou non? - avancé

````{admonition} →
un tableau `numpy.ndarray` peut être
1. un tableau *original* (on vient de le créer éventuellement par copie)
1. une vue sur un tableau (il a été créé par slicing ou indexation)  
  il partage son segment de mémoire avec au moins un autre tableau


l'attribut `numpy.ndarray.base` vaut alors


1. `None` si le tableau est un tableau original

```python
tab = np.arange(10)
print(tab.base)
-> None
```


```python
tab1 = np.arange(10)
tab2 = tab1.copy()
print(tab2.base)
-> None
```

2. **le tableau original qui a servi à créer la vue**  
    quand le tableau est une vue  



```python
tab1 = np.array([[1, 2, 3], [4, 5, 6]])
tab2 = tab1[0:2, 0:2] # une vue
tab2.base is tab1
-> True
```

```python  
tab1 = np.arange(120)
tab2 = tab1.reshape(2, 3, 4, 5) # une vue
tab2.base is tab1
-> True
```

faites attention, dans l'exemple

```python
tab1 = np.arange(10).reshape(2, 5)
```

`tab1.base` est l'objet `np.arange(10)`  


les `numpy.ndarray` ayant le même objet `numpy.ndarray.base`

* partagent tous leur segment sous-jacent
* sont différentes vues d'un même tableau original  
(celui indiqué par leur attribut `base`)

* modifier les éléments de l'un modifiera les éléments des autres  
(ils *pointent tous* sur le même segment de mémoire)

`numpy` essaie de créer le moins de mémoire possible  
pour stocker les éléments de ses tableaux
````

```{code-cell} ipython3
# le code
tab1 = np.arange(10)
print(tab1.base)
```

```{code-cell} ipython3
# le code
tab1 = np.arange(10)
tab2 = tab1.copy()
print(tab2.base)
```

```{code-cell} ipython3
# le code
tab1 = np.array([[1, 2, 3], [4, 5, 6]])
tab2 = tab1[0:2, 0:2] # vue
tab2.base is tab1
```

```{code-cell} ipython3
# le code
tab1 = np.arange(120)
tab2 = tab1.reshape(2, 3, 4, 5) # une vue
tab2.base is tab1
```

```{code-cell} ipython3
# le code
tab1 = np.arange(10).reshape(2, 5)
tab1.base
```

**exercice**


1. créez un nouveau tableau formé des deux matrices $[\begin{pmatrix} 2 & 4 & 6\\ 8 & 10 & 12 \end{pmatrix}, \begin{pmatrix} 14 & 16 & 18 \\ 20 & 22 & 24 \end{pmatrix}]$.  

1. affichez sa `base`

1. *slicez* le tableau pour obtenir $[\begin{pmatrix} 24 & 22 & 20 \\ 18 & 16 & 14 \\ \end{pmatrix}, \begin{pmatrix} 12 & 10 & 8 \\ 6 & 4 & 2\end{pmatrix}] $

1. affichez la `base` de la slice

1. vérifiez que les deux `base` sont le même objet

```{code-cell} ipython3
# votre code ici
```

+++ {"tags": ["framed_cell"]}

## modification des sous-tableaux

````{admonition} →
pour modifier un sous-tableau, il faut simplement faire attention
1. au type des éléments  
2. et à la forme du tableau
````

+++

## exercices avancés pour les rapides

+++

avant d'aborder ces exercices, il existe un utilitaire très pratique (parmi les 2347 que nous n'avons pas eu le temps de couvrir ;); il s'agit de `numpy.indices()`

commençons par un exemple :

```{code-cell} ipython3
lignes, colonnes = np.indices((3, 5))
```

```{code-cell} ipython3
:cell_style: split

lignes
```

```{code-cell} ipython3
:cell_style: split

colonnes
```

vous remarquerez que dans le tableau qui s'appelle `lignes`, la valeur dans le tableau correspond au numéro de ligne; dit autrement :

* `lignes[i, j] == i` pour tous les `(i, j)`,

et dans l'autre sens bien sûr

* `colonnes[i, j] == j`

```{code-cell} ipython3
:cell_style: split

lignes[1, 4]
```

```{code-cell} ipython3
:cell_style: split

colonnes[1, 4]
```

Pourquoi est-ce qu'on parle de ça me direz-vous ?

Eh bien en guise d'indice, cela vous renvoie à la notion de programmation vectorielle.

Ainsi par exemple si je veux créer une matrice de taille (3,5) dans laquelle `M[i, j] == i + j`, je **ne vais surtout par écrire une boucle `for`**, et au contraire je vais écrire simplement

```{code-cell} ipython3
I, J = np.indices((3, 5))
M = I + J
M
```

### les rayures

+++

Écrivez une fonction `zebre`, qui prend en argument un entier *n* et qui fabrique un tableau carré de coté `n`, formé d'une alternance de colonnes de 0 et de colonnes de 1.

+++

par exemple pour `n=4` on s'attend à ceci

```console
0 1 0 1
0 1 0 1
0 1 0 1
0 1 0 1
```

+++

### le damier

Écrivez une fonction *checkers*, qui prend en argument la taille *n* du damier, et un paramètre optionnel qui indique la valeur de la case (0, 0), et qui crée un tableau `numpy` carré de coté `n`, et le remplit avec des 0 et 1 comme un damier.

vous devez obtenir par exemple

```python
>>> checkers(4)

array([[1, 0, 1, 0],
       [0, 1, 0, 1],
       [1, 0, 1, 0],
       [0, 1, 0, 1]])

>>> checkers(5, False)

array([[0, 1, 0, 1, 0],
       [1, 0, 1, 0, 1],
       [0, 1, 0, 1, 0],
       [1, 0, 1, 0, 1],
       [0, 1, 0, 1, 0]])
```

```{code-cell} ipython3
# a vous de jouer

def checkers(n, up_left=True):
    pass
```

```{code-cell} ipython3
# pour tester

checkers(4)
```

```{code-cell} ipython3
checkers(5, False)
```

+++ {"tags": ["level_advanced"]}

### le super damier par blocs

+++ {"tags": ["level_advanced"]}

Il y a beaucoup de méthodes pour faire cet exercice de damier; elles ne vont pas toutes se généraliser pour cette variante du super damier :

**Variante** écrivez une fonction `block_checkers(n, k)` qui crée et retourne

* un damier de coté `k*n x k*n`
* composé de blocs de `k x k` homogènes (tous à 0 ou tous à 1)
* eux mêmes en damiers
* on décide que le premier bloc (en 0,0) vaut 0

c'est-à-dire par exemple pour `n=4` et `k=3` cela donnerait ceci :

```
>>> block_checkers(4, 3)

array([[0, 0, 0, 1, 1, 1, 0, 0, 0, 1, 1, 1],
       [0, 0, 0, 1, 1, 1, 0, 0, 0, 1, 1, 1],
       [0, 0, 0, 1, 1, 1, 0, 0, 0, 1, 1, 1],
       [1, 1, 1, 0, 0, 0, 1, 1, 1, 0, 0, 0],
       [1, 1, 1, 0, 0, 0, 1, 1, 1, 0, 0, 0],
       [1, 1, 1, 0, 0, 0, 1, 1, 1, 0, 0, 0],
       [0, 0, 0, 1, 1, 1, 0, 0, 0, 1, 1, 1],
       [0, 0, 0, 1, 1, 1, 0, 0, 0, 1, 1, 1],
       [0, 0, 0, 1, 1, 1, 0, 0, 0, 1, 1, 1],
       [1, 1, 1, 0, 0, 0, 1, 1, 1, 0, 0, 0],
       [1, 1, 1, 0, 0, 0, 1, 1, 1, 0, 0, 0],
       [1, 1, 1, 0, 0, 0, 1, 1, 1, 0, 0, 0]])
```

```{code-cell} ipython3
:tags: [level_advanced]

#  vous de jouer

def block_checkers(n, k):
    pass
```

```{code-cell} ipython3
:tags: [level_advanced]

block_checkers(3, 2)
```

```{code-cell} ipython3
:tags: [level_advanced]

# doit vous donner la figure ci-dessus
# éventuellement avec des False/True au lieu de 0/1

block_checkers(4, 3)
```

### les escaliers

+++

Écrivez une fonction *escalier*, qui prend en argument un entier *n*, qui crée un tableau de taille *2n+1*, et qui le remplit de manière à ce que:

- aux quatre coins du tableau on trouve la valeur *0*
- dans la case centrale on trouve la valeur *2n*
- et si vous partez de n'importe quelle case  et que vous vous déplacez d'une case (horizontalement ou verticalement),
 en vous dirigeant vers une case plus proche du centre, la valeur augmente de 1

par exemple

```python
>>> stairs(4)

array([[0, 1, 2, 3, 4, 3, 2, 1, 0],
       [1, 2, 3, 4, 5, 4, 3, 2, 1],
       [2, 3, 4, 5, 6, 5, 4, 3, 2],
       [3, 4, 5, 6, 7, 6, 5, 4, 3],
       [4, 5, 6, 7, 8, 7, 6, 5, 4],
       [3, 4, 5, 6, 7, 6, 5, 4, 3],
       [2, 3, 4, 5, 6, 5, 4, 3, 2],
       [1, 2, 3, 4, 5, 4, 3, 2, 1],
       [0, 1, 2, 3, 4, 3, 2, 1, 0]])
```

```{code-cell} ipython3
# à vous de jouer

def stairs(n):
    pass
```

```{code-cell} ipython3
# pour vérifier
stairs(4)
```

+++ {"tags": ["level_advanced"]}

### calculs imbriqués (avancé)

+++ {"tags": ["level_advanced"]}

Regardez le code suivant :

```{code-cell} ipython3
:tags: [level_advanced]

# une fonction vectorisée
def pipeline(array):
    array2a = np.sin(array)
    array2b = np.cos(array)
    array3 = np.exp(array2a + array2b)
    array4 = np.log(array3+1)
    return array4
```

+++ {"tags": ["level_advanced"]}

Les questions : j'ai un tableau `X` typé `float64` et de forme `(1000,)`

* j'appelle `pipeline(X)`, combien de mémoire est-ce que `pipeline` va devoir allouer pour faire son travail ?
* quel serait le minimum de mémoire dont on a besoin pour faire cette opération ?
* voyez-vous un moyen d'optimiser `pipeline` pour atteindre ce minimum ?

+++ {"tags": ["level_advanced"]}

**indice**

* l'exercice vous invite à réfléchir à l'utilisation du paramètre `out=` qui est supporté dans les fonction vectorisées de numpy
* dans ce cadre, sachez qu'on peut presque toujours remplacer l'usage d'un opérateur (comme ici `+`) par une fonction vectorisée (ici `np.add`)
