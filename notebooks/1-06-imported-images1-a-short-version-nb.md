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
nbhosting:
  title: TP simple avec des images
---

# TP images (1/2) - version courte

merci à Wikipedia et à stackoverflow

```{admonition} disclaimer
:class: danger

**vous n'allez pas faire ici de traitement d'image - on se sert d'images pour égayer des exercices avec `numpy`  
(et parce que quand on se trompe: on le voit)**
```

+++

```{admonition} **Notions intervenant dans ce TP**
:class: tip

* création, indexation, slicing, modification  de `numpy.ndarray`
* affichage d'image (RBG, RGB-A, niveaux de gris)
* lecture de fichier `jpg`
* les autres notions utilisées sont rappelées (très succinctement)

**N'oubliez pas d'utiliser le help en cas de problème.**
```

+++

## import des librairies

+++

1. Importez la librairie `numpy`

1. Importez la librairie `matplotlib.pyplot`

```{code-cell} ipython3
# votre code
import numpy as np
from matplotlib import pyplot as plt
```

## création d'une image de couleur

````{admonition} Rappels (rapides)
:class: tip


* dans une image en couleur, les pixels sont représentés par leurs *dosages* dans les 3 couleurs primaires: `red`, `green`, `blue` (RGB)  
  ```{image} media/synthese-additive.png
  :width: 100px
  :align: right
  ```

* l'affichage à l'écran, d'une image couleur `rgb`, utilise les règles de la synthèse additive  
`(r, g, b) = (255, 255, 255)` donne la couleur blanche  
`(r, g, b) = (0, 0, 0)` donne du noir  
`(r, g, b) = (255, 0, 0)` donne du rouge
`(r, g, b) = (255, 255, 0)` donne du jaune ...

* pour afficher le tableau `im` comme une image, utilisez: `plt.imshow(im)`
* pour afficher plusieurs images dans une même cellule de notebook faire `plt.show()` après chaque `plt.imshow(...)`
````

+++

**Exercice**

1. Créez un tableau **non initialisé**, pour représenter une image rectangulaire **de 91 pixels par 201 de côté**, d'entiers 8 bits non-signés, et affichez-le  

````{admonition} indices
:class: tip

* il vous faut pouvoir stocker 3 `uint8` par pixel pour ranger les 3 couleurs
* on s'intéresse uniquement à la taille, et pas au contenu puisqu'on a dit "non initialisé"; que vous ayez du blanc, du noir ou du bruit, c'est OK
````

```{code-cell} ipython3
# votre code
```

2. Transformez le en tableau blanc (en un seul slicing) et affichez-le

```{code-cell} ipython3
# votre code
```

3. Transformez le en tableau jaune `[255, 255, 0]` ou vert `[0, 255, 0]` (en un seul slicing) et affichez-le

```{code-cell} ipython3
# votre code
```

4. Affichez les valeurs RGB du premier pixel de l'image, et du dernier

```{code-cell} ipython3
# votre code
```

5. Faites un quadrillage d'une ligne bleue, toutes les 10 lignes et colonnes et affichez-le

```{code-cell} ipython3
# votre code
```

## lecture d'une image en couleur

+++

1. Avec la fonction `plt.imread` lisez le fichier `data/les-mines.jpg`

```{code-cell} ipython3
# votre code
```

2. Vérifiez si l'objet est modifiable avec `im.flags.writeable`; si il ne l'est pas, copiez simplement l'image (avec `copy()`)

```{code-cell} ipython3
# votre code
```

3. Affichez l'image

```{code-cell} ipython3
# votre code
```

4. Quelle est la taille de l'image en hauteur et largeur ?

```{code-cell} ipython3
# votre code
```

5. Quel est le type des pixels ?  
(deux types pour les pixels: entiers non-signés 8 bits ou flottants sur 64 bits)

```{code-cell} ipython3
# votre code
```

## accès à des parties d'image

+++

1. Slicer et afficher l'image en ne gardant qu'une ligne et qu'une colonne sur 2, 5, 10 et 20  
(ne dupliquez pas le code - là vous pouvez faire un `for` sur les 4 valeurs...)

```{code-cell} ipython3
# votre code
```

## canaux RGB de l'image

+++

1. Relire l'image

```{code-cell} ipython3
# votre code
```

2. Découpez l'image en ses trois canaux Red, Green et Blue
   (Il s'agit donc de construire trois tableaux de dimension 2)

```{code-cell} ipython3
# votre code
```

3. Afficher chaque canal avec `plt.imshow`; la couleur est-elle la couleur attendue ?  
    Si oui très bien, si non que se passe-t-il ?

    ```{admonition} **rappel** table des couleurs
    :class: tip

    * `RGB` représente directement l'encodage de la couleur du pixel, et non un indice dans une table
    * donc pour afficher des pixel avec les 3 valeurs RGB pas besoin de tables de couleurs, on a la couleur
    * mais pour afficher une image unidimensionnelle contenant des nombres de `0` à `255`, 
      il faut bien lui dire à quoi correspondent les valeurs  
      (lors de l'affichage, le `255` des rouges n'est pas le même `255` des verts)

    * du coup, voyez le paramètre `cmap=` de `plt.imshow`; et notamment avec `'Reds'`,  `'Greens'` ou  `'Blues'`
    ```

```{code-cell} ipython3
# votre code
```

4. Corrigez vos affichages si besoin

```{code-cell} ipython3
# votre code
```

## transparence des images

+++

````{admonition} rappel: la transparence
**rappel** RGB-A

* on peut indiquer, dans une quatrième valeur des pixels, leur transparence
* ce 4-ème canal s'appelle le canal alpha
* les valeurs vont de `0` pour transparent à `255` pour opaque
````

+++

1. Relire l'image initiale (sans la copier)

```{code-cell} ipython3
# votre code
```

2. Créez un tableau vide de la même hauteur et largeur que l'image, du type de l'image initiale, mais avec un quatrième canal

```{code-cell} ipython3
# votre code
```

3. Copiez-y l'image initiale, mettez le quatrième canal à `128` et affichez l'image

```{code-cell} ipython3
# votre code
```

## image en niveaux de gris en `float`

+++

1. Relire l'image `data/les-mines.jpg`

```{code-cell} ipython3
# votre code
```

2. Passez ses valeurs en flottants entre 0 et 1 et affichez-la

```{code-cell} ipython3
# votre code
```

3. Transformer l'image en deux images en niveaux de gris :  
a. en mettant pour chaque pixel la moyenne de ses valeurs R, G, B  
b. en utilisant la correction `Y` (qui corrige le constrate) basée sur la formule  
   `Y = 0.299 * R + 0.587 * G + 0.114 * B`

```{code-cell} ipython3
# votre code
```

4. Prenez l'image de 3.a (moyenne des 3 canaux), passez les pixels au carré, et affichez le résultat
   Quel est l'effet sur l'image ?

```{code-cell} ipython3
# votre code
```

5. Pareil, mais cette fois utilisez la racine carrée; quel effet cette fois ?

```{code-cell} ipython3
# votre code
```

6. Convertissez l'image (de 3.a toujours) en type entier (avec les bonnes valeurs des pixels), et affichez la

```{code-cell} ipython3
# votre code
```

*end*
