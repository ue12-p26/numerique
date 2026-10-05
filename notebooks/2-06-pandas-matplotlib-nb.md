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

# `df.plot()` / catégories

```{code-cell} ipython3
import pandas as pd
import numpy as np

import matplotlib.pyplot as plt

# juste une commodité pour le notebook, pas important
import IPython
```

+++ {"tags": ["framed_cell"]}

## *plot* une dataframe

````{admonition} →
Les fonctionnalités de `matplotlib` ont été intégrées avec la librairie `pandas`  
afin de faciliter leur utilisation à partir de dataframe et de séries

nous allons illustrer les quelques fonctions sur un petit exemple  
*(référez-vous à la documentation pour aller plus loin dans les réglages -nous resterons ici très simples)*

une `pandas.DataFrame` est une table de données en dimension 2  
`matplotlib` lui apporte des facilités de visualisations
1. de données des `pandas.Series`  
e.g plot, boxplots (boîtes à moustaches), histogrammes, barcharts...
1. de nuages de points 2D ou 3D impliquant plusieurs colonnes

nous allons voir quelques plots intéressants sur l'exemple des iris
````

+++

***

+++ {"tags": ["framed_cell"]}

### la dataframe des `iris`

````{admonition} →
lisons le `csv` des `iris`  avec `pandas`  
affichons les 2 premières lignes

```python
df = pd.read_csv('data/iris.csv')
df.head(2)
->
     SepalLength    SepalWidth    PetalLength    PetalWidth    Name
0    5.1            3.5           1.4            0.2           Iris-setosa
1    4.9            3.0           1.4            0.2           Iris-setosa
```

affichons les petites statistiques  
elles donnent une bonne première idée des données, de leur répartition...

```python
df.head(2)
df.describe()
->       SepalLength SepalWidth PetalLength PetalWidth
count    150.000000  150.000000 150.000000  150.000000
mean     5.843333    3.054000   3.758667    1.198667
std      0.828066    0.433594   1.764420    0.763161
min      4.300000    2.000000   1.000000    0.100000
25%      5.100000    2.800000   1.600000    0.300000
50%      5.800000    3.000000   4.350000    1.300000
75%      6.400000    3.300000   5.100000    1.800000
max      7.900000    4.400000   6.900000    2.500000
```

remarquez que `describe` par défaut  
n'affiche que les 4 colonnes numériques
````

+++ {"tags": ["framed_cell", "level_intermediate"]}

::::{admonition} → **digression**: display d'une dataframe avec IPython
:class: warning dropdown

dans une cellule Jupyter on peut facilement afficher une dataframe, en finissant la cellule par le nom de la dataframe  
mais comment faire si on veut afficher **plusieurs** dataframes dans la même cellule ?

l'approche naíve consisterait à utilsier un `print()`, mais le résultat est moche !  

```python
# vous pouvez essayer, le rendu n'est pas très lisible

by_sex = df.groupby(by='Sex')

for group, subdf in by_sex:
    print(group, subdf.head(1))
```

pour retrouver la même qualité d'affichage (en html)  
il faut utiliser la méthode `IPython.display.display()`  
en important la librairie `IPython`

```python
# comme ceci ça devient lisible

import IPython

for group, subdf in by_sex:
    print(group)
    IPython.display.display(subdf.head(1))
```
::::

```{code-cell} ipython3
# le code
df = pd.read_csv('data/iris.csv')
IPython.display.display(   df.head(2)      )

IPython.display.display(   df.describe()   )
```

+++ {"tags": ["framed_cell"]}

### visualisation avec `df.plot()`

````{admonition} →
la méthode `plot`  des objets de type `pandas.DataFrame` i.e. `df.plot`  
permet une première visualisation simple, rapide et informative **des colonnes numériques**  
qui apporte beaucoup d'informations sur ces données

comme on l'a vu dans le TP sur le tri, `df.plot()` produit:
- autant de plots que de colonnes numériques
- dans chacune, **les abscisses sont prises dans l'index**
- et **les ordonnées dans la colonne** en question

