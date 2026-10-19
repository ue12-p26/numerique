---
jupytext:
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
nbhosting:
  title: pivot vs stack/unstack
---

# pivot / unstack / groupby : TP sur les pneus

```{code-cell} ipython3
import pandas as pd
# import numpy as np
from matplotlib import pyplot as plt
```

un magasin de pneus surveille la pression des pneus des véhicules de ses client, il conserve:
- le nom du client (colonne `'name'`)
- l'année de visite du client `'year'`
- le numéro de la visite dans l'année `'visit'` à partir de `1`  
- à chaque visite les mesures des pressions `'pressure'` des pneus avant et des pneus arrière 

+++

1. lire le fichier `data/tyre-pressure.csv`
2. affichez les 2 premières lignes

```{code-cell} ipython3
# your code
df = pd.read_csv(filepath_or_buffer='data/tyre-pressure.csv')
print(df.shape)
df.head(2)
```

## `pivot_table`

+++

3. transformez cette dataframe de manière à avoir:
- en index les années et les visites
- en colonne les client et les types de pneus (avant/arrière)
- comme valeur la pression des pneus
- dans ce genre :

```{image} media/tyre-pressure.png
:width: 500px
:align: center
```

```{code-cell} ipython3
# your code
df_pivoted = df.pivot_table(
    values='pressure',
    index=['year', 'visit'],
    columns=['client', 'tyre pressure'])
df_pivoted
```

4. Si vous avez utilisé `pivot_table`, vérifiez que vous avez autant de valeurs dans cette dataframe que dans celle de départ

```{code-cell} ipython3
# your code
display(
    df_pivoted = df.pivot_table(
        values='pressure',
        index=['year', 'visit'],
        columns=['client', 'tyre pressure'],
    )
)

# en comparant les formes
df.shape[0] == df_pivoted.shape[0] * df_pivoted.shape[1]
```

5. vous remarquez que vous n'avez donc pas besoin de fonction d'aggrégation  
  (la moyenne `mean` calculée sur une seule valeur)

      remplacez `df.pivot_table` par `df.pivot`  
      *(qui permet de modifier la forme d'une dataframe en réorganisant ses index et column values  
      sans proposer de fonction d'aggrégation de données)*

```{code-cell} ipython3
# your code
df_pivoted = df.pivot_table(
    values='pressure',
    index=['year', 'visit'],
    columns=['client', 'tyre pressure'],
)
df_pivoted
```

6. **Utilisation de `unstack`**  
    Nous avons mis, dans l'index des lignes, deux niveaux `year` et `visit` 
    
    Nous aimerions (sans repasser par `pivot` ni `pivot_table`)  
    remonter le niveau des `visit` dans les colonnes afin d'avoir quelque chose comme cela:
    
    ```{image} media/tyre-pressure-unstacked.png
    :width: 650px
    :align: center
    ```

   Faites le en utilisant pour cela la fonction `unstack`
   - elle permet de passer un index de ligne en colonne
   - passez-lui le paramètre `level`  
     (notez que dans la dimension des lignes, notre multi-index contient `0`: `year` et `1` `visit` (donc aussi `-1` car le dernier))

```{code-cell} ipython3
# pd.DataFrame.unstack?
```

```{code-cell} ipython3
# votre code
df_unstacked = df_pivoted.unstack(level=-1)
df_unstacked
```

7. **Utilisation de `stack()`**  
   inversement, `stack` part des colonnes et va vers les index  
   les niveaux dans les multi-index des colonnes sont `0`: `client` et `1`: `tyre`

   En partant de la dataframe pivotée (pas celle faite à partir de `unstack`)  
   Descendez la colonne `tyre pressure` dans les lignes  
   *(on peut passer à `level` l'indice ou le label de la colonne)*

```{code-cell} ipython3
# votre code
df_stacked = df_pivoted.stack(level='tyre pressure')
df_stacked.head(4)
```

8. dans cette dernière dataframe il ne reste qu'un seul niveau de colonne  
   celui des `client`  
   Descendez ce niveau dans les lignes avec `stack`

9. Quel est le type de l'objet que vous obtenez ?

```{code-cell} ipython3
# votre code
type(   df_stacked.stack(level='client')   )
```

10. produire le pivot à la main i.e. sans passer par un `pivot_table`  
   repartons de la dataframe d'origine  
   Il faut mettre les colonnes en index de ligne m(pour créer le multi-index)
   puis appliquer `unstack`...

```{code-cell} ipython3
# votre code
df.set_index(['client', 'year', 'visit', 'tyre pressure']).unstack(level='client').unstack('tyre pressure')
```

11. `groupby`  

   Pour ces données nous n'avons pas besoin de faire de groupement ni d'agrégation : faisons la même chose sur des données que noud devons aggréger  

  Relisons les données du titanic et voyons comment faire une `pivot_table` à-la-main.  

```{code-cell} ipython3
# votre code
df_titanic = pd.read_csv('data/titanic.csv')
df_titanic.head()
```

+++ {"jp-MarkdownHeadingCollapsed": true}

12. Il s'agit de reproduire sans `pivot_table()`:


```{image} media/titanic-pivoted.png
:width: 400px
:align: center
```


hints:
- utilisez un `groupby` pour obtenir une collection de sous-dataframes (par sexe et classe)
- sélectionnez la colonne à aggréger (survivant), pour se ramener à une collection de séries
- lui appliquer une fonction d'aggrégation
- nous avons une série avec un multi-index : il ne reste plus qu'à remonter un des niveau de l'index en colonne (les classes)

conclusion **pivot_table = groupby + unstack**

```{code-cell} ipython3
# votre code
df_titanic.groupby(by=['Sex', 'Pclass'])['Survived'].mean().unstack(level='Pclass')
```
