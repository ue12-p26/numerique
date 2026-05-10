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

# création de dataframe

*ne pas faire en cours, lire en autonomie*

```{code-cell} ipython3
import pandas as pd
import numpy as np
```

de très nombreuses voies sont possibles pour créer une dataframe par programme  
en voici quelques-unes à titre d'illustration  
voyez la documentation de `pd.DataFrame?` pour les détails

+++

## à partir d'une liste de dicts (les lignes)

```{code-cell} ipython3
lines_as_dicts = [
    {'name': 'snail',    'speed': 0.1,  'lifespan': 2},
    {'name': 'pig',      'speed': 17.5, 'lifespan': 8},
    {'name': 'elephant', 'speed': 40,   'lifespan': 70},
    {'name': 'rabbit',   'speed': 48,   'lifespan': 1.5},
]

pd.DataFrame(lines_as_dicts)
```

+++ {"tags": []}

## à partir d'un dict de list (les colonnes)

```{code-cell} ipython3
# le code

cols_dict = {
    'name' :     ['snail', 'pig', 'elephant', 'rabbit'],
    'speed' :    [0.1,      17.5,         40,       48],
    'lifespan' : [2,           8,         70,      1.5],
}

df = pd.DataFrame(cols_dict)
df
```

+++ {"tags": ["framed_cell"]}

## pareil avec un index

```{code-cell} ipython3
# le même effet que la précédente, si on avait mis 'name' commme index

cols_dict = {
    'speed' :    [0.1,      17.5,         40,       48],
    'lifespan' : [2,           8,         70,      1.5],
}

line_ids =  ['snail', 'pig', 'elephant', 'rabbit']

pd.DataFrame(cols_dict, index = line_ids)
```

+++ {"tags": ["framed_cell"]}

## à partir d'un tableau numpy

````{admonition} →
avec la méthode `pandas.DataFrame`

à partir d'un `numpy.ndarray` qui décrit la *table désirée*  
attention à la forme

et attention au `type` puisque le type des éléments d'un `numpy.ndarray` est homogène  

**remarquez**, sans index

* les index des `2` colonnes sont leurs indices `0` à `1`
* les index des `4` lignes sont leurs indices `0` à `3`

comme ci-dessus on peut passer les index (colonnes et/ou lignes) au constructeur - les détails sont dans la doc
````

```{code-cell} ipython3
# sans préciser, on obtient un RangeIndex dans les deux directions

nd = np.array([
    [ 0.1,  2. ],
    [17.5,  8. ],
    [40. , 70. ],
    [48. ,  1.5],
])

pd.DataFrame(nd)
```

```{code-cell} ipython3
# ici on indique les index dans les deux directions

pd.DataFrame(
    nd,
    index=['snail', 'pig', 'elephant', 'rabbit'],
    columns = ['speed', 'lifespan'],
)
```

## **exercice** : création de df et type des éléments

+++

1. créer un `numpy.ndarray` à partir de la liste suivante

```{code-cell} ipython3
animals = [['snail', 0.1, 2.0],
           ['pig', 17.5, 8.0],
           ['elephant', 40.0, 70.0],
           ['rabbit', 48.0, 1.5],
           ['giraffe', 52.0, 25.0],
           ['coyote', 69.0, 12.0],
           ['horse', 88.0, 28.0]]

# votre code
```

2. Affichez le type des éléments de la table  
   Que constatez-vous ? (U = Unicode)
   Que se passe-t-il si on essaie d'affecter dans la case (2, 0) la chaine `"grey elephant more than 32 charaters long"`
   Remettez-y le mot `"elephant"`

```{code-cell} ipython3
# votre code
```

3. créez une `pandas.DataFrame` **à partir du tableau numpy**  
   et avec pour noms de colonnes `'names'`, `'speed'` et `'lifespan'`

   ````{admonition} le passage par numpy est-il une bonne idée ?
   :class: dropdown
   dans cet exercice on vous impose de passer par le tableau numpy, ce qui en l'espèce n'est pas forcément la meilleure idée  
   mais ça peut être intéressant de voir ce que ça donne ... :)
   ````

```{code-cell} ipython3
# votre code
```

4. affichez la valeur et le type du `'lifespan'` de l'éléphant  
Que constatez-vous ?  
(`object` signifie ici `str`)

```{code-cell} ipython3
# votre code
```

5. affichez la valeur et le type du `'names'` de l'éléphant  
Que constatez-vous ?

```{code-cell} ipython3
# votre code
```

6. avec `loc` ou `iloc`, modifiez la valeur `elephant` par `'grey elephant more than 32 charaters long'`  
affichez la valeur et le type du `'names'` de l'éléphant  
un constat ?

```{code-cell} ipython3
# votre code
```

7. affichez le type des colonnes  
utilisez l'attribut `dtypes` des `pandas.DataFrame`

```{code-cell} ipython3
# votre code
```

8. avec la méthode `pandas.DataFrame.to_numpy`  
affichez le tableau `numpy` sous-jacent de votre data-frame  
affichez le type du tableau  
que constatez-vous ?

```{code-cell} ipython3
# votre code
```

9. modifiez les colonnes `'speed'` et `'lifespan'` de manière à leur donner le type `float`  
(utilisez `pandas.Series.astype` voir les **rappels** en fin d'exercice)

```{code-cell} ipython3
# votre code
```

10. pour comparer, construisez directement une dataframe à partir de l'objet liste  
    a-t-on besoin dans ce cas de convertir les types des colonnes ?

```{code-cell} ipython3
# your code
```

````{admonition} rappels

* `astype`  
la méthode `pandas.Series.astype`, à laquelle vous indiquez un type `float`  
crée (si c'est possible) une nouvelle `pandas.Series` dont les éléments sont de type `float`

* rajouter ou modifier une colonne dans une `pandas.DataFrame`  
revient à modifier ou rajouter une clé à un `dict`
````

+++

````{admonition} explications

* quand les types des colonnes `numpy` ne sont pas homogènes  
`numpy` met un tableau de caractères `Unicode` avec une taille qui permet de tout contenir

* quand les types des colonnes `pandas` ne sont pas homogènes  
sans indication, `pandas` met un `str` Python

* quand dans une data-frame `pandas` on mélange des types de colonnes - genre `float` et `str`  
`pandas` et son tableau `numpy` sous-jacent indiqueront `O` ou `object`  
pour **mixed data types in columns**
````
