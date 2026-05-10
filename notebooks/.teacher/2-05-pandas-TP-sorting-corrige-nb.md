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

# TP trier une dataframe

+++

**Notions intervenant dans ce TP**

* affichage des données par `plot`
* tri de `pandas.DataFrame` par ligne, par colonne et par index

**N'oubliez pas d'utiliser le help en cas de problème.**

+++

## tri et affichage

+++

### 1. import

importez les librairies `numpy` et `pandas`

```{code-cell} ipython3
# votre code
```

```{code-cell} ipython3
# prune-cell

import numpy as np
import pandas as pd
```

### 2. import (2)

importez la librairie `matplotlib.pyplot` avec le nom `plt`

```{code-cell} ipython3
# votre code
```

```{code-cell} ipython3
# prune-cell

import matplotlib.pyplot as plt
```

### 3. read

lors de la lecture du fichier de données `data/titanic.csv`:
1. gardez uniquement les colonnes `cols` suivantes `'PassengerId'`, `'Survived'`, `'Pclass'`, `'Name'`, `'Sex'`, `'Age'` et `'Fare'`
1. mettez la colonne `PassengerId` comme index des lignes
1. besoin d'aide ? faites `pd.read_csv?`

```{code-cell} ipython3
# votre code
```

```{code-cell} ipython3
# prune-cell

cols = ['PassengerId', 'Survived', 'Pclass', 'Name', 'Sex', 'Age', 'Fare' ]
df = pd.read_csv('data/titanic.csv', index_col='PassengerId', usecols=cols)
```

### 4. plot

en utilisant la méthode `df.plot()`:  

1. plottez la dataframe (pas la série) réduite à la colonne des ages  
1. utilisez le paramètre de `style` `'rv'` (`r` pour rouge et `v` pour le style: points triangulaires)

vous allez voir les points *en vrac*; dans la suite on va s'efforcer de les trier, pour mieux
voir la distribution des âges dans la population concernée

```{code-cell} ipython3
# votre code
```

```{code-cell} ipython3
# prune-cell

df[['Age']].plot(style='rv');
```

### 5. sort

pour commencer on va trier - i.e. mettre les lignes de la  dataframe suivant l'ordre d'une colonne  
en utilisant la méthode `df.sort_values()`:
1. créez une nouvelle dataframe  dont les lignes sont triées  
   dans l'ordre croissant des `'Age'` des passagers
2. pour constater qu'elles sont triées, affichez les 4 premières lignes de la dataframe  
   la colonne des `Age` est triée  
   les lignes ont changé de place dans la table
3. remarquez que l'indexation a été naturellement conservée

```{code-cell} ipython3
# votre code
```

```{code-cell} ipython3
# prune-cell
# on trie dans l'axe des lignes donc `axis=0`

df_sorted = df.sort_values(by='Age', ascending=True, axis=0)
df_sorted.head(4)
```

### 6. plot

1. plottez la colonne des ages de la dataframe triée  
   pour changer un peu on va mettre un style `'b.'`
1. Que constatez-vous ?

```{code-cell} ipython3
# votre code
```

```{code-cell} ipython3
# prune-cell

# pas de changement majeur, la sortie n'est pas triée

df_sorted[['Age']].plot(style='b.');
```

### 7. untangle

la logique de `df.plot()` consiste
* à **utiliser comme abscisses** l'index de la dataframe
* et accessoirement à faire autant de plots que de colonnes - ici on n'en a qu'une

vous tracez donc le point $(804, 0.42)$ puis le point $(756, 0.67)$ ...  
alors que vous voudriez tracer le point $(0, 0.42)$ puis le point $(1, 0.67)$ ...  
c'est à dire: le fait d'utiliser le 'PassengerId' n'est pas bon, on voudrait que les abscisses soient les indices de lignes

1. une solution: voyez la méthode `reset_index()`
   qui permet de transformer l'index en une colonne normale  
1. utiliser cette méthode et regardez ce que vous avez dans l'index ensuite
1. plottez le résultat  

normalement à ce stade vous obtenez la visualisation qu'on cherche

```{code-cell} ipython3
# votre code
```

```{code-cell} ipython3
# prune-cell

df_sorted.reset_index()[['Age']].plot(style='b.');
```

