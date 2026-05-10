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
  nbconvert_exporter: python
  pygments_lexer: ipython3
---

# Python-numérique - introduction

+++

````{admonition} Rappel

**Note**: pour un rendu optimal, pensez à installer les *requirements* du cours avec

```bash
pip install -r requirements.txt
```
````

+++

## contenu de ce notebook

(sauter si déjà acquis)

````{admonition} →

comprendre que des objets qui semblent aussi différents qu'une matrice, une table de mesures hétérogènes, une série temporelle, une image...

sont en fait une même structure de données

que celle-ci n'existe pas en `python`

d'où le recours à la librairie `numpy`
````

+++

## objectifs de Python-numérique

````{admonition} →

vous êtes désormais capables de lire et d'écrire du code **python simple**

vous savez le mettre en œuvre dans un **notebook**

nous allons maintenant aborder le cours de **Python-numérique**

il s'agit des fonctionnalités de base de **data-science**

issues de librairies python comme `numpy`, `pandas`, `matplotlib.pyplot`...


commençons par **importer** ces librairies dans Python

```python
import numpy as np
import pandas as pd
from matplotlib import pyplot as plt
```

il peut être nécessaire de les installer avec `pip install numpy pandas matplotlib`  
(ou `%pip install numpy pandas matplotlib` dans une cellule de vos notebooks)

et regarder la version de ces librairies

```python
np.__version__
pd.__version__
```
````

```{code-cell} ipython3
#!pip install numpy pandas matplotlib
```

```{code-cell} ipython3
# prune-cell
# je coupe en trois morceaux pour éviter un timeout du coté de readthedocs
```

```{code-cell} ipython3
# manière classique d'importer les librairies de data-science
# NB: la toute première fois qu'on importe une librairie 
# après un pip install, ça peut être un peu long...

import numpy as np
```

```{code-cell} ipython3
import pandas as pd
```

```{code-cell} ipython3
from matplotlib import pyplot as plt
```

```{code-cell} ipython3
# vérifier les versions de ces librairies

print(f'numpy version {np.__version__}')
print(f'pandas version {pd.__version__}')

import matplotlib as mpl # la version de matplotlib
print(f'matplotlib version {mpl.__version__}')
```

## les données


````{admonition} →

qui dit data-science dit **données**

données qui seront **manipulées** dans des programmes Python

pour les manipuler, il faut tout d'abord les **lire** et les **stocker** en mémoire

en data-science on peut avoir de **très grandes quantités** de données

