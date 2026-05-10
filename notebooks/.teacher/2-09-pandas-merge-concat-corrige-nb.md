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

# accumulation des données

```{code-cell} ipython3
import pandas as pd
import numpy as np
```

+++ {"tags": ["framed_cell"], "jp-MarkdownHeadingCollapsed": true}

````{admonition} →
parfois on obtient les données par **plusieurs canaux**, qu'il faut accumuler dans une seule dataframe

les outils à utiliser pour cela sont multiples  
pour bien choisir, il est utile de se poser en priorité la question de savoir 
si les différentes sources à assembler concernent les **mêmes colonnes** ou au contraire les **mêmes lignes**  (*)


illustrations / use cases (juste pour fixer les idées)

* on recueille les données à propos du coronavirus, qui sont disponibles par mois  
  chaque fichier a la même structure - disons 2 colonnes: *deaths*, *confirmed*  
  l'assemblage consiste donc à accumuler les dataframes **en hauteur**

* on recueille les notes des élèves d'une classe de 20 élèves  
  chaque prof fournit un fichier excel avec les notes de sa matière  
  chaque table contient 20 lignes  
  il faut cette fois accumuler les dataframes **en largeur**
````

+++ {"tags": ["framed_cell"]}

## en hauteur `pd.concat()`

````{admonition} →
pour l'accumulation de données (en hauteur donc), préférez la fonction `pandas` suivante

* la fonction `pd.concat([df1, df2, ..])`  
  qui a vocation à accumuler des données en hauteur  
````

```{code-cell} ipython3
# exemple 1
# les deux dataframes ont les mêmes colonnes
# (ici on crée les dataframe à partir d'un dict décrivant les colonnes)
df1 = pd.DataFrame(
    data={
        'name': ['Bob', 'Lisa', 'Sue'],
        'group': ['Accounting', 'Engineering', 'HR']})

df2 = pd.DataFrame(
    data={
        'name': ['John', 'Mary', 'Andrew'],
        'group': ['HR', 'Accounting', 'Engineering',]})
```

```{code-cell} ipython3
:cell_style: split
:tags: [gridwidth-1-2]

df1
```

```{code-cell} ipython3
:cell_style: split
:tags: [gridwidth-1-2]

df2
```

```{code-cell} ipython3
:tags: [gridwidth-1-2]

# nous ne gardons pas les index de chaque sous-dataframe
pd.concat([df1, df2], ignore_index=True)
# pd.concat([df1, df2], axis=0) # by default concat rows
```

```{code-cell} ipython3
:tags: [gridwidth-1-2]

# nous indexons les dataframes par la colonne 'name'
pd.concat([df1.set_index('name'), df2.set_index('name')])
```

+++ {"tags": ["framed_cell"]}

## en largeur `pd.merge()`

````{admonition} →
pour la réconciliation de données (i.e. le `JOIN` de SQL), voyez cette fois

* la fonction `pd.merge(left, right)`  
  ou sous forme de méthode `left.merge(right)`  

* et la méthode `left.join(right)` - en fait une version simplifiée de `left.merge(...)`

grâce à ces outils, il est possible d'aligner des dataframes sur les valeurs de une ou plusieurs colonnes

````

+++

## alignements

dans les deux cas, `pandas` va ***aligner*** les données  
par exemple on peut concaténer deux tables qui ont les mêmes colonnes, même si elles sont dans le désordre

l'usage typique de `merge()`/`join()` est l'équivalent d'un JOIN en SQL (pour ceux à qui ça dit quelque chose)  

**sans indication**, `merge()` calcule les **colonnes communes** et se sert de ça pour aligner les lignes

```{code-cell} ipython3
# exemple 1
# les deux dataframes ont exactement une colonne en commun: 'name'

df1 = pd.DataFrame(
    data={
        'name': ['Bob', 'Lisa', 'Sue'],
        'group': ['Accounting', 'Engineering', 'HR'],
})

df2 = pd.DataFrame(
    data={
        'name': ['Lisa', 'Bob', 'Sue'],
        'hire_date': [2004, 2008, 2014],
})
```

```{code-cell} ipython3
:cell_style: split
:tags: [gridwidth-1-2]

df1
```

```{code-cell} ipython3
:cell_style: split
:tags: [gridwidth-1-2]

df2
```

```{code-cell} ipython3
:tags: [gridwidth-1-2]

# sans rien préciser, on JOIN sur la colonne commune 'name'

df1.merge(df2)
```

```{code-cell} ipython3
:tags: [gridwidth-1-2]

# on peut aussi l'écrire comme ceci

pd.merge(df1, df2)
```

```{code-cell} ipython3
# exemple 2
# cette fois il faut aligner l'index de gauche
# avec la colonne 'name' à droite

df1 = pd.DataFrame(
    index = ['Bob', 'Lisa', 'Sue'],  # l'index
    data={'group': ['Accounting', 'Engineering', 'HR']})  # une seule colonne

df2 = pd.DataFrame(
    data = {'name': ['Lisa', 'Bob', 'Sue'],
            'hire_date': [2004, 2008, 2014]})
```

```{code-cell} ipython3
:cell_style: split
:tags: [gridwidth-1-2]

df1
```

```{code-cell} ipython3
:cell_style: split
:tags: [gridwidth-1-2]

df2
```

```{code-cell} ipython3
:tags: [gridwidth-1-2]

# du coup ici sans préciser de paramètres, ça ne fonctionnerait pas
# il faut être explicite

df1.merge(df2, left_index=True, right_on='name')
```

```{code-cell} ipython3
:tags: [gridwidth-1-2]

# ou encore

pd.merge(df1, df2, left_index=True, right_on='name')
```

## optionnel: stratégies pour `merge()

comme en SQL, on a à notre disposition plusieurs stratégies pour le `merge` (ou `join`, donc)
le paramètre `how` peut prendre les valeurs suivantes:

* `left`: on ne garde que les clés qui sont dans la première dataframe
* `right`: on ne garde que les clés qui sont dans la seconde dataframe
* `inner`: on ne garde que les clés communes
* `outer`: on garde l'union des clés

(il y a aussi `cross`, mais c'est plus particulier comme usage..)

+++

## concat() *vs* merge()

````{admonition} concat() *vs* merge()
les deux fonctionnalités sont assez similaires sauf que

* `merge` est une opération **binaire**, alors que `concat` est **n-aire**  
   ce qui explique d'ailleurs la différence de signatures: `concat([d1, d2])` *vs* `merge(d1, d2)`

* seule `concat()` supporte un paramètre `axis=`

* `concat()` produit toujours une **addition** (le nombre final de lignes est la somme des nombres de lignes)  
  dans le cas de `merge()` c'est plus compliqué; si on fait un merge 1 pour 1, on ne voit pas trop la différence avec `concat(axis=1)`;  
  mais lorsque dans la colonne de clé, une valeurs apparait plusieurs fois, il se produit un effet **multiplicatif** qu'on ne peut pas obtenir avec `concat()`  

  ```{admonition} un exemple un peu extrême
  :class: dropdown tip

  expérience de la pensée: vous avez deux dataframes A et B qui font chacun 10 lignes, et qui ont toutes les deux, cas extrême, une colonne 'clé' remplie de '1'  
  lorsque vous faites un merge sur cette clé, vous obtenez .. 100 lignes ! c'est donc un effet multiplicatif ici

  ```
  
````
