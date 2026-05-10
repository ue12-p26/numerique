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
  nbconvert_exporter: python
  pygments_lexer: ipython3
---

(label-matplotlib-ipympl)=
# `%matplotlib ipympl`

+++

````{admonition} avertissement
:class: warning

ce point est assez scabreux, et dépend notamment des versions de Jupyter:

* dans la version dite "notebook classic" qui était encore très répandue jusqu'en juin 2023, on utilisait  
  `%matplotlib notebook`

* mais cet idiome ne fonctionne plus et il faut maintenant, dans JupyterLab 4 ou Notebook7, on recommande d'utiliser plutôt  
  `%matplotlib widget`

* de plus il se trouve que cette forme repose en fait sur un module supplémentaire qui s'appelle `ipympl`
et que l'expérience a montré que c'est encore mieux (lire: ça marche aussi dans vs-code) si vous utilisez à la place
`%matplotlib ipympl`

et c'est donc ce qu'on a choisi d'illustrer ici

l'invariant là dedans, c'est que ça vaut vraiment la peine de passer un peu de temps à s'assurer **que vos graphiques sont bien interactifs**
````

+++

de la bonne utilisation de `plt.figure()`, `plt.show()` en fonction du driver `%matplotlib` - épisode 2

+++

**take home message**

* nécessite l'installation `pip install ipympl`
* plus pratique / interactif  
  * on peut retailler la figure
  * se déplacer / zoomer dans la figure
* il **faut** appeler `plt.figure()` pour chaque figure  
* et en ajouter d'autres `plt.figure()`  
  pour créer plusieurs figures depuis une seule cellule

* **attention** à `df.plot()` qui appelle automatiquement `plt.figure()`

+++

***

+++

````{admonition} seulement dans un notebook
:class: warning

dans la version book (la version html statique) ceci ne va pas bien fonctionner,
ce notebook est un support que vous devez vraiment ouvrir dans jupyterlab sur votre ordi...
````

```{code-cell} ipython3
%matplotlib ipympl
```

```{code-cell} ipython3
import matplotlib.pyplot as plt

# pour changer la taille des figures par défaut
plt.rcParams["figure.figsize"] = (4, 2)
```

## préparation

```{code-cell} ipython3
import numpy as np

X = np.linspace(0, 2*np.pi)
Y = np.sin(X)
Y2 = np.cos(X)
```

## un plot = une figure

+++

l'apport principal de ce driver, c'est qu'on peut "naviguer" dans le graphe - zoomer et se déplacer, sauver la figure, etc... avec **la palette d'outils** située par défaut à gauche du dessin; entraînez-vous à retailler la figure, à zoomer dedans, à revenir au point de départ, etc..

```{code-cell} ipython3
:cell_style: split

# on peut avoir l'impression
# que ce n'est pas la peine
# de créer une figure,
# car la première fois ça fonctionne
plt.figure()     # <-- mais c'est mieux de prendre
                 # l'habitude de le faire quand meme !
                 # pour vous en assurer enlever le commentaire
plt.plot(X, Y);
```

```{code-cell} ipython3
:cell_style: split

# mais en fait si on ne le fait pas
# on écrit dans la dernière figure
# ouverte
plt.plot(X, Y2);
```

```{code-cell} ipython3
:cell_style: split

# donc vous voyez, il faut mettre la création de l figure
plt.figure()
plt.plot(X, Y2);
```

## plusieurs courbes

```{code-cell} ipython3
:cell_style: split

# du coup avec ce mode c'est important
# de TOUJOURS créer une figure
# avant d'écrire dedans
plt.figure()
plt.plot(X, Y)
plt.plot(X, Y2);
```

```{code-cell} ipython3
:cell_style: split

# et voici comment, tout simplement
# on crée deux figures dans une cellule
plt.figure()
plt.plot(X, Y)
plt.figure()
plt.plot(X, Y2);
```

```{code-cell} ipython3
# alors que si on utilise un style à base de
# `plt.show()` qui marche avec le driver 'inline'
# eh bien ici ça ne fonctionne plus du tout
# car les courbes se retrouvent dans la figure du dessus !
plt.plot(X, Y)
plt.show()
plt.plot(X, 2* Y2)  # * 2 pour qu'on la voie bien
plt.show()
```

## `pandas.plot`

```{code-cell} ipython3
import pandas as pd
df = pd.DataFrame({'sin': Y, 'cos': Y2}, index=X)
```

enfin, dernière blague, lorsqu'on affiche directement une dataframe avec `df.plot()`  
`pandas` fait **automatiquement un appel à `plt.figure()`**  

du coup il faut faire attention:  
après tout ce qu'on vient de voir on aurait envie de faire  
mais regardez ce que ça donne:

```{code-cell} ipython3
plt.figure()    # parce que %matplotlib ipympl
                # mais en fait il ne faut pas le mettre
df.plot();
```

comme vous le voyez, le premier `plt.figure()` **est de trop**,  
il ne faut pas le mettre

mais par contre avec une série ça n'est pas le cas !?!

*go figure*…

```{code-cell} ipython3
plt.figure()      # ici il faut garder cet appel
df['sin'].plot();
```

***
