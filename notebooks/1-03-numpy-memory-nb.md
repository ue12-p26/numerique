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

# la mémoire

+++ {"tags": ["framed_cell"]}

## contenu de ce notebook (sauter si déjà acquis)

avoir une intuition de ce qui se passe dans en mémoire pour un `numpy.ndarray`  

> *An array object represents a multidimensional, **homogeneous** array of **fixed-size** items.*

* indiçage des tableaux `numpy`
* modification de la forme des tableaux `numpy` avec `numpy.resize` et `numpy.reshape` (la mémoire sous-jacente est partagée)
* indirection versus décalage (*offset*)

+++ {"tags": ["framed_cell"]}

## organisation de la mémoire

````{admonition} →
### pourquoi comprendre comment `numpy` travaille en mémoire ?

pour prendre des décisions en connaissance de cause  

* savoir les conséquences de vos choix
* comprendre les erreurs  
(conversions implicites...)

pour ne pas être dépourvu le jour où votre code, en se complexifiant

* devient beaucoup trop lent
* prend beaucoup trop d'espace mémoire

pour vous familiariser avec l'informatique et comprendre

* les mécanismes sous-jacents
* les choix des concepteurs

pour vous faire une petite culture en informatique technique

* ne jamais penser que c'est magique, incompréhensible, trop compliqué...
* le plus souvent c'est simplement logique
````

+++

créons un tableau `numpy` en 2 dimensions: 4 lignes et 5 colonnes

```{code-cell} ipython3
import numpy as np
```

```{code-cell} ipython3
mat =  np.array(
    [[1, 2, 3, 4, 5],
     [6, 7, 8, 9, 10],
     [11, 12, 13, 14, 15],
     [16, 17, 18, 19, 20]])
mat
```

la mémoire occupée en mémoire en nombre d'octets (byte)

```{code-cell} ipython3
mat.nbytes
```

+++ {"tags": ["framed_cell"]}

### organisation en mémoire des tableaux

````{admonition} →
l'aide (accessible via `help(np.ndarray)`) dit
> *An array object represents a multidimensional, homogeneous array of fixed-size items.*

donc un `numpy.ndarray` est un tableau
1. **multi-dimensionnel**
1. avec un type d'élément **homogène**
1. et des éléments de **taille fixe**

**homogène**  

* toutes les cases du tableau ont le même type
* donc elles occupent la même taille en mémoire

**taille fixe**  

* une fois un tableau créé, on ne peut plus modifier la taille de ses éléments  
i.e. le nombre d'octets sur lequel chaque élément est stocké en mémoire est fixe



* si on manipule et que la taille des éléments ne suffit plus ?  
`numpy` convertit la valeur  
mais ne modifie pas la taille de ses éléments


* pour modifier la taille des éléments ?  
on n'a pas le choix, il faut allouer un nouveau tableau, et recopier l'ancien dedans (et c'est à éviter...)

pourquoi ces **contraintes** ?  

* pour que `numpy` soit le plus rapide possible dans ses manipulations de tableaux
* grâce à ces contraintes, passer d'une case du tableau à une autre  est très rapide
````

+++

***

+++ {"tags": ["framed_cell"]}

### rapidité des manipulations mémoire

````{admonition} →
deux **idées** pour assurer la rapidité de manipulation de tableaux en mémoire


* passez rapidement d'une case du tableau à une autre (**offset**)


* avoir la valeur de l'élément directement dans la case (pas **d'indirection** mémoire)
````

+++

***

+++ {"tags": ["framed_cell"]}

### offset

````{admonition} →
supposons que le tableau soit représenté en mémoire par un **bloc d'octets continu**  
(ici 9 cases sont **contiguës** et de même taille - homogène)

<div class="memory">

```
...☐☐☐☐☐☐☐☐☐...
```

</div>


passer d'une case à une autre devient un simple décalage mémoire  
*on va 2 cases plus loin*  


l'**offset** est la distance qui sépare ces deux cases

un tel décalage devient impossible si un tableau était réparti un peu partout en mémoire...  

<div class="memory">

```
...☐.......☐..☐....☐...  
☐....☐.....☐.....☐.....  
......☐.....
```

</div>
````

+++

***

+++ {"tags": ["framed_cell"]}

### pas d'indirection mémoire

````{admonition} →
pour un tableau, on sait maintenant

* que la taille des éléments est homogène  
* que le bloc est contigu en mémoire

<div class="memory">

```
☐☐☐☐☐☐☐☐☐☐☐☐☐☐☐☐☐☐☐☐☐☐☐☐☐☐☐☐☐☐
```
</div>


l'idée de n'avoir pas d'indirection est

* quand on arrive dans une case du tableau
* elle contient la valeur qu'on cherche
* on n'a pas besoin d'aller ailleurs en mémoire

