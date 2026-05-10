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

# TP on the moon

+++

**Notions intervenant dans ce TP**

* suppression de colonnes avec `drop` sur une `DataFrame`
* suppression de colonne entièrement vide avec `dropna` sur une `DataFrame`
* accès aux informations sur la dataframe avec `info`
* valeur contenues dans une `Series` avec `unique` et `value_counts` 
* conversion d'une colonne en type numérique avec `to_numeric` et `astype` 
* accès et modification des chaînes de caractères contenues dans une colonne avec l'accesseur `str` des `Series`
* génération de la liste Python des valeurs d'une série avec `tolist`

```{admonition} pensez à l'aide en ligne (rappels)
:class: dropdown tip

vous avez plein de moyens pour obtenir de l'aide; notamment dans ipython ou jupyter:

- pensez à utiliser la complétion avec Tab
- utiliser 'Shift-Tab' pour voir l'aide de la fonction que vous venez de taper - genre pour voir les paramètres attendus
- on peut aussi faire par exemple `pd.DataFrame.drop?` pour obtenir de l’aide, mais il faut valider la cellule, c'est souvent moins pratique que `Shift-Tab`

il y a aussi la méthode *old-school* qui consiste à appeler `help(une_fonction)`, qui fonctionne dans Python de base - mais en pratique c'est sous-optimal
```

+++

## 1. import

1. importez les librairies `pandas` et `numpy`

```{code-cell} ipython3
# votre code
```

```{code-cell} ipython3
# prune-cell

import pandas as pd
import numpy as np
```

## 2. read

1. lisez le fichier de données `data/objects-on-the-moon.csv`
2.  affichez sa taille et regardez quelques premières lignes

```{code-cell} ipython3
# votre code
```

```{code-cell} ipython3
# prune-cell

df = pd.read_csv('data/objects-on-the-moon.csv')
print(df.shape)
```

```{code-cell} ipython3
# prune-cell

df.head(2)
```

## 3. drop

1. vous remarquez une première colonne franchement inutile  
   utiliser la méthode `drop` des dataframes pour supprimer cette colonne de votre dataframe

```{code-cell} ipython3
# votre code
```

```{code-cell} ipython3
:scrolled: true

# prune-cell

# it's not as if there was an obvious criteria
# that a column should fulfill before we drop it

# although, on second thought:
# the extra column contains the same as the index
# so we might want to check for that first before dropping it

(df.iloc[:, 0] == df.index).all()
```

```{code-cell} ipython3
:scrolled: true

# prune-cell

# the simplest
df.drop(['Unnamed: 0'], axis=1, inplace=True)

# or also
#df.drop(columns=['Unnamed: 0'], inplace = True)

# or yet
# df.drop(columns=df.columns[0], inplace = True)


df.head(2)
```

```{code-cell} ipython3
# prune-cell
df.shape
```

## 4. info

1. appelez la méthode `info` des dataframes (`non-null` signifie `non-nan` i.e. non manquant)
2. remarquez une colonne entièrement vide

```{code-cell} ipython3
# votre code
```

```{code-cell} ipython3
# prune-cell

df.info()
```

## 5. dropna

