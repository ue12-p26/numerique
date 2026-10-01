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

# Python-numérique - TP1 `pandas` lecture d'une table de données

+++ {"tags": ["framed_cell"]}

1) importez `pandas`

```{code-cell} ipython3
# le code
import pandas as pd
df = pd.read_csv('iris-TP1.csv', sep=' ', skiprows=3, header=None)
df
```

+++ {"tags": ["framed_cell"]}

2) Lisez le fichier `iris-TP1.csv`
- oui il va y avoir des erreurs mais vous devez les contourner...

**Indices**:
- lisez le help de `pd.read_csv`

- ```py
- regardez les premières lignes du fichier...

```{code-cell} ipython3
# le code
```

+++ {"tags": ["framed_cell"]}

3) Affichez les premières lignes de la dataframe

4) Affichez sa forme, combien de lignes contient-il ?

```{code-cell} ipython3
# le code
```

```{code-cell} ipython3
# le code
```

+++ {"tags": ["framed_cell"]}

5) Affichez la liste de ses colonnes

- oui ce sont des valeurs entières de `0` à `4`

6) Mettez des noms *intelligemment choisis* à la place

**Indice** 
- il suffit pour cela de modifier la liste des colonnes par une liste de noms de colonnes

7) Affichez les 10 dernière lignes

```{code-cell} ipython3
# le code
```

```{code-cell} ipython3
# le code
```

```{code-cell} ipython3
# le code
```

+++ {"tags": ["framed_cell"]}

8) Sélectionnez la sous-dataframe réduites aux 4 colonnes de mesures  

   (vous en connaissez le nom, vous pouvez en faire la liste et la passer à la dataframe)

   

10) Affichez les *petites* statistiques (`count`, `mean`, `std`...) des ces données numériques


12) Affichez les statistiques de la colonne du `Type` des iris

 

14) Combien de types d'iris voyez-vous ?

```{code-cell} ipython3
# le code
```

```{code-cell} ipython3
# le code
```

```{code-cell} ipython3
# le code
```

+++ {"tags": ["framed_cell"]}

Voici comment ajouter une colonne à une dataframe `df`

```{code-cell} ipython3
# exemple d'ajout d'une colonne
import pandas as pd

# je crée une dataframe à partir d'un dictionnaire
data = {'name': ['Jane', 'Bob', 'Charlie'], 'marks math': [16.5, 11.8, 17.6]}
students = pd.DataFrame(data)
display(     students.head()     )

# j'ajoute une nouvelle colonne
students['marks cs'] = [13.7, 7.30, 20]

display(     students.head()     )
```

+++ {"tags": ["framed_cell"]}

12) Créez en `numpy` un tableau de la taille de la dataframe avec des entiers commençant à `0` et espacés de `10`
13) Mettez  cette colonne dans la dataframe sous le non `Id`
14) Mettez cette colonne comme index des lignes de la dataframe
15) Affichez l'index des lignes de la dataframe
16) Affichez les 15 premières lignes de la dataframe

```{code-cell} ipython3
# le code
```

```{code-cell} ipython3
# le code
```

```{code-cell} ipython3
# le code
```

```{code-cell} ipython3
# le code
```

+++ {"tags": ["framed_cell"]}

*end*