Que pourrait-il y avoir d'autre dans une case que la valeur d'un élément ?

si toutes les cases d'un même tableau en informatique ont la même taille, comment puis-je

* y "*mettre*"  des élément hétérogènes ? entier, réel, string...
* modifier ces éléments sans réallouer le tableau ?

```python
tab = [1, np.pi, True ]
tab[0] = 12345678235234501256848345678901234567890264378034
tab[0] = "bonjour"
```

en `python`, dans une case d'un vecteur (`list`)

* on ne trouve pas l'objet lui même (`1` ou `"bonjour"`)
* mais l'**adresse** en mémoire de l'endroit où l'objet a été alloué

si un tableau contient les adresses de ses éléments  
et pas directement la valeur des éléments  
il y aura une indirection à faire quand on arrive sur une case
````

+++

### exercice: tableau de chaînes de caractères

+++

**exercices**

1. à partir de la liste Python de chaînes de caractères
```python
l = ['un', 'deux', 'trois', 'cinq']
```
créez un tableau `numpy.ndarray` (de nom `tab`) et affichez-le

1. modifiez le premier élément pour mettre `quatre`
```python
tab[0] = 'quatre'
```
et affichez le tableau

1. Que constatez-vous ? Pourquoi `quatr` ?

1. affichez le type des éléments, le comprenez-vous ?  
`<` est une histoire d'ordre des octets dans les objets  
`U` signifie unicode  
Que signifie `5` ?

```{code-cell} ipython3
# votre code ici
```

`numpy` cherche le plus petit type pour stocker les chaînes de caractères initiales

