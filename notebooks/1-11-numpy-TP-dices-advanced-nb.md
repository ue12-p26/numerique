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

# exercice sur le *broadcasting*

```{code-cell} ipython3
import numpy as np
```

on veut énumérer les résultats du tirage de `n` dés à `s` faces

+++

deux versions pour cet exercice:
   - la première est pour les débutants, elle est guidée et amène à construire le résultat pas à pas
   - la deuxième est pour les forts qui se débrouillent tout seuls

+++

```{admonition} juste un exercice hein

vous remarquez qu'on est dans une manière de faire qui **explicite l'ensemble des solutions**,
c'est ce qu'on appelle une méthode en force brute. Ces méthodes sont clairement exponentielles.

bien entendu ce n'est pas la méthode la plus adaptée ici, puisqu'on peut calculer tout ça sans avoir à énumérer toutes les possibilités comme on vient de le faire...
```

+++

## version pour les débutants

+++

On veut calculer les résultats des tirages de `n` dés à `s` faces. Afin, par exemple de faire des probabilités d'obtention de certains tirages. De combien de manières différentes peut-on obtenir `7` avec `3` dés à `6` faces.

+++

Si nous prenons un seul dé à `6` faces. Quels sont les tirages possibles ?

oui `1, 2, 3, 4, 5, 6`

Construisez alors un `numpy.ndarray` contenant les tirages d'un dé à `s` (comme *sides*) faces.

```{code-cell} ipython3
s = 6
```

```{code-cell} ipython3
# votre code ici
```

Maintenant si on prend `n=2` dés à `s=6` faces. Quels sont les tirages possibles ?

Oui:

```{list-table}
:header-rows: 1
:stub-columns: 1
:widths: 40 20 20 20 20 20 20
:align: center

* - &plus;
  - 1
  - 2
  - 3
  - 4
  - 5
  - 6

* - 1
  - 2
  - 3
  - 4
  - 5
  - 6
  - 7

* - 2
  - 3
  - 4
  - 5
  - 6
  - 7
  - 8

* - 3
  - 4
  - 5
  - 6
  - 7
  - 8
  - 9

* - 4
  - 5
  - 6
  - 7
  - 8
  - 9
  - 10

* - 5
  - 6
  - 7
  - 8
  - 9
  - 10
  - 11

* - 6
  - 7
  - 8
  - 9
  - 10
  - 11
  - 12
```

+++

Construisez alors un `numpy.ndarray` contenant les tirages de `n=2` dés à `s=6` faces. Un indice ? Utilisez le `broadcasting`:

On vous fait un rappel. Si on ajoute en `numpy` un tableau de forme `(3,)` à un tableau de forme `(3, 1)` on obtient la matrice suivante: 

$$
\begin{equation}
\begin{pmatrix} a_{1} & a_{2} & a_{3} \end{pmatrix} 
+ 
\begin{pmatrix} b_1 \\ b_2 \\ b_3 \end{pmatrix} 
= 
\begin{pmatrix} a_{1} + b_1 & a_{2} + b_1 & a_{3} + b_1 \\ a_{1} + b_2 & a_{2} + b_2 & a_{3} + b_2 \\ a_{1} + b_3 & a_{2} + b_3 & a_{3}  + b_3\\ a_{1} + b_4 & a_{2} + b_4 & a_{3} + b_4 \end{pmatrix}
\end{equation}
$$

+++

### n=2

calculer le tableau pour n=2 avec 6 faces

```{code-cell} ipython3
# votre code ici
```

### n=3

On continue.

Maintenant si je prends `3` dés avec `6` faces, je suis en dimension `3` et je veux donc obtenir un *cube* (avec tous les résultats). Pour obtenir ce cube, je peux simplement ajouter 3 tableaux, de formes respectivement:

* `(s,)` c'est à dire une ligne
* `(s, 1)` c'est à dire une colonne
* `(s, 1, 1)` ...

et de par les règles du broadcasting on va obtenir une somme de forme `(s, s, s)`

```{admonition} un dernier indice: reshape(-1)
:class: dropdown tip

pour rendre votre code un peu plus élégant, 
regardez la doc de `np.reshape` et voyez ce que ça donne si on met `-1` dans le paramètre `shape`
```

```{code-cell} ipython3
# votre code ici
```

Vous avez maintenant tous les indices pour généraliser en dimension `n` dés (vous aurez naturellement une boucle mais bien sûr pas sur les éléments d'un `numpy.ndarray` !); c'est le propos de la deuxième version

+++ {"tags": ["level_advanced"]}

## les dés version  pour les forts

On étudie les probabilités d'obtenir une certaine somme avec plusieurs dés.

Tout le monde connaît le cas classique avec deux dés à 6 faces, ou l'on construit mentalement la grille de 6 sur 6 qui liste les tirages possibles - voir ci-dessus

Imaginons que vous êtes un étudiant, vous venez de faire un exercice de maths qui vous a mené à une formule qui permet de calculer, pour un jeu à `nb_dice` dés, chacun à `sides` faces, le nombre de tirages qui donnent une certaine somme `target`.

Vous voulez **vérifier votre formule**, en appliquant une **méthode de force brute**. C'est-à-dire constuire un hypercube avec toutes les possibilités de tirage, puis calculer pour chaque point dans l'hypercube la somme correspondante; de cette façon on pourra compter les occurrences de `target`.

C'est l'objet de cet exercice. Vous devez écrire une fonction `dice` qui prend en paramètres:

* `target` : la somme cible à atteindre,
* `nb_dice` : le nombre de dés,
* `sides`: le nombre de faces sur chaque dé.

On convient que par défaut `nb_dice`=2 et `sides`=6, qui correspond au cas habituel.

Dans ce cas-là par exemple, on voit, en comptant la longueur des diagonales sur la figure, que `dice(7)` doit valoir 6, puisque le tableau comporte 6 cases contenant 7 sur la diagonale.

À nouveau, on demande explicitement ici un parcours de type force brute; c'est-à-dire de créer sous la forme d'un tableau `numpy`, un hypercube qui énumère toutes les combinaisons possibles; et sans faire de `for` sur les éléments d'un tableau.

+++ {"tags": ["level_advanced"]}

````{admonition} indice: np.newaxis

Il existe en `numpy` une astuce pour augmenter la dimension d'un tableau, ça s'appelle `np.newaxis`, et ça s'utilise comme ceci

```python
# un tableau "plat"
dice_1 = np.arange(1, 7)

# peut être transformé en une colonne comme ceci
dice_2 = dice_1[:, np.newaxis]

# et plus généralement je peux "décaler" la shape d\un cran avec
dice_nplus1 = dice_n[..., np.newaxis]
```
````

```{code-cell} ipython3
# votre code

def dice(*args):
    pass
```

```{code-cell} ipython3
# pour tester votre code - devrait être True

(
    dice(7, 2, 6) == 6
and dice(10, 3, 6) == 27
and dice(13, 4, 6) == 140
)
```