1. utilisez la méthode `dropna` des dataframes pour supprimer *en place* les colonnes qui ont toutes leurs valeurs manquantes  
   (ici on s'interdit un code qui ferait explicitement référence à la colonne `'Size'`)
2. vérifiez que vous avez bien enlevé la colonne `'Size'`

```{code-cell} ipython3
# votre code
```

```{code-cell} ipython3
# prune-cell

df.dropna(how='all', axis=1, inplace=True)
'Size' in df.columns
```

## 6. dropna (2)

1. affichez la ligne d'`index` $88$, que remarquez-vous ?
2. utilisez la méthode `dropna` des dataframes pour supprimer
   *en place* les lignes qui ont toutes leurs valeurs manquantes
   (et de nouveau sans faire référence à une ligne en particulier)

```{code-cell} ipython3
# votre code
```

```{code-cell} ipython3
# prune-cell

# toutes les valeurs sont manquantes

df.loc[88]
```

```{code-cell} ipython3
# prune-cell
df.dropna(how='all', axis=0, inplace=True)
df.shape
```

## 7. dtypes

1. utilisez l'attribut `dtypes` des dataframes pour voir le type de vos colonnes
2. que remarquez vous sur la colonne des masses ?

```{code-cell} ipython3
# votre code
```

```{code-cell} ipython3
# prune-cell

# la colonne des masses devrait être de type numérique
# mais elle est de type 'object'

df.dtypes
```

## 8. unique

1. utilisez la méthode `unique` des `Series`pour en regarder le contenu de la colonne des masses
2. que remarquez vous ?

```{code-cell} ipython3
# votre code
```

```{code-cell} ipython3
# prune-cell

# on remarque la présence de choses comme '>400'
# que pandas ne peut pas transformer en nombres, d'où les chaines de caractères

df['Mass (lb)'].unique()
```

## 9. to_numeric

1. conservez la colonne `'Mass (lb)'` d'origine  
   (par exemple dans une colonne de nom `'Mass (lb) orig'`)  
1. utilisez la fonction `pd.to_numeric` pour convertir  la colonne `'Mass (lb)'` en numérique  
   en remplaçant les valeurs invalides par la valeur manquante (NaN)
1. naturellement vous vérifiez votre travail en affichant le type de la série `df['Mass (lb)']`
1. combien y a-t-il de données manquantes dans cette colonne ?

```{code-cell} ipython3
# votre code
```

```{code-cell} ipython3
# prune-cell

df['Mass (lb) orig'] = df['Mass (lb)']
```

```{code-cell} ipython3
# prune-cell

df['Mass (lb)'] = pd.to_numeric(df['Mass (lb)'], errors='coerce')
```

```{code-cell} ipython3
# prune-cell

df['Mass (lb)'].dtype
```

```{code-cell} ipython3
# prune-cell

df['Mass (lb)'].isna().sum()
```

## 10. replace

1. cette solution ne vous satisfait pas, vous ne voulez perdre aucune valeur  
   (même au prix de valeurs approchées)  
2. vous décidez vaillamment de modifier les `str` en leur enlevant les caractères `<` et `>`  
   afin de pouvoir en faire des entiers  
   remplacez les `<` et les `>` par des '' (chaîne vide)
   ````{admonition} *hint*
   :class: dropdown tip

   les `pandas.Series` formées de chaînes de caractères sont du type `pandas` `object`  
   mais elle possèdent un accesseur `str` qui permet de leur appliquer les méthodes python des `str`  
   (comme par exemple `replace`)
    ```python
    df['Mass (lb) orig'].str
    ```
    ````
 3. utilisez la méthode `astype` des `Series` pour la convertir finalement en `int`
 4. (optionnel) pour les avancés: sauriez-vous convertir la série en entiers tout en conservant les `nan` ?
    ````{admonition} *hint*
    :class: tip dropdown

    cherchez `pandas.Int64Dtype`
    ````

```{code-cell} ipython3
# votre code
```

```{code-cell} ipython3
# prune-cell 1. 2. 3.

df['Mass (lb) clean'] = df['Mass (lb) orig'].str.replace('<', '').str.replace('>', '').astype(int)
```

```{code-cell} ipython3
# prune-cell 4.

# REMARQUE - pour les avancés
# il existe en Pandas un type qui contient les entiers ET nan
# donc si par exemple on n'avait pas nettoyé la dernière ligne ci-dessus
# on aurait une valeur nan dans la colonne des masses
# et dans ce cas-là on ne peut pas faire .astype(int)
# MAIS on peut le faire avec ce type:

# le type magique se construit comme ceci
int_with_nan = dtype=pd.Int64Dtype()

# converting nan to plain 'int' is not possible
try:
    df['Mass (lb) ints'] = df['Mass (lb)'].astype(int)
except Exception as exc:
    print(f"OOPS: converting nan to int raises {type(exc)}")

print("but we can convert to pandas Int64")
df['Mass (lb) ints'] = df['Mass (lb)'].astype(int_with_nan)
```

```{code-cell} ipython3
# prune-cell

# summarize

mass_columns = [col for col in df.columns if 'Mass' in col]
df_mass = df[mass_columns]
df_mass.dtypes, df_mass.isna().sum()
```

## 11. convert

1. sachant que `1 kg = 2.205 lb`  
   créez une nouvelle colonne `'Mass (kg)'` en convertissant les lb en kg  
   arrondissez les flottants en entiers en utilisant `astype`

```{code-cell} ipython3
# votre code
```

```{code-cell} ipython3
# prune-cell

df['Mass (kg)'] = (df['Mass (lb) clean'] / 2.205).astype(int)
```

## 12. countries

1. Quels sont les pays qui ont laissé des objets sur la lune ?
2. Combien en ont-ils laissé en pourcentage (pas en nombre) ?
   ```{admonition} *hint*
   :class: dropdown tip
   
   regardez les paramètres de `value_counts`
   ```

```{code-cell} ipython3
# votre code
```

```{code-cell} ipython3
:scrolled: true

# prune-cell

df['Country'].unique()
```

```{code-cell} ipython3
:scrolled: true

# prune-cell

df['Country'].value_counts(normalize=True)
```

## 13. total

1. quel est le poids total des objets sur la lune en kg ?
2. quel est le poids total des objets laissés par les `United States`  ?

```{code-cell} ipython3
# votre code
```

```{code-cell} ipython3
# prune-cell

df['Mass (kg)'].sum()
```

```{code-cell} ipython3
:scrolled: true

# prune-cell

df.loc[df['Country'] == 'United States', 'Mass (kg)'].sum()
```

```{code-cell} ipython3
# prune-cell

# plus tard on verra les groupby
# et pour obtenir cette info 
# pour tous les pays d'un coup on fera 

df.groupby(by=['Country'])['Mass (kg)'].sum()
```

## 14. blame

1. quel pays a laissé l'objet le plus léger ?  
   ````{admonition} *hint*
   :class: dropdown tip
   
   voyez les méthodes `Series.idxmin()` et `Series.argmin()`
   ````

```{code-cell} ipython3
# votre code
```

```{code-cell} ipython3
# prune-cell

# using .loc: we need the index, so idxmin()

df.loc[df['Mass (kg)'].idxmin(), 'Country']
```

```{code-cell} ipython3
# prune-cell

# we can also use argmin() that returns a position (integer rank)
# but then, if we want to use the column name there are 2 options

df.iloc[df['Mass (kg)'].argmin()].loc['Country']
```

```{code-cell} ipython3
# prune-cell

# or,

df.iloc[df['Mass (kg)'].argmin(), df.columns.get_loc('Country')]
```

```{code-cell} ipython3
# prune-cell

# note that this approach seems to work in this context
# because we're lucky enough to have a RangeIndex
# but that is "coding by accident", and it's *wrong* 

# WORKS, BUT WRONG nonetheless
df.loc[df['Mass (kg)'].argmin(), 'Country']
```

## 15. memorial

1. y-a-t-il un Memorial sur la lune ?  
   ````{admonition} *hint*
   :class: dropdown tip
   en utilisant l'accesseur `str` de la colonne `'Artificial object'`  
   regardez si une des descriptions contient le terme `'Memorial'`
   ````
2. quel est le pays qui a mis ce mémorial ?

```{code-cell} ipython3
# votre code
```

```{code-cell} ipython3
# prune-cell
np.any(df['Artificial object'].str.contains('Memorial'))
```

```{code-cell} ipython3
# prune-cell
df.loc[df['Artificial object'].str.contains('Memorial'), 'Country']
```

## 16.  tolist

1. faites la liste Python des objets sur la lune  
   ````{admonition} *hint*
   :class: dropdown tip
   voyez la méthode `tolist()` des séries
   ```

```{code-cell} ipython3
# votre code
```

```{code-cell} ipython3
:scrolled: true

# prune-cell
ao = df['Artificial object'].tolist()
ao
```

***