* le stockage des données en mémoire doit être **optimisé**  
(en **espace mémoire** et en **temps d'accès** à cet espace mémoire)
<br>

* afin que les calculs prennent le **moins de temps possible**

mais avant de parler de cela, regardons les différentes formes de données que nous voulons manipuler :
````

+++

***

+++

## différents formats de données

### plusieurs exemples

````{admonition} →

1. des **vecteurs** et **matrices** numériques classiques

```{image} media/matrice.png
:width: 400px
```

------

2. des **tables** d'observations où

* chaque **observation** (*lignes*)...

* ...est décrite par une ou plusieurs **mesures** (*colonnes*)

* la première ligne indique, dans cet exemple, les noms des colonnes

Quelles sont ces différentes **mesures** ?  
certaines, *SibSp* et *Parch*, sont impossibles à comprendre sans les **meta-data** de la table

```{image} media/titanic.png
:width: 1000px
```

-----

3. des **séries temporelles**

* on affiche ici les valeurs cumulées des infections au covid de janvier à août 2020 en France

```{image} media/corona-france.jpg
:width: 500px
```
<https://www.data.gouv.fr/fr/datasets/coronavirus-covid19-evolution-par-pays-et-dans-le-monde-maj-quotidienne/>

-----

4. des images

```{image} media/les-mines.jpg
:width: 500px
```

-----

5. des sons (musique, voix)  

-----

6. **etc.**
````

+++

***

+++ {"lines_to_next_cell": 0}

### la matrice

````{admonition} →

pour la matrice, on peut imaginer une représentation Python comme celle-là

```python
matrice = [
[1, 2, 3, 4, 5],
[6, 7, 8, 9, 10],
[11, 12, 13, 14, 15],
[16, 17, 18, 19, 20]
]
```

mais pour transposer la sous-matrice ... c'est moins facile  
et on ne va pas coder une fonction qui doit déjà exister !

````

+++

***

+++

### table d'observations

````{admonition} →

la table (des passagers du Titanic), est donnée dans un fichier, voici les 5 premières lignes

```
PassengerId,Survived,Pclass,Name,Sex,Age,SibSp,Parch,Ticket,Fare,Cabin,Embarked
1,0,3,"Braund, Mr. Owen Harris",male,22,1,0,A/5 21171,7.25,,S
2,1,1,"Cumings, Mrs. John Bradley (Florence Briggs Thayer)",female,38,1,0,PC 17599,71.2833,C85,C
3,1,3,"Heikkinen, Miss. Laina",female,26,0,0,STON/O2. 3101282,7.925,,S
4,1,1,"Futrelle, Mrs. Jacques Heath (Lily May Peel)",female,35,1,0,113803,53.1,C123,S
...
```

que remarquez-vous ?

* en première ligne - les noms des mesures (les colonnes de la table)


* puis une observation par ligne


* les valeurs des mesures sont séparées par des `','`


* certaines valeurs sont manquantes `',,'`


* on voit des entiers, des réels (format US donc la virgule des décimales
est représentée par un `.`)...


* ce format est donc un tableau en 2 dimensions de données hétérogènes  
(des réels, des chaînes de caractères, des entiers...)

ce format s'appelle un `CSV` pour **C**omma-**S**eparated-**V**alues  
(fichier `data/titanic.csv`)
````

+++

***

+++

### la série temporelle

````{admonition} →

pour la série, on a aussi un fichier `CSV`, `data/corona-par-pays.csv`

```
#Vous pouvez utiliser ces données sans problème
#une référence à https://coronavirus.politologue.co sera appréciable
Date;Pays;Infections;Deces;Guerisons;TauxDeces;TauxGuerison;TauxInfection
2020-08-17;Andorre;989;53;863;5.36;87.26;7.38
2020-08-17;Émirats Arabes Unis;64312;364;57694;0.57;89.71;9.72
2020-08-17;Afghanistan;37596;1375;27166;3.66;72.26;24.09
...
```
que remarquez-vous ?

* il ressemble au précédent


* on a deux lignes de commentaires (commençant par `#`)


* les noms des colonnes sont dans la troisième ligne  


* les deux premières mesures sont la date et le pays
puis on voit 6 mesures reliées au covid


* dans chaque ligne, on a la valeur de ces 6 mesures pour une date et un pays


* les dates ont le format `year-month-day`



* les séparateurs sont des `';'`


* les réels sont en format US


* ce format est aussi une table en 2 dimensions de données hétérogènes  
(dates, identificateurs, réels...)
````

+++

***

+++

### l'image

````{admonition} →

pour l'image on a le fichier, en format `jpg`, `media/les-mines.jpg`

on sait que l'image est constituée de $533$ lignes et $800$ colonnes de pixels

et que chaque pixel est représenté par ses 3 valeurs `RGB` RedGreenBlue

voici les valeurs des premiers pixels de l'image

```python
[[[150, 106, 33], [143, 105, 0], [ 58, 31, 4], [135, 45, 36], [229, 131, 84], [153, 158, 200]...    ]]
```

on devine les trois dimensions (les trois `[[[`)

les valeurs des pixels RGB

* ici, des entiers prenant 256 valeurs
* $2^8$ valeurs de 0 à 255  
* pour les stocker il suffit donc d'entiers non-signés sur 8 bits  
  (0 est `00000000` et 255 est `11111111`)

````

+++

***

+++

## représenter ces données en mémoire

````{admonition} →

### notre problème

représenter ces données dans la mémoire de l'ordinateur afin de les analyser

* ces données semblent assez différentes : matrice, tables de passagers, série temporelle, image...  

* nous souhaitons pourtant leur appliquer le même genre de fonctions

comme un `max` ou un `min`

* le passager le plus agé ou le plus jeune du titanic
* les pixels les plus clairs ou les plus foncés
* les minima ou maxima des lignes de la matrice


comme des `plot` (boxplot, histogramme,  plot 2D...)

comme de petites statistiques (moyenne, écart-type...)

il faut leur trouver une **forme commune**
````

+++

***

+++

### ces données sont des tableaux multi-dimensionnels

````{admonition} →

on a des tableaux **homogènes**

* la matrice est un tableau d'entiers, en 2 dimensions, de taille $5 \times 4$


* l'image est un tableau d'entiers, en 3 dimensions, de taille $533 \times 800 \times 3$

et des tableaux **hétérogènes**

* la table des passagers du Titanic est un tableau 2D de taille $891 \times 9$


* la série temporelle est un tableau 2D de taille $33342 \times 8$


* les colonnes sont des séries de valeurs de même type


* toutes  les colonnes n'ont pas le même type
````

+++

***

+++

### pas de type Python adéquat

````{admonition} →

**structures de ces données ?**

Python ne possède pas de type adapté à ces tableaux multi-dimensionnels

depuis 2006, une librairie numérique `numpy` est *développée* pour cela

non intégrée au core-langage Python par souci de maintenance du code

elle est LA librairie numérique incontournable de Python

elle étend Python avec la manipulation de tableaux multi-dimensionnels

c'est une bibliothèque libre et open source

`SciPy` (ScientificPython) pour le calcul scientifique est fondée sur `numpy`
````
