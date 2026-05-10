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

## 2. read

1. lisez le fichier de données `data/objects-on-the-moon.csv`
2.  affichez sa taille et regardez quelques premières lignes

```{code-cell} ipython3
# votre code
```

## 3. drop

1. vous remarquez une première colonne franchement inutile  
   utiliser la méthode `drop` des dataframes pour supprimer cette colonne de votre dataframe

```{code-cell} ipython3
# votre code
```

## 4. info

1. appelez la méthode `info` des dataframes (`non-null` signifie `non-nan` i.e. non manquant)
2. remarquez une colonne entièrement vide

```{code-cell} ipython3
# votre code
```

## 5. dropna

1. utilisez la méthode `dropna` des dataframes pour supprimer *en place* les colonnes qui ont toutes leurs valeurs manquantes  
   (ici on s'interdit un code qui ferait explicitement référence à la colonne `'Size'`)
2. vérifiez que vous avez bien enlevé la colonne `'Size'`

```{code-cell} ipython3
# votre code
```

## 6. dropna (2)

1. affichez la ligne d'`index` $88$, que remarquez-vous ?
2. utilisez la méthode `dropna` des dataframes pour supprimer
   *en place* les lignes qui ont toutes leurs valeurs manquantes
   (et de nouveau sans faire référence à une ligne en particulier)

```{code-cell} ipython3
# votre code
```

## 7. dtypes

1. utilisez l'attribut `dtypes` des dataframes pour voir le type de vos colonnes
2. que remarquez vous sur la colonne des masses ?

```{code-cell} ipython3
# votre code
```

## 8. unique

1. utilisez la méthode `unique` des `Series`pour en regarder le contenu de la colonne des masses
2. que remarquez vous ?

```{code-cell} ipython3
# votre code
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

## 11. convert

1. sachant que `1 kg = 2.205 lb`  
   créez une nouvelle colonne `'Mass (kg)'` en convertissant les lb en kg  
   arrondissez les flottants en entiers en utilisant `astype`

```{code-cell} ipython3
# votre code
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

## 13. total

1. quel est le poids total des objets sur la lune en kg ?
2. quel est le poids total des objets laissés par les `United States`  ?

```{code-cell} ipython3
# votre code
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

## 16.  tolist

1. faites la liste Python des objets sur la lune  
   ````{admonition} *hint*
   :class: dropdown tip
   voyez la méthode `tolist()` des séries
   ```

```{code-cell} ipython3
# votre code
```

***
