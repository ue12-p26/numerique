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

# obtenir de l'aide

+++

## la complétion

l'outil le plus utilisé, et de loin, pour avoir de l'aide en ligne, est la complétion  
on rappelle qu'en tapant la touche 'Tab' (`⇥`), l'ordi essaie de compléter la commande que vous avez commencée

c'est vraiment **hyper utile**, si vous ne l'utilisez pas en permanence c'est le moment de réessayer - et de l'adopter comme une habitude presque inconsciente

+++

## help dans les notebooks avec Shift-Tab

dans Jupyter seulement, si vous tapez 'Shift-Tab' vous avez un popup qui vous montre la doc de la fonction sur laquelle vous êtes

```{code-cell} ipython3
import numpy as np
```

```{code-cell} ipython3
np.empty
```

`````{grid} 2 2 2 2
````{card}
si dans cette situation
```{image} media/jlab-help-before.png
```
je tape Shift-Tab, je vais obtenir cela  
c'est pratique car dès que je tape un autre caractère le popup s'efface  
(du coup d'ailleurs j'ai dû faire le screenshot avec un tél...)
````
````{card}
```{image} media/jlab-help-after.png
:width: 300px
```
````
`````

+++

## help IPython avec ?

dans Jupyter, ou aussi dans IPython:

+++

taper, dans une cellule de code, le symbole sur lequel vous voulez avoir de l'aide suivi de `?`

```python
Entrée [ ]: int?
```

Une fenêre contenant le help apparaît en bas de votre notebook

```{code-cell} ipython3
# décommenter pour tester
# int?
```

## help de Python avec help()

+++

dans le code Python, appeler la fonction `help`


* avec un nom en argument `help(int)`, vous obtenez la documentation sur ce nom  
  ce nom peut être une chaîne `help('if')` 


* sans argument `help()`  
  un utilitaire vous permet d'afficher la documentation des noms que vous entrez

```{code-cell} ipython3
# décommenter pour tester
# help(help)
```

```{code-cell} ipython3
# décommenter pour tester
#help()
```

```{code-cell} ipython3
# décommenter pour tester
#help('if')
```
