---
jupytext:
  custom_cell_magics: kql
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

# exploration interactive

+++

````{admonition} →

pour finir je vous signale un outil commode pour une exploration un peu plus interactive de vos données depuis le notebook

````

```{code-cell} ipython3
import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
```

## le package `itables`

+++

le plus simple c'est de voir un exemple; naturellement il faut avoir d'abord installé le package `itables`

```bash
pip install itables
```

ensuite depuis le notebook il faut initialiser le mode interactif; c'est un peu comme le `%matplotlib ipympl` si on veut; ça se présenterait comme ceci

```python
# pour activer itables depuis un notebook

import itables
itables.init_notebook_mode()
```

```{code-cell} ipython3
import itables

# le mieux c'est de lire ceci dans un notebook
# car dans les supports en HTML ça ne marche pas du tout
# et ça casse même l'affichage usuel
# (mais vous avez un aperçu statique ci-dessous)

itables.init_notebook_mode()
```

et de là on peut afficher les dataframes comme d'habitude, et explorer les données interactivement:

- choisir une pagination
- trier par colonne
- faire des recherches

```{code-cell} ipython3
# je vais prendre le titanic

df = pd.read_csv('data/titanic.csv')
```

et maintenant chaque fois que j'affiche une dataframe j'obtiens ce genre de représentation

```{image} media/itables.png
```

```{code-cell} ipython3
# dans le HTML ça ne donne rien mais vous avez un aperçu statique ci-dessus

df
```

## options

on peut modifier le comportement par défaut; voici quelques idiomes utiles, [allez voir la doc](https://mwouts.github.io/itables) pour plus de détails

```{code-cell} ipython3
# offer more choices in the pagination menu
itables.options.lengthMenu = [3, 5, 10, 25, 50, -1]

# which of these should be the default page size
itables.options.pageLength = 5

# allow for more space
itables.options.maxBytes = "128KB"
```

```{code-cell} ipython3
:scrolled: true

df
```

## `itables.show()`

si vous avez besoin d'appeler explicitement la mise en page d'une dataframe, vous pouvez faire simplement ceci

```python
itables.show(df)
```

+++

et ça peut être utile, par exemple pour lui passer des options spécifiques

```{code-cell} ipython3
# pour afficher par "Pclass" croissant - c'est la 3éme colonne

itables.show(df, pageLength=3, order=[[2, "asc"]])
```

qui donnerait ceci

```{image} media/itables-options.png
```

+++

## voir aussi

- [la documentation](https://mwouts.github.io/itables)
- [un blog sur cet outil](https://blog.jupyter.org/make-your-pandas-or-polars-dataframes-interactive-with-itables-2-0-c64e75468fe6)