## tri des lignes selon plusieurs critères

quand on trie, que faire en cas d'égalité ?  
en général on choisit plusieurs critères, on trie selon le premier, puis en cas d'égalité selon le second, etc..

*note*: on appelle cela un ordre lexicographique, car c'est - un peu - comme dans un dictionnaire

+++

### 1. rechargez la dataframe

```{code-cell} ipython3
# votre code
```

```{code-cell} ipython3
# prune-cell

cols = ['PassengerId', 'Survived', 'Pclass', 'Name', 'Sex', 'Age', 'Fare' ]
df = pd.read_csv('data/titanic.csv', index_col='PassengerId', usecols=cols)
```

### 2. sort

utilisez `df.sort_values()` pour trier la dataframe suivant la colonne (`'Pclass'`)  
et trier les lignes identiques (passagers de même classe) suivant la colonne (`'Age'`)

```{code-cell} ipython3
# votre code
```

```{code-cell} ipython3
# prune-cell 2.

df_sorted = df.sort_values(by=['Pclass', 'Age'])
df_sorted.head(3)
```

### 3. select

sélectionnez, dans la nouvelle dataframe, la sous-dataframe des gens dont les ages ne sont pas définis  
```{admonition} *hint*
:class: dropdown tip
utiliser la méthode `isna()` sur une série, pour créer un masque de booléens, et appliquer ce masque à la dataframe
```

```{code-cell} ipython3
# votre code
```

```{code-cell} ipython3
# prune-cell

df_sorted_isna = df_sorted[df_sorted['Age'].isna()]
df_sorted_isna
```

### 4. missing ages

combien nous manque-t-il d'ages ?

```{code-cell} ipython3
# votre code
```

```{code-cell} ipython3
# prune-cell

len(df_sorted_isna)
```

### 5. scattered

où sont placés ces passagers dans la data-frame globale triée ?
- en début (voir avec `head`)
- ou en fin (voir avec `tail`)
- ou c'est plus compliqué que ça ?

````{admonition} *hint*
:class: dropdown tip

la façon standard d'afficher un dataframe consiste à montrer le début et la fin  
il y a des situations, comme celle-ci, où on veut avoir une *vision globale* des données,
et pour cela une approche consiste à se ramener à un tableau numpy  
pour cela voyez par exemple `df.no_numpy()`
````

```{code-cell} ipython3
# votre code
```

```{code-cell} ipython3
# prune-cell

# les nan vont plutôt à la fin

df_sorted.tail() 
```

```{code-cell} ipython3
# prune-cell

# pour voir un aperçu de tous les résultats, et visualiser 
# les 3 blocs de nan (un par classe)
# situés effectivement à la fin de chaque groupe de Pclass

df_sorted['Age'].isna().astype(int).to_numpy()
```

```{code-cell} ipython3
# prune-cell

# ou encore, pour afficher les positions des lignes en question, et 
#  nouveau matérialiser les 3 blocs

np.nonzero(df_sorted['Age'].isna())
```

### 6. untangle

trouvez le paramètre de `sort_values()`  
qui permet de mettre ces lignes en début de dataframe lors du tri

```{code-cell} ipython3
# votre code
```

```{code-cell} ipython3
# prune-cell

df_sorted.sort_values(by='Age', ascending=True, axis=0, na_position='first').head()
```

### 7. sort again

produire une nouvelle dataframe en ne gardant que les ages connus,
et triée selon les ages, puis les prix de billet

```{code-cell} ipython3
# prune-cell 7.

df[df.Age.notna()].sort_values(by=['Age', 'Fare'])
```

+++ {"cell_style": "center"}

## tri d'une dataframe selon l'index

reprenez la dataframe du Titanic, en choisissant toujours comme index `PassengerId`  
et triez-là selon les index

```{admonition} *hint*
:class: dropdown tip

voyez `df.sort_index()`
```

```{code-cell} ipython3
# votre code
```

```{code-cell} ipython3
# prune-cell

cols = ['PassengerId', 'Survived', 'Pclass', 'Name', 'Sex', 'Age', 'Fare' ]
df = pd.read_csv('data/titanic.csv', index_col='PassengerId', usecols=cols)

df.sort_index(inplace=True)
df.head(3)
```

***