ici une case est constituée d'un tableau d'au plus 5 caractères  
(une case n'est pas l'adresse d'une chaîne de caractère mais bien la valeur de la chaîne)

+++

### exercice: tableau hétérogène

+++

**exercice**


1. créez un tableau `np.ndarray` à partir de la liste Python suivante
```python
l = [127, 128, 17.4, np.pi, True, False]
```

1. affichez le type des éléments  
que constatez-vous ?  
que `numpy` a trouvé le plus petit type pouvant contenir tous ces objets numériques

1. ajoutez à la liste Python `l`, la chaîne de caractères `bonjour`  
et créez un autre `numpy.ndarray` à partir de la nouvelle valeur de `l`

1. affichez les éléments  
Que constatez-vous ?

1. quel type `numpy` a-t-il trouvé pour stocker tous ces éléments ?

```{code-cell} ipython3
# votre code ici
```

Pour plus d'informations, voir <https://numpy.org/doc/stable/user/basics.types.html>

+++

## index des tableaux

+++ {"tags": ["framed_cell"]}

### forme des tableaux numpy

````{admonition} →
la mémoire d'un `numpy.ndarray` est **toujours** un **segment unidimensionnel continu de cases de même taille et même type**

<div class="memory">

```
☐☐☐☐☐☐☐☐☐☐☐☐☐☐☐☐☐☐☐☐☐☐☐☐☐☐☐☐☐☐
```
</div>

`numpy` crée sur cette base, un système d'indexation

* pour *considérer* le tableau sous une forme (`shape`) multi-dimensionnelle
````

+++

***

+++ {"tags": ["framed_cell"]}

### 1-dimension

````{admonition} →
créons un tableau de dimension 1 donc de `shape=(30,)`
```python
seg = np.ones(shape=(30,))
```

un seul index suffit à le parcourir

<div class="memory">

```
 ☐☐☐☐☐☐☐☐☐☐☐☑☐☐☐☐☐☐☐☐☐☐☐☐☐☐☐☐☐☐
            ↑
           seg[i]

```

</div>

l'index est l'offset à partir du premier élément du tableau

le premier élément du tableau est indiqué par `seg`  
avec un offset de `0`

voila pourquoi la plupart du temps en informatique, les **tableaux commencent à l'index 0**
(et pas 1, sauf pour *matlab*, *R*, *Fortran*...)
````

+++

***

+++ {"tags": ["framed_cell"]}

### 2-dimension

````{admonition} →
créons un tableau de dimension 2, par exemple de `shape=(3, 10)`
```python
seg = np.ones(shape=(3, 10))
```

il faut 2 index pour le parcourir  
    un pour les lignes et un pour les colonnes `seg[i, j]`

<div class="memory">

```
        j
   ☐☐☐☐☐☐☐☐☐☐
i  ☐☐☐☐☐☑☐☐☐☐
   ☐☐☐☐☐☐☐☐☐☐
```

</div>

avec $i \in [0..3[$ et $j \in [0..10[$
````

+++

***

+++ {"tags": ["framed_cell"]}

### 3-dimension

````{admonition} →
créons un tableau de dimension 3, par exemple de `shape=(2, 3, 10)`
```python
seg = np.ones(shape=(2, 3, 10))
```

3 index pour le parcourir `seg[i, j, k]`  
table, ligne, colonne

<div class="memory">

```
           k
      ☐☐☐☐☐☐☐☐☐☐
    j ☐☐☐☐☐☑☐☐☐☐
      ☐☐☐☐☐☐☐☐☐☐
 i
      ☐☐☐☐☐☐☐☐☐☐
      ☐☐☐☐☐☐☐☐☐☐
      ☐☐☐☐☐☐☐☐☐☐

```

</div>

avec $i \in [0..2[$ et $j \in [0..3[$ et $k \in [0..10[$

et ainsi de suite
````

+++ {"tags": ["framed_cell"]}

### les lignes et colonnes

````{admonition} →
sachez qu'en dimension élevée (>=3), l'affichage de numpy fonctionne comme ceci:  
ce sont les **deux dernières valeurs de leur forme `tab.shape`**  
qui servent à déterminer le nombre **de lignes et de colonnes (resp.)**

```{admonition} seulement une convention !
:class: warning

c'est un **choix assez arbitraire** en fait; par exemple lorsqu'on construira des images on sera amenés à faire des tableaux de (100, 100, 3)  
mais cette image en fait fera 100 pixels de haut et 100 pixels de large, la dimension 3 ce sera pour les couleurs !

cela n'est important **que** quand vous regardez le tableau avec un `print()` !  
(et aussi quand vous faites des produits tensoriels avec `.dot()`, mais c'est une autre histoire; on en reparlera..
```

**exercice**

1. faites un tableau de `ones` de forme `(1, 2, 3, 4, 5)`
1. affichez-le
1. observez notamment la taille des rectangles qui sont affichés
1. corrélez cela avec la dimension du tableau
````

```{code-cell} ipython3
# votre code ici
```

## changer la forme d'un tableau

+++ {"tags": ["framed_cell"]}

### fonctions `resize` et `reshape`

````{admonition} →
on peut modifier la forme d'un `numpy.ndarray` existant  
tant qu'on ne modifie pas son nombre d'éléments

deux fonctions pour *réindexer* un tableau: `ndarray.reshape` et `ndarray.resize`

* `np.ndarray.reshape`  
  renvoie un tableau contenant les mêmes données avec une nouvelle forme

* `np.ndarray.resize`  
  modifie la forme du tableau *en-place* (directement dans le tableau)  
  et ne renvoie donc rien

```{admonition} pas de copie des données

NB: **aucune des deux fonctions ne crée un nouveau segment de données**  
elle ne font que créer (reshape) ou modifier (resize) l'indexation  
```

**reshape**

```python
seg = np.arange(0, 30)
seg = seg.reshape(5, 6) # reshape retourne le tableau ainsi modifié
seg = seg.reshape(2, 5, 3)
```

on peut le faire dès la création du tableau

```python
l = range(30)
seg = np.array(l).reshape(2, 5, 3)
```

**resize**

```python
seg = np.arange(0, 30)
seg.resize(5, 6) # resize modifie le tabeau en place
seg.resize(2, 5, 3)
```

si aucune mémoire n'est créée, c'est que les différentes indexations prises sur un tableau  
**partagent l'objet sous-jacent**
````

```{code-cell} ipython3
# le code
seg = np.arange(0, 30)
seg = seg.reshape(5, 6) # reshape retourne le tableau ainsi modifié
print(seg)
seg = seg.reshape(2, 5, 3)
print(seg)
```

```{code-cell} ipython3
# le code
seg = np.arange(0, 30)
seg.resize(5, 6) # resize modifie le tabeau en place
print(seg)
seg.resize(2, 5, 3)
print(seg)
```

### mémoire partagée

+++

**exercice**

1. créez un tableau `tab` de 6 `ones` de forme `(6)`  
et affichez-le

1. mettez dans `tab1` le reshape de `tab` avec la forme `(3, 2)`  
et affichez-le

1. modifiez le premier élément de `tab`

1. affichez `tab1`  
a-t-il été modifié ?

les deux objets  `tab` et `tab1` de type `numpy.ndarray`

* sont des objets différents (leurs index sont différents)
* mais ils ont le même segment sous-jacent de données
* toucher l'un a pour effet de modifier l'autre

````{admonition} indice pour créer un tuple de dimension 1
:class: dropdown

si vous écrivez `(1)` dans un programme Python, les parenthèses sont interprétées comme dans un calcul, i.e. comme dans `(2+3)`, du coup le résultat c'est l'entier `1`  
du coup pour contruire un **tuple** qui ne contient que un élément, je vous recommande d'écrire `(1,)`
````

```{code-cell} ipython3
# votre code
```