`df.plot()` accepte les mêmes paramètres que la fonction `matplotlib.pyplot.plot`  
elle permet les mêmes réglages  
(en fait elles utilisent toutes les deux la même fonction)

```python
df.plot()
```

```{image} media/iris-plot.png
```
````

```{code-cell} ipython3
# le code
df.plot();
```

:::{admonition} pourquoi c'est mieux qu'avec `plt.plot()` ?
:class: dropdown attention
voici ce qu'on obtient si on essaie de le faire "à la main" en matplotlib  
d'une part c'est plus bavard, et d'autre part on n'a pas la légende...

```{code-cell} ipython3
plt.figure()
plt.plot(df.index, df.SepalLength)
plt.plot(df.index, df.SepalWidth)
plt.plot(df.index, df.PetalLength)
plt.plot(df.index, df.PetalWidth)
plt.show()
```

:::

+++ {"tags": ["framed_cell"]}

### boxplots des colonnes `df.boxplot`

````{admonition} →
un `boxplot` montre:  
- la boite: construite à partir de 
  - la médiane (en vert, aka Q2), 
  - ainsi que Q1 (premier quartile) et Q3 (l'extérieur de la boite, en bleu)
- les moustaches (en noir); il s'agit de datapoints, voir la définition ci-dessous
- les (éventuels) outliers: les points en dehors des moustaches  
  ces points sont potentiellement aberrants ou simplement des extrêmes  

:::{admonition} comment sont définies les moustaches
:class: tip dropdown
en détail, le calcul est le suivant:
- on calcule $IQR = Q3-Q1$
- puis les bornes: 
  - $UP = Q3 + 1.5\times IQR$ 
  - $DOWN = Q1 - 1.5\times IQR$
- enfin les moustaches sont 
  - le plus grand datapoint <= $UP$
  - le plus petit datapoint >= $DOWN$
:::

nous pouvons dessiner les boxplots ensemble  
ils sont alors mis à la même échelle  

```python
df.boxplot()
```

```{image} media/iris-boxplot.png
```

on remarque des outliers dans la colonne des `SepalWidth`  

nous pouvons dessiner les boxplots des colonnes indiquées par une liste

```python
df.boxplot(['SepalWidth', 'PetalWidth'])
```

nous pouvons regrouper les boxplots suivant les valeurs d'une colonne  
(cela nous rappelle `groupby`, c'est très utile)

```python
df.boxplot(['PetalLength'], by='Name')
```

```{image} media/iris-boxplot-by.png
```

nous remarquons  
que les iris *Setosa* ont des `PetalLength` bien plus petits que ceux des autres types d'iris  
ce qui permet de les discriminer des deux autres types d'iris
````

```{code-cell} ipython3
# le code

df.boxplot()

plt.show() # afin de ne pas superposer les plots

df.boxplot(['SepalWidth', 'PetalWidth']);

plt.show()

df.boxplot(['PetalLength'], by='Name')

plt.tight_layout() # le padding
```

+++ {"tags": ["framed_cell"]}

### histogrammes `df.hist()`

````{admonition} →
un histogramme donne la distribution des valeurs d'une colonne

les valeurs de la colonne sont rangées dans des intervalles - ou *bins*  
les nombres de valeurs par intervalle sont affichés

```python
df.hist()
```
```{image} media/iris-hist.png
```

on remarque 3 pics dans `SepalLength`  
correspondent-ils aux 3 types d'iris ?

on peut dessiner l'histogramme d'une seule colonne  
on peut changer des paramètres comme le nombre d'intervalles `bins=`, la couleur `color=`...

```python
df.hist('SepalLength', bins=10, color='lightblue')
```
````

```{code-cell} ipython3
:cell_style: center

# le code
df.hist()
df.hist('SepalLength', bins = 10, color='lightblue')
plt.title('histogramme de la colonne SepalLength');
```

+++ {"tags": ["framed_cell"]}

### barchart `df.plot.bar()`

````{admonition} →
prenons un exemple pour illustrer le dessin des barres  
la dataframe `df_animals` des animaux, leur vitesse et leur durée de vie

barres verticales

```python
df_animals.plot.bar()
```

barres horizontales

```python
df_animals.plot.hbar()
```

une seule colonne

```python
df_animals.plot.barh(x='lifespan')
```

une colonne

```python
df_animals.plot.barh(x='lifespan')
```

une colonne en fonction d'une autre

```python
df_animals.plot.barh(x='lifespan')
```

utilisez le `help`
````

```{code-cell} ipython3
# le code
df_animals = pd.DataFrame({'speed' : [0.1, 17.5, 40, 48, 52, 69, 88],
                   'lifespan' : [2, 8, 70, 1.5, 25, 12, 28]},
                  index = ['snail', 'pig', 'elephant',
                           'rabbit', 'giraffe', 'coyote', 'horse'])

df_animals.plot.bar()

df_animals.plot.barh()

df_animals.plot.bar(x='lifespan', y='speed');
```

+++ {"tags": ["framed_cell"]}

## catégories

### le type de la colonne `'Name'`

````{admonition} →
revenons à nos `iris`

affichons la description de la colonne des types de fleurs `'Name'`

```python
df[['Name']].describe()
->
Name
count	150
unique	3
top	Iris-versicolor
freq	50
```

nous avons 3 noms uniques donc 3 types différents d'iris

comptons le nombre d'observations  
par valeurs dans cette colonne

```python
df['Name'].value_counts()
->
Iris-versicolor    50
Iris-virginica     50
Iris-setosa        50
Name: Name, dtype: int64
```

on remarque que les 3 types sont bien répartis dans les données (1/3)

affichons le type des éléments de la colonne `Name`

```python
df['Name'].dtype
-> 'O'
```

`O` signifie `object`

ce type est `object` ici ce sont des objets de type chaînes de caractères

pourtant ...  
la colonne des noms des `iris` est **plutôt une colonne de type catégorie**  
avec ses 3 valeurs `Iris-versicolor`, `Iris-virginica` et `Iris-setosa`

nous allons changer le type des éléments de la série `df['Name']`  
````

```{code-cell} ipython3
# le code
IPython.display.display(   df[['Name']].describe()   )
df['Name'].value_counts()
```

```{code-cell} ipython3
#le code
df['Name'].dtype
```

### encodage de `'Name'` en catégories

+++

````{admonition} →

la colonne `df['Name']` est de type `pandas.Series`  

avec la méthode `astype('category')` on crée une nouvelle série mais **de type catégoriel**

```python
col = df['Name'].astype('category')
col.head(2)
->
0    Iris-setosa
1    Iris-setosa
Name: Name, dtype: category
Categories (3, object): ['Iris-setosa', 'Iris-versicolor', 'Iris-virginica']
```

**remarquez** l'ordre dans la liste des catégories (`'Iris-setosa'` est à l'indice 0...)



Nous allons maintenant extraire de cette nouvelle colonne  
les **codes** générés par `pandas` pour les trois catégories d'`iris`

**à savoir:** sur une colonne de type `category`  
- `cat` permet d'accéder aux méthodes et attributs des objets de type category  
  (comme `str` le permet sur les colonnes d'éléments de type `str`)
- l'attribut `codes` des colonnes category permet d'accéder aux codes numériques  
  donné par `pandas` aux 3 catégories (dans l'ordre de la liste des catégories)
- on crée une nouvelle colonne `'Name-code'` avec ces codes  
  on regarde ce qu'elle contient

  ```python
  df['Name-code'] = col.cat.codes
  df['Name-code'].value_counts()
  ->
  Name-code
  0    50
  1    50
  2    50
  Name: count, dtype: int64
  ```

-------------------------

À quoi cela va-t-il nous servir ?  
par exemple à améliorer nos visualisations où ces codes peuvent servir de code-couleur lors d'affichage des Iris  
(nous y reviendrons lors de `scatter`)
````

```{code-cell} ipython3
# le code
col = df['Name'].astype('category')
col.head(2)
```

```{code-cell} ipython3
# le code
df['Name-code'] = col.cat.codes
df['Name-code'].value_counts()
```

```{code-cell} ipython3
# et en une seul ligne
df['Name-code'] = df['Name'].astype('category').cat.codes
```

### nuages de points `df.plot.scatter()`

+++

````{admonition} →
pour mettre en valeur des informations sur nos données  
on peut dessiner en 2D les colonnes les unes par rapport aux autres  
avec `df.plot.scatter`

dessinons les `'SepalLength'` en fonction des `'SepalWidth'`

```python
df.plot.scatter(x='SepalLength', y='SepalWidth')
```

avec le paramètre `c=`  

* on peut changer la couleur  
* mais on peut aussi, indiquer une **couleur par point**  
* une idée du code couleur intéressant à utiliser ?

oui, on peut représenter ainsi la catégorie des points  

* chacun des 3 types d'iris, est une valeur entière différente  
* on va considérer cette valeur comme un code dans une table de couleurs
* attention au code `0` (il peut être très peu coloré dans certaines tables)

```python
df.plot.scatter(x='SepalLength', y='SepalWidth', c='Name-code', cmap='viridis');
```

avec le paramètre `s=` on peut changer la taille des points  
ou la taille de chaque point  
par exemple, donnons leur une taille proportionnelle à la largeur des pétales  

```python
plt.scatter(df['SepalLength'], df['SepalWidth'], c=df['Name-code'], s=df['PetalWidth']);
```

ainsi sur un même dessin on peut voir 4 informations  
le nuage, la couleur et la taille des points

il faut travailler un peu les paramètres pour que ce soit visible  
(là la taille est trop peu différenciée, multipliez la)

````

```{code-cell} ipython3
# le code
df.plot.scatter(x='SepalLength', y='SepalWidth');
```

```{code-cell} ipython3
# le code
plt.scatter(df['SepalLength'], df['SepalWidth']);
# plt.xlabel('SepalLength')
# plt.ylabel('SepalWidth')
```

```{code-cell} ipython3
# le code
df.plot.scatter(x='SepalLength', y='SepalWidth', c='Name-code', cmap='viridis');
```

```{code-cell} ipython3
# le code
plt.scatter(df['SepalLength'], df['SepalWidth'], c=df['Name-code'], cmap='viridis')
plt.colorbar();
```

```{code-cell} ipython3
# le code
plt.scatter(df['SepalLength'], df['SepalWidth'], c=df['Name-code'], s=df['PetalWidth']*50);
```

+++ {"tags": ["level_intermediate"]}

### fabriquer son propre type `category`

+++ {"tags": ["level_intermediate"]}

````{admonition} →
:class: danger
*pour les avancés*

avec la technique précédente on n'a pas de **contrôle sur l'ordre** parmi les différentes catégories

imaginez que nous avons maintenant une colonne dont les valeurs uniques sont  
`bad`, `average`, `good`, `excellent`  
cette colonne est clairement une colonne de type catégorie mais **ordonnée**

on peut définir *son propre type catégoriel* avec la fonction  
`pd.CategoricalDtype()`  
qui permet de créer une catégorie ordonnée avec `ordered=True`

en l'appliquand à la colonne des `'Names'` je peux ensuite trier la dataframe  
sur cette colonne

```python
iris_ord_cat = pd.CategoricalDtype(
    categories=['Iris-versicolor', 'Iris-virginica', 'Iris-setosa'],
    ordered=True
)
df['Name'] = df.Name.astype(iris_ord_cat)
df.sort_values(by='Name')
```

````

```{code-cell} ipython3
:tags: [level_intermediate]

# le code
iris_ord_cat = pd.CategoricalDtype(
    categories=['Iris-versicolor', 'Iris-virginica', 'Iris-setosa'],
    ordered=True
)
iris_ord_cat
```

```{code-cell} ipython3
:tags: [level_intermediate]

df.Name = df.Name.astype(iris_ord_cat)
```

```{code-cell} ipython3
:tags: [level_intermediate]

df.sort_values(by='Name').head(4)
```

***
