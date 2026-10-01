---
jupytext:
  cell_metadata_json: true
  encoding: '# -*- coding: utf-8 -*-'
  text_representation:
    extension: .md
    format_name: myst
    format_version: 0.13
    jupytext_version: 1.19.5
kernelspec:
  display_name: Python 3 (ipykernel)
  language: python
  name: python3
---

# TP on the moon (with polars)

```{admonition} ***TRÈS OPTIONNEL***
:class: danger

Pour ceux qui connaissent déjà pandas et qui voudraient se frotter à `polars`: voici le TP 'on the moon' adapté pour cette librairie.

Par contre nous ne fournissons pas de support sur `polars`;  part les quelques généralités c-dessous, vous êtes en complète autonomie pour le faire.
```

+++

**Notions intervenant dans ce TP**

* suppression de colonnes avec `drop` sur une `DataFrame`
* suppression de colonnes entièrement vides (il n'y a pas de `dropna(axis=1)` en polars)
* suppression de lignes entièrement vides avec `filter` et `pl.all_horizontal`
* accès aux informations sur la dataframe avec `schema`, `null_count`, `describe` et `glimpse`
* valeurs contenues dans une `Series` avec `unique` et `value_counts`
* conversion d'une colonne en type numérique avec `cast`
* accès et modification des chaînes de caractères contenues dans une colonne avec le *namespace* `str` des expressions
* génération de la liste Python des valeurs d'une série avec `to_list`

```{admonition} polars vs pandas : les deux différences à garder en tête
:class: important

- **pas d'index** : les lignes n'ont pas de label, seulement une position;  
  il n'y a donc ni `.loc` ni `.iloc`; on sélectionne les lignes avec `filter(<condition>)`  
  et les colonnes avec `select(...)`
- **pas de modification en place** : il n'y a pas de `inplace=True`;  
  chaque opération renvoie une nouvelle dataframe, qu'on réaffecte : `df = df.drop(...)`  
  et pour ajouter ou modifier une colonne on utilise `df.with_columns(...)`
```

+++

## 0. install

1. installez `polars` si vous ne l'avez pas encore fait

```{admonition} hint
:class: dropdown tip
depuis le notebook vous pouvez lancer `pip` avec la *magic* `%pip`
```

```{code-cell} ipython3
:tags: [level_basic]

# votre code
```

## 1. import

1. importez la librairie `polars` (sous le nom `pl`, c'est l'usage)

```{code-cell} ipython3
:tags: [level_basic]

# votre code
```

```{code-cell} ipython3
# prune-cell

import polars as pl
```

## 2. read

1. lisez le fichier de données `data/objects-on-the-moon.csv`
2. affichez sa taille et regardez quelques premières lignes

:::{admonition} itables
:class: dropdown tip
on peut [utiliser `itables` aussi avec une table polars](#label-itables)
:::

```{code-cell} ipython3
:tags: [level_basic]

# votre code
```

```{code-cell} ipython3
# prune-cell

df = pl.read_csv('data/objects-on-the-moon.csv')
print(df.shape)
```

```{code-cell} ipython3
import itables
itables.init_notebook_mode()
```

```{code-cell} ipython3
# prune-cell

df.head(2)
```

## 3. drop

1. vous remarquez une première colonne franchement inutile  
   (c'est l'index d'une dataframe pandas, sauvée telle quelle avec `to_csv`)
2. (optionnel) vérifiez que cette colonne contient bien les entiers $0, 1, 2, ...$
   ````{admonition} *hint*
   :class: dropdown tip

   comparez-la avec `pl.int_range(pl.len())`
   ````
3. utilisez la méthode `drop` des dataframes pour supprimer cette colonne de votre dataframe

```{code-cell} ipython3
:tags: [level_basic]

# votre code
```

```{code-cell} ipython3
# prune-cell

# il n'y a pas d'index en polars, donc on compare
# avec la suite des entiers 0 .. len-1

df.select((pl.first() == pl.int_range(pl.len())).all()).item()
```

```{code-cell} ipython3
# prune-cell

# pas de inplace : on réaffecte
df = df.drop('Unnamed: 0')

# ou encore
# df = df.drop(df.columns[0])

df.head(2)
```

```{code-cell} ipython3
# prune-cell
df.shape
```

## 4. info

1. il n'y a pas de méthode `info` en polars;  
   regardez le résultat de `schema`, `null_count()`, `describe()` et `glimpse()`
2. remarquez une colonne entièrement vide

```{code-cell} ipython3
# votre code
```

```{code-cell} ipython3
# prune-cell

df.schema
```

```{code-cell} ipython3
# prune-cell

# la colonne 'Size' a autant de null que de lignes

df.null_count()
```

```{code-cell} ipython3
# prune-cell

df.describe()
```

```{code-cell} ipython3
# prune-cell

df.glimpse()
```

## 5. drop empty columns

1. supprimez de la dataframe les colonnes qui ont toutes leurs valeurs manquantes  
   (ici on s'interdit un code qui ferait explicitement référence à la colonne `'Size'`)
   ````{admonition} *hint*
   :class: dropdown tip

   il n'y a pas d'équivalent de `dropna(how='all', axis=1)` en polars;  
   mais on peut itérer sur les colonnes d'une dataframe (ce sont des `Series`),  
   et une `Series` a une méthode `null_count()`
   ````
2. vérifiez que vous avez bien enlevé la colonne `'Size'`

```{code-cell} ipython3
# votre code
```

```{code-cell} ipython3
# prune-cell

df = df.select(s.name for s in df if s.null_count() < df.height)
'Size' in df.columns
```

```{code-cell} ipython3
# prune-cell

# variante, en partant des colonnes à supprimer
# df = df.drop(s.name for s in df if s.null_count() == df.height)
```

## 6. drop empty rows

1. affichez la ligne en position $88$, que remarquez-vous ?  
   (en polars c'est une position, pas un label d'index)
2. supprimez de la dataframe les lignes qui ont toutes leurs valeurs manquantes  
   (et de nouveau sans faire référence à une ligne en particulier)
   ````{admonition} *hint*
   :class: dropdown tip

   pensez à `filter`, `pl.all()` et `pl.all_horizontal()`
   ````

```{code-cell} ipython3
# votre code
```

```{code-cell} ipython3
# prune-cell

# toutes les valeurs sont manquantes

df.row(88, named=True)
```

```{code-cell} ipython3
# prune-cell

# pl.all() désigne toutes les colonnes
# pl.all_horizontal() fait un "et" logique ligne par ligne

df = df.filter(~pl.all_horizontal(pl.all().is_null()))
df.shape
```

```{code-cell} ipython3
# prune-cell

# attention : sans index, les lignes suivantes "remontent"
# il n'y a plus de trou dans la numérotation (contrairement à pandas)
# ici ça ne se voit pas car c'était la dernière ligne
```

## 7. dtypes

1. utilisez l'attribut `dtypes` (ou `schema`) des dataframes pour voir le type de vos colonnes
2. que remarquez vous sur la colonne des masses ?

```{code-cell} ipython3
# votre code
```

```{code-cell} ipython3
# prune-cell

# la colonne des masses devrait être de type numérique
# mais elle est de type String

# au passage, 'Year' est bien de type entier, alors qu'en pandas
# elle était en flottant à cause de la ligne vide :
# en polars les entiers acceptent nativement les valeurs manquantes (null)

df.schema
```

## 8. unique

1. utilisez la méthode `unique` des `Series` pour regarder le contenu de la colonne des masses
2. que remarquez vous ?

```{code-cell} ipython3
# votre code
```

```{code-cell} ipython3
# prune-cell

# on remarque la présence de choses comme '>400'
# que polars ne peut pas transformer en nombres, d'où les chaines de caractères

df['Mass (lb)'].unique(maintain_order=True).to_list()
```

## 9. cast

1. conservez la colonne `'Mass (lb)'` d'origine  
   (par exemple dans une colonne de nom `'Mass (lb) orig'`)
   ````{admonition} *hint*
   :class: dropdown tip

   `df.with_columns(<expression>.alias('nouveau nom'))`
   ````
1. utilisez la méthode `cast` des expressions pour convertir la colonne `'Mass (lb)'` en flottant  
   en remplaçant les valeurs invalides par la valeur manquante (`null`)
   ````{admonition} *hint*
   :class: dropdown tip

   regardez le paramètre `strict` de `cast`  
   c'est l'équivalent de `pd.to_numeric(..., errors='coerce')`
   ````
1. naturellement vous vérifiez votre travail en affichant le type de la série `df['Mass (lb)']`
1. combien y a-t-il de données manquantes dans cette colonne ?

```{code-cell} ipython3
# votre code
```

```{code-cell} ipython3
# prune-cell

df = df.with_columns(pl.col('Mass (lb)').alias('Mass (lb) orig'))
```

```{code-cell} ipython3
# prune-cell

# sans strict=False, la conversion de '>400' déclenche une exception

df = df.with_columns(pl.col('Mass (lb)').cast(pl.Float64, strict=False))
```

```{code-cell} ipython3
# prune-cell

df['Mass (lb)'].dtype
```

```{code-cell} ipython3
# prune-cell

df['Mass (lb)'].null_count()
```

## 10. replace

1. cette solution ne vous satisfait pas, vous ne voulez perdre aucune valeur  
   (même au prix de valeurs approchées)
2. vous décidez vaillamment de modifier les `str` en leur enlevant les caractères `<` et `>`  
   afin de pouvoir en faire des entiers  
   remplacez les `<` et les `>` par des '' (chaîne vide)  
   et rangez le résultat dans une colonne `'Mass (lb) clean'`
   ````{admonition} *hint*
   :class: dropdown tip

   les expressions polars de type `String` possèdent un *namespace* `str`  
   qui donne accès à des méthodes sur les chaînes (comme par exemple `replace_all`)
    ```python
    pl.col('Mass (lb) orig').str
    ```
   ````
3. utilisez `cast` pour la convertir finalement en entier (`pl.Int64`)
4. (optionnel) en pandas il fallait un type spécial (`pd.Int64Dtype`)  
   pour avoir des entiers **et** des valeurs manquantes;  
   essayez de convertir la colonne `'Mass (lb)'` de la question 9 en entiers, que se passe-t-il ?

```{code-cell} ipython3
# votre code
```

```{code-cell} ipython3
# prune-cell 1. 2. 3.

# replace_all accepte une regex
df = df.with_columns(
    pl.col('Mass (lb) orig')
    .str.replace_all('[<>]', '')
    .cast(pl.Int64)
    .alias('Mass (lb) clean')
)

# ou encore, puisque ces caractères sont en début de chaîne
# pl.col('Mass (lb) orig').str.strip_chars_start('<>').cast(pl.Int64)
```

```{code-cell} ipython3
# prune-cell 4.

# rien de spécial : en polars tous les types entiers acceptent les null
# il n'y a pas besoin d'un type particulier

df = df.with_columns(pl.col('Mass (lb)').cast(pl.Int64).alias('Mass (lb) ints'))
df['Mass (lb) ints'].dtype, df['Mass (lb) ints'].null_count()
```

```{code-cell} ipython3
# prune-cell

# summarize

df_mass = df.select(pl.col('^Mass.*$'))
df_mass.schema, df_mass.null_count()
```

## 11. convert

1. sachant que `1 kg = 2.205 lb`  
   créez une nouvelle colonne `'Mass (kg)'` en convertissant les lb en kg  
   arrondissez les flottants en entiers en utilisant `cast`

```{code-cell} ipython3
# votre code
```

```{code-cell} ipython3
# prune-cell

df = df.with_columns(
    (pl.col('Mass (lb) clean') / 2.205).cast(pl.Int64).alias('Mass (kg)')
)
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
# prune-cell

df['Country'].unique(maintain_order=True).to_list()
```

```{code-cell} ipython3
# prune-cell

df['Country'].value_counts(normalize=True, sort=True)
```

## 13. total

1. quel est le poids total des objets sur la lune en kg ?
2. quel est le poids total des objets laissés par les `United States` ?

```{code-cell} ipython3
# votre code
```

```{code-cell} ipython3
# prune-cell

df['Mass (kg)'].sum()
```

```{code-cell} ipython3
# prune-cell

# l'équivalent de df.loc[mask, col] : filter puis on prend la colonne

df.filter(pl.col('Country') == 'United States')['Mass (kg)'].sum()
```

```{code-cell} ipython3
# prune-cell

# plus tard on verra les group_by
# et pour obtenir cette info
# pour tous les pays d'un coup on fera

df.group_by('Country').agg(pl.col('Mass (kg)').sum()).sort('Mass (kg)', descending=True)
```

## 14. blame

1. quel pays a laissé l'objet le plus léger ?
   ````{admonition} *hint*
   :class: dropdown tip

   voyez la méthode `Series.arg_min()`  
   (il n'y a pas de `idxmin()` puisqu'il n'y a pas d'index)
   ````
2. y a-t-il plusieurs objets ex-aequo ?

```{code-cell} ipython3
# votre code
```

```{code-cell} ipython3
# prune-cell

# arg_min() renvoie une position; et comme il n'y a pas d'index
# la position est la seule façon de désigner une ligne :
# pas de piège comme avec loc / iloc en pandas

df['Country'][df['Mass (kg)'].arg_min()]
```

```{code-cell} ipython3
# prune-cell

# la façon idiomatique : filtrer sur la valeur minimale
# avantage, on voit tous les ex-aequo

df.filter(pl.col('Mass (kg)') == pl.col('Mass (kg)').min()).select(
    'Artificial object', 'Country', 'Mass (lb) orig', 'Mass (kg)'
)
```

```{code-cell} ipython3
# prune-cell

# remarque : la conversion en kg par cast tronque
# on peut départager avec la masse en lb

df.bottom_k(1, by='Mass (lb) clean').select('Artificial object', 'Country', 'Mass (lb) clean')
```

## 15. memorial

1. y-a-t-il un Memorial sur la lune ?
   ````{admonition} *hint*
   :class: dropdown tip
   en utilisant le namespace `str` de la colonne `'Artificial object'`  
   regardez si une des descriptions contient le terme `'Memorial'`
   ````
2. quel est le pays qui a mis ce mémorial ?

```{code-cell} ipython3
# votre code
```

```{code-cell} ipython3
# prune-cell
df['Artificial object'].str.contains('Memorial').any()
```

```{code-cell} ipython3
# prune-cell
df.filter(pl.col('Artificial object').str.contains('Memorial'))['Country']
```

## 16. to_list

1. faites la liste Python des objets sur la lune
   ````{admonition} *hint*
   :class: dropdown tip
   voyez la méthode `to_list()` des séries
   ````

```{code-cell} ipython3
# votre code
```

```{code-cell} ipython3
# prune-cell
ao = df['Artificial object'].to_list()
ao
```

***
