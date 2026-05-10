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

# conditions et masques

```{code-cell} ipython3
import pandas as pd
import numpy as np
```

+++ {"tags": ["framed_cell"]}

## conditions sur une dataframe

````{admonition} →
dans les analyses de données, il est fréquent de **sélectionner des données par des conditions**  
(qui peuvent s'appliquer, selon le contexte, à tout un tableau, ou un morceau précis comme une colonne, une ligne, un sous-tableau...)

en `pandas`, comme en `numpy`, les fonctions sont **vectorisées** par souci de rapidité du code  
→ il ne faut **jamais itérer avec un `for-python`** sur les valeurs d'une table  
(les itérations se font dans le code des fonctions `numpy` et `pandas`)

comme en `numpy`, une expression conditionnelle va s'appliquer à toute la structure  
et retourner une structure du même forme, mais avec des résultats booléens  
comme [on avec les masques `numpy`](#label-numpy-mask)

exemple:

* `titanic['Age']` : un objet de type `Series` à valeurs entières
* `titanic['Age'] < 12` : un objet de type `Series` à valeurs booléennes

(voir ci-dessous)

````

+++

***

+++ {"tags": ["framed_cell"]}

(label-pandas-mask)=

## conditions et masques

### structure d'un masque

````{admonition} →
regardons cet exemple en détail:  
quels passagers avaient moins de 12 ans ?

```python
df = pd.read_csv('data/titanic.csv', index_col='PassengerId')

children = df['Age'] < 12 # l'opérateur < est vectorisé 
children

-> PassengerId
    552    False  # <- le passager de PassengerId 552 a plus de 12 ans
    638    False
           ...
    326    False
    396    False
    832     True  # <- celui-ci par contre a strictement moins de 12 ans
    Name: Age, Length: 891, dtype: bool
```

cette expression retourne une `pandas.Series`  
dont le type est `bool` - appelée **un masque**   
avec, pour chaque ligne, la réponse au test

en `pandas` comme en `numpy` pour combiner les conditions  

* on utilise `&` (et) `|` (ou) et `~` (non)  
ou les `numpy.logical_and`, `numpy.logical_or`, `numpy.logical_not`

* et **surtout pas** `and`, `or` et `not` (opérateurs `Python` non vectorisés)
* on **parenthèse toujours** les expressions

```python
girls = (df['Age'] < 12) & (df['Sex'] == 'female')
girls.sum()
-> 32
```

```{attention}

c'est **très important** de bien mettre des parenthéses  
car les opérateurs bitwise (`&` et autres) ont des **précédences** (priorités)  
qui sont non intuitives, et très différentes des opérateurs logiques (`and` et autres)
```

on pourra ensuite utiliser ces tableaux de booléens  

* pour leur appliquer des fonctions (comme `sum`)  
* ou comme des masques pour sélectionner des sous-tableaux
````

```{code-cell} ipython3
# le code
df = pd.read_csv('data/titanic.csv', index_col='PassengerId')
children = df['Age'] < 12
children
```

```{code-cell} ipython3
children.dtype
```

```{code-cell} ipython3
girls = (df['Age'] < 12) & (df['Sex'] == 'female')
girls.sum()
```

+++ {"tags": ["framed_cell"]}

### indexation par un masque

````{admonition} →
comment utiliser un masque ?  
en pratique, le plus souvent on est intéressés par **les lignes** qui correspondent au masque

et pour les "extraire" de la dataframe on va tout simplement  
**indexer la dataframe par le masque**  
c'est-à-dire en français: écrire `df[mask]`  

```python
# pour construire la dataframe réduite aux filles
girls_df = df[girls]
girls_df.head(2)
->
             Survived  Pclass                              Name     Sex  Age  SibSp  Parch Ticket      Fare    Cabin  Embarked  
PassengerId                                                                    
238                 1       2  Collyer, Miss. Marjorie "Lottie"  female  8.0  0      2     C.A. 31921  26.250  NaN    S 
375                 0       3        Palsson, Miss. Stina Viola  female  3.0  3      1     349909      21.075  NaN    S   
```

```{admonition} ou encore avec .loc
:class: admonition-small

en fait on fera même plutôt `df.loc[mask]`, mais bon, on n'a pas encore parlé de `.loc` ...
```
````

```{code-cell} ipython3
# le code

girls_df = df[girls]
girls_df.head(2)
```

```{code-cell} ipython3
# avec .loc (même si on ne l'a pas encore vu...)

girls_df = df.loc[girls]
girls_df.head(2)
```

+++ {"tags": ["framed_cell"]}

## `value_counts()`

````{admonition} →
comment calculer le nombre d'enfants ?  
par exemple nous pouvons sommer les `True` avec `pandas.Series.sum`

```python
children = df['Age'] < 12
children.sum()
-> 68
```

ou utiliser la méthode `value_counts()` qui compte les occurrences dans une colonne  

```python
children = df['Age'] < 12
children.value_counts()
-> False    823
   True      68
   Name: count, dtype: int64
```

ainsi parmi les passagers dont on connait l'âge, **`68` passagers,  ont moins de `12` ans**  
on reviendra tout de suite sur les données manquantes
````

```{code-cell} ipython3
children.sum()
```

```{code-cell} ipython3
children.value_counts()
```

## valeurs manquantes

+++ {"tags": ["framed_cell"]}

### contexte général

````{admonition} →
souvent, certaines colonnes ont des valeurs manquantes...  
dans l'exemple du Titanic, ce sont les valeurs qui ne sont pas renseignées dans le `csv`  

on a souvent besoin de les trouver, les compter, et si nécessaire les éliminer

`NA` signifie Non-Available et `NaN` Not-a-Number

sur les `DataFrame` et les `Series`, la méthode `isna()` construit **un masque**  
du même type (DataFrame ou Series donc), et à valeurs booléennes où

* `True` signifie que la valeur est manquante
* `False` que la valeur ne l'est pas

il existe son contraire qui est `notna()`  
il existe aussi des synonymes `isnull()` et `notnull()` - **préférez** `isna`

````

+++

***

+++ {"tags": ["framed_cell"]}

### valeurs manquantes dans une colonne

````{admonition} →
regardons les valeurs manquantes d'une colonne

```python
df['Age'].isna()
->  PassengerId
    552    False
    638    False
    499    False
    261     True
    395    False
           ...
    396    False
    832    False
    Name: Age, Length: 891, dtype: bool
```

l'age du passager d'`Id` 261 est manquant  
on peut le vérifier dans le fichier en format `csv`:

```
261,0,3,"Smith, Mr. Thomas",male,,0,0,384461,7.75,,Q
                                ^^
```

combien d'ages sont manquants ?

```python
df['Age'].isna().sum()
-> 177
```

on y reviendra
````

```{code-cell} ipython3
:scrolled: true

# le code
df['Age'].isna()
```

```{code-cell} ipython3
:lines_to_next_cell: 2

df['Age'].isna().sum()
```

```{code-cell} ipython3
# remarquez qu'on peut tout aussi bien
# utiliser le sum() de np ou de Python
import numpy as np
np.sum(df['Age'].isna()), sum(df['Age'].isna())
```

+++ {"tags": ["framed_cell"]}

### valeurs manquantes sur une dataframe

````{admonition} →
la méthode `isna()` s'applique aussi à une dataframe  
et elle retourne une **dataframe de booléens** où - sans surprise :  

* `True` signifie que la valeur est manquante
* `False` que la valeur ne l'est pas

regardons les valeurs manquantes d'une dataframe

```python
df.isna()
->              Survived  Pclass   Name    Sex  ...  Ticket   Fare  Cabin  Embarked
PassengerId                                  ...
552             False   False  False  False  ...   False  False   True     False
638             False   False  False  False  ...   False  False   True     False
499             False   False  False  False  ...   False  False  False     False
261             False   False  False  False  ...   False  False   True     False
395             False   False  False  False  ...   False  False  False     False
...               ...     ...    ...    ...  ...     ...    ...    ...       ...
463             False   False  False  False  ...   False  False  False     False
287             False   False  False  False  ...   False  False   True     False
326             False   False  False  False  ...   False  False  False     False
396             False   False  False  False  ...   False  False   True     False
832             False   False  False  False  ...   False  False   True     False

[891 rows x 11 columns]
```

vous remarquez une dataframe de la **même taille** que `df`
````

```{code-cell} ipython3
# le code
df.isna()
```

+++ {"jp-MarkdownHeadingCollapsed": true, "tags": ["framed_cell"]}

### compter les valeurs manquantes

````{admonition} →
comme en `numpy` je peux appliquer une fonction - ici `sum()` - en précisant l'`axis`  
`0` on applique la fonction dans l'axe des lignes (le défaut): on obtient un résultat par colonne  
`1` on applique la fonction dans l'axe des colonnes  
l'objet retourné est une série contenant le résultat de la fonction

exemple avec la somme (`sum`) des valeurs manquantes sur l'axe des lignes `axis=0`  
qui `sum` les lignes entre elles - le résultat est par colonne donc

```python
df.isna().sum()       # les deux formes sont
df.isna().sum(axis=0) # équivalentes

Survived      0
Pclass        0
Name          0
Sex           0
Age         177
SibSp         0
Parch         0
Ticket        0
Fare          0
Cabin       687
Embarked      2
dtype: int64
```

nous remarquons des valeurs manquantes dans les colonnes `Cabin`, `Age` et `Embarked`

```{admonition} note
:class: attention

pour souligner une différence avec `numpy`: comparez le comportement

* de `array.sum()`
* et `df.sum()`  
(on y revient ci-dessous)
```
````

+++ {"tags": ["framed_cell"]}

### dans l'autre direction (axis=1)

````{admonition} →
exemple de la somme des valeurs manquantes sur l'axe des colonnes

```python
df.isna().sum(axis=1):
->  PassengerId
    552    1
    638    1
    499    0
    261    2
    395    0
          ..
    463    0
    287    1
    326    0
    396    1
    832    1
    Length: 891, dtype: int64
```

le passager d'id `261` a deux valeurs manquantes
````

```{code-cell} ipython3
# le code
df.isna().sum()       # c'est la
df.isna().sum(axis=0) # même chose
```

```{code-cell} ipython3
# le code
df.isna().sum(axis=1)
```

+++ {"tags": ["framed_cell"]}

### les fonctions `numpy` d'agrégation

````{admonition} →
les méthodes `numpy` d'agrégation (comme `sum()` et `mean()` et `min()` etc...) s'appliquent sur des `pandas.DataFrame` et des `pandas.Series`

on précise l'`axis`  
`0` pour l'axe des lignes (c'est le mode par défaut)  
`1` pour l'axe des colonnes  

différence avec `numpy`, si on appelle sans préciser `axis`

* avec **numpy**: on obtient le résultat **global**  
* avec **pandas**: par défaut `axis=0`, on agrège sur l'axe des lignes

**si on désire le résultat global**
1. soit on applique la fonction deux fois  
   e.g. `df.isna().sum().sum()`
1. soit on peut passer par le sous-tableau `numpy`  
  et là la fonction `numpy.sum()` donnera le résultat global

la méthode `pandas.DataFrame.to_numpy` retourne le tableau `numpy.ndarray` de la DataFrame `pandas`

```python
df.isna().to_numpy()
-> array([[False, False, False, ..., False,  True, False],
          [False, False, False, ..., False, False, False],
          ...,
          [False, False, False, ..., False,  True, False],
          [False, False, False, ..., False,  True, False]])
```

on somme

```python
np.sum(df.isna().to_numpy())
df.isna().to_numpy().sum()
-> 866
```

il y a `866` valeurs manquantes dans toute la data-frame

```{admonition} note
:class: attention

remarque: contrairement à ce qu'on avait vu en `numpy`, ici on ne pourrait pas faire `df.isna().sum(axis=(0, 1))`  
il faut faire en deux fois `df.isna().sum().sum()`
```
````

```{code-cell} ipython3
df.isna().sum().sum()
```

```{code-cell} ipython3
# le code
df.isna().to_numpy()
```

```{code-cell} ipython3
# le code
np.sum(df.isna().to_numpy())
df.isna().to_numpy().sum()
```

***

+++

## **exercice** valeurs uniques

+++

1. lisez la data-frame du titanic `df`

```{code-cell} ipython3
# votre code
```

```{code-cell} ipython3
:lines_to_next_cell: 2

# prune-cell 1.

df = pd.read_csv("data/titanic.csv")
```

2. utilisez la méthode `pd.Series.unique` (1) pour compter le nombre de valeurs uniques  
des colonnes `'Survived'`, `'Pclass'`, `'Sex'` et `'Embarked'`  
vous pouvez utiliser un for-python pour parcourir la liste `cols` des noms des colonnes choisies

(1) servez-vous du help `pd.Series.unique?`

```{code-cell} ipython3
# votre code
```

```{code-cell} ipython3
:lines_to_next_cell: 2

# prune-cell 2.

cols = ['Survived', 'Pclass', 'Sex', 'Embarked']
for c in cols:
    print(f"{c} unique values: {df[c].unique()}")
```

3. utilisez l'expression `df[cols]` pour sélectionner la sous-dataframe réduite à ces 4 colonnes  
   et utilisez l'attribut `dtypes` des `pandas.DataFrame` pour afficher le type de ces 4 colonnes

```{code-cell} ipython3
# votre code
```

```{code-cell} ipython3
# prune-cell 3.

minidf = df[cols]
print(f"{minidf.dtypes=}")

# séparateur
print(10*'-')

# du coup on pourrait aussi faire
for c in minidf.columns:
    print(f"column {c:>12} has type {minidf.dtypes[c]} =?= {df[c].dtype}")
```

4. que constatez-vous ?  
quel type serait plus approprié pour ces colonnes ?

```{code-cell} ipython3
# votre code
```

prune-cell 4.

* la colonne Survived pourrait être un booléen
* les trois autres colonnes sont des catégories (nombre fini de valeurs possibles)

+++

***

+++

## **exercice** conditions

+++

1. lisez la data-frame des passagers du titanic

```{code-cell} ipython3
# votre code
```

```{code-cell} ipython3
# prune-cell 1.

df = pd.read_csv('data/titanic.csv', index_col='PassengerId')
df.head(2)
```

2. comptez les valeurs manquantes: dans toute la table, par colonne et par ligne

```{code-cell} ipython3
# votre code
```

```{code-cell} ipython3
# prune-cell 2.

# df.isna().to_numpy().sum(), df.isna().sum(axis=1), df.isna().sum(axis=0),

print(10*'-', 'total')
print(df.isna().sum().sum())
print(10*'-', 'par colonne')
print(df.isna().sum())
print(10*'-', 'par ligne')
print(df.isna().sum(axis=1))
```

1. calculez le nombre de classes du bateau

```{code-cell} ipython3
# votre code
```

```{code-cell} ipython3
# prune-cell 3.

len(df['Pclass'].unique())
```

```{code-cell} ipython3
# prune-cell 3.

len(df['Pclass'].value_counts())
```

4. calculez le taux d'hommes et de femmes  
   indice: voyez les paramètres optionnels de `Series.value_counts()`

```{code-cell} ipython3
# votre code
```

```{code-cell} ipython3
# prune-cell 4.

df['Sex'].value_counts()/len(df)

# ou encore
df['Sex'].value_counts(normalize=True)#/len(df)
```

5. calculez le taux de personnes entre 20 et 40 ans (bornes comprises)

```{code-cell} ipython3
# votre code
```

```{code-cell} ipython3
# prune-cell 5.

((df['Age'] >= 20) & (df['Age'] <= 40)).sum()/len(df)
```

6. calculez le taux de survie des passagers

```{code-cell} ipython3
# votre code
```

```{code-cell} ipython3
# prune-cell 6.

(df.Survived == 1).mean()
```

7. calculez le taux de survie des hommes et des femmes par classes  
   i.e. pour chacun des 6 groupes (hommes/femmes) x (classe 1/2/3)  
   (notez qu'on reverra ces décomptes d'une autre manière)

```{code-cell} ipython3
# votre code
```

```{code-cell} ipython3
# prune-cell

# DISCLAIMER

# OF COURSE: this is better done with a pivot_table()
# here we just feel the pain of doind it manually..
```

```{code-cell} ipython3
# prune-cell 7.

# NOTE: in Python 'class' is a keyword

# for one group, say
cls, sex = 1, 'female'

# the corresponding group is
group_df = df[ (df.Sex == sex) & (df.Pclass == cls) ]

# and the corresponding survival rate is
rate = group_df.Survived.sum() / len(group_df)

print(f"for {cls=} and {sex=} we have a survival rate of {rate=:.2f}")
```

```{code-cell} ipython3
# prune-cell

# so all we need to do is loop over the possible groups

for cls in df.Pclass.unique():
    for sex in df.Sex.unique():
        group_df = df[ (df.Sex == sex) & (df.Pclass == cls) ]
        rate = group_df.Survived.sum() / len(group_df)
        print(f"for {cls=} and {sex=} we have a survival rate of {rate=:.2f}")        
```

```{code-cell} ipython3
# prune-cell

# this was not required, but out of curiosity
# how coud we store these results in a dataframe to mimick the outcome of pivot_table

results = {}

for cls in df.Pclass.unique():
    for sex in df.Sex.unique():
        group_df = df[ (df.Sex == sex) & (df.Pclass == cls) ]
        rate = group_df.Survived.sum() / len(group_df)
        # index results by the group tuple
        results[cls, sex] = rate

# now we can create a series from this dict
series = pd.Series(results)
```

```{code-cell} ipython3
# prune-cell

# we're almost there, just "move" the index level 1 to the columns space

series.unstack()
```

***
