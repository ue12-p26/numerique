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

# TP images (1/2)

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
ou toute autre librairie d'affichage que vous aimez et/ou savez utiliser: `seaborn` ...

```{code-cell} ipython3
# votre code
```

```{code-cell} ipython3
# prune-cell

import numpy as np
from matplotlib import pyplot as plt
```

2. optionnel - changez la taille par défaut des figures matplotlib
   par exemple choisissez d'afficher les figures dans un carré de 4x4 (en théorie ce sont des inches)

   ````{tip}
   il y a plein de façons de le faire, google et/ou stackoverflow sont vos amis...
   ````

```{code-cell} ipython3
# prune-cell

# je prends un truc + petit
plt.rc('figure', figsize=(2, 2))
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

1. Créez un tableau **non initialisé**, pour représenter une image carrée **de 91 pixels de côté**, d'entiers 8 bits non-signés, et affichez-le  
   ```{admonition} indices
   :class: tip

   * il vous faut pouvoir stocker 3 `uint8` par pixel pour ranger les 3 couleurs
   * on s'intéresse uniquement à la taille, et pas au contenu puisqu'on a dit "non initialisé"; que vous ayez du blanc, du noir ou du bruit, c'est OK
   ```

```{code-cell} ipython3
# votre code
```

```{code-cell} ipython3
# prune-cell
import numpy as np
from matplotlib import pyplot as plt

# 1.
img = np.empty(shape=(91, 91, 3), dtype=np.uint8) # RGB
plt.imshow(img)
plt.show()
```

2. Transformez le en tableau blanc (en un seul slicing) et affichez-le

```{code-cell} ipython3
# votre code
```

```{code-cell} ipython3
# prune-cell
# 2.
img[:, :] = [255, 255, 255] 

# ou encore
img[:, :, :] = 255
img[:] = 255   # pas super lisible mais ça marche par broadcasting
img[...] = 255

# 
plt.imshow(img)
plt.show()
```

3. Transformez le en tableau vert (en un seul slicing) et affichez-le

```{code-cell} ipython3
# votre code
```

```{code-cell} ipython3
# prune-cell
# 3.
# ici c'est plus robuste car on récrit les 3 canaux - mais c'est possiblement plus long
img[:, :] = (0, 255, 0)

# ou encore
# ici on on garde le G à 255, et on écrit les plans R (0) et B (2)
img[:, :, [0, 2]] = 0
# pareil mais ici on utilise une "slice à step" plutôt qu'une liste
img[:, :, ::2] = 0

#
plt.imshow(img)
plt.show()
```

4. Affichez les valeurs RGB du premier pixel de l'image, et du dernier

```{code-cell} ipython3
# prune-cell
# 4.
print(img[0, 0, :])
print(img[-1, -1, :])
```

```{code-cell} ipython3
# votre code
```

5. Faites un quadrillage d'une ligne bleue, toutes les 10 lignes et colonnes et affichez-le

```{code-cell} ipython3
# votre code
```

```{code-cell} ipython3
# prune-cell
# 5.

BLUE = (0, 0, 255)

img[::10, :] = BLUE
img[:, ::10] = BLUE
plt.imshow(img);
```

## lecture d'une image en couleur

+++

1. Avec la fonction `plt.imread` lisez le fichier `data/les-mines.jpg`

```{code-cell} ipython3
# votre code
```

```{code-cell} ipython3
# prune-cell
import numpy as np
from matplotlib import pyplot as plt

filename = 'data/les-mines.jpg'

# 1.
im = plt.imread(filename)
```

2. Vérifiez si l'objet est modifiable avec `im.flags.writeable`; si il ne l'est pas, copiez l'image

```{code-cell} ipython3
# votre code
```

```{code-cell} ipython3
# prune-cell
# 2.
print(im.flags.writeable)
im = im.copy()
print(im.flags.writeable)
```

3. Affichez l'image

```{code-cell} ipython3
# votre code
```

```{code-cell} ipython3
# prune-cell
# 3.
plt.imshow(im)
plt.show()
```

4. Quel est le type de l'objet créé ?

```{code-cell} ipython3
# votre code
```

```{code-cell} ipython3
# prune-cell
# 4.
print(type(im))
```

5. Quelle est la dimension de l'image ?

```{code-cell} ipython3
# prune-cell
# 5.
im.ndim
```

6. Quelle est la taille de l'image en hauteur et largeur ?

```{code-cell} ipython3
# votre code
```

```{code-cell} ipython3
# prune-cell
# 6.
rows, cols, channels = im.shape
# ou encore...
rows, cols, *_ = im.shape

rows, cols
```

7. Quel est le nombre d'octets utilisé par pixel ?

```{code-cell} ipython3
# prune-cell
# 7.
im.itemsize
```

8. Quel est le type des pixels ?  
(deux types pour les pixels: entiers non-signés 8 bits ou flottants sur 64 bits)

```{code-cell} ipython3
# votre code
```

```{code-cell} ipython3
# prune-cell
# 8.
print(im.dtype)
```

9. Quelles sont ses valeurs maximale et minimale des pixels ?

```{code-cell} ipython3
# votre code
```

```{code-cell} ipython3
# prune-cell
# 9.
im.min(), im.max()
```

10. Affichez le rectangle de 10 x 10 pixels en haut de l'image

```{code-cell} ipython3
# votre code
```

```{code-cell} ipython3
# prune-cell
# 10.
plt.imshow(im[:10, :10, :]);
```

## accès à des parties d'image

+++

1. Relire l'image

```{code-cell} ipython3
# prune-cell
import numpy as np
from matplotlib import pyplot as plt

filename = 'data/les-mines.jpg'

# 1.
im = plt.imread(filename)
```

```{code-cell} ipython3
# votre code
```

2. Slicer et afficher l'image en ne gardant qu'une ligne et qu'une colonne sur 2, 5, 10 et 20  
(ne dupliquez pas le code)

```{admonition} indices
:class: tip

* vous pouvez créer plusieurs figures depuis une seule cellule  
  pour cela, faites plusieurs fois la séquence `plt.imshow(...); plt.show()`

* vous pouvez ensuite choisir de 'replier' ou non la zone *output* en hauteur;  
  c'est-à-dire d'afficher soit toute la hauteur, soit une zone de taille fixe avec une scrollbar pour naviguer  
  pour cela cliquez dans la marge gauche de la zone *output*
```

```{code-cell} ipython3
# prune-cell
# 2.
for n in (2, 5, 10, 20):
    print(f"un pixel sur {n}")
    plt.imshow(im[::n, ::n, :]);
    plt.show()
```

```{code-cell} ipython3
# votre code
```

3. Isoler le rectangle de `l` lignes et `c` colonnes en milieu d'image  
affichez-le pour `(l, c) = (10, 20)`) puis `(l, c) = (100, 200)`

```{code-cell} ipython3
# votre code
```

```{code-cell} ipython3
# prune-cell
# 3.
for (l, c) in ((10, 20), (100, 200)):
    print(f"centre de taille {l} x {c}")
    ml = im.shape[0] // 2 - l//2
    mc = im.shape[1] // 2 - c//2
    plt.imshow(im[ml:ml+l, mc:mc+c, :])
    plt.show()
```

## canaux RGB de l'image

+++

1. Relire l'image

```{code-cell} ipython3
# votre code
```

```{code-cell} ipython3
# prune-cell
import numpy as np
from matplotlib import pyplot as plt

# 1.
filename = 'data/les-mines.jpg'
im = plt.imread(filename)
```

2. Découpez l'image en ses trois canaux Red, Green et Blue
   (Il s'agit donc de construire trois tableaux de dimension 2)

```{code-cell} ipython3
# votre code
```

```{code-cell} ipython3
# prune-cell
# 2.
R, G, B = im[:, :, 0], im[:, :, 1], im[:, :, 2]
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

```{code-cell} ipython3
# prune-cell
# 3.
print('le canal R sans colormap')
plt.imshow(R)
plt.show()
```

4. Corrigez vos affichages si besoin

```{code-cell} ipython3
# votre code
```

```{code-cell} ipython3
# prune-cell
# 4.
print('le canal R avec colormap')
plt.imshow(R, cmap='Reds')
plt.show()

# les 3 canaux
print('les 3 canaux avec colormap')
for (channel, cmap) in (R, 'Reds'), (G, 'Greens'), (B, 'Blues'):
    plt.imshow(channel, cmap)
    plt.show()
```

5. Copiez l'image, et dans la copie, remplacer le carré de taille `(200, 200)` en bas à droite:

   * d'abord par un carré de couleur RGB `(219, 112, 147)` (vous obtenez quelle couleur)  
   * puis par un carré blanc avec des rayures horizontales rouges de 1 pixel d'épaisseur

```{code-cell} ipython3
# votre code
```

```{code-cell} ipython3
# prune-cell
# 5.1
im1 = im.copy()
l = 200
c = 200
#im1[-l:, -c:, 0] = 230
#im1[-l:, -c:, 1] = 112
#im1[-l:, -c:, 2] = 147
#plt.imshow(im1)
#plt.show()
im1[-l:, -c:] = (230, 112, 147)
plt.imshow(im1)
plt.show()
```

```{code-cell} ipython3
# prune-cell
# 5.2
#im1[-l::2, -c:, :] = 255
#im1[-l+1::2, -c:, 0] = 255
#im1[-l+1::2, -c:, 1:] = 0
im1[-l::2, -c:] = 255
im1[-l+1::2, -c:] = 255, 0, 0
plt.imshow(im1)
plt.show()
```

6. enfin pour vérifier, affichez les 20 dernières lignes et colonnes du carré à rayures

```{code-cell} ipython3
# votre code
```

```{code-cell} ipython3
# prune-cell
# 6.
plt.imshow(im1[-20:, -20:])
plt.show()
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

```{code-cell} ipython3
# prune-cell
import numpy as np
from matplotlib import pyplot as plt

# 1.
filename = 'data/les-mines.jpg'
im = plt.imread(filename)
```

2. Créez un tableau vide de la même hauteur et largeur que l'image, du type de l'image initiale, mais avec un quatrième canal

```{code-cell} ipython3
# votre code
```

```{code-cell} ipython3
# prune-cell
# 2.
ima = np.empty(shape=(im.shape[0], im.shape[1], 4), dtype=im.dtype)
# ou encore pour les geeks
# ima = np.empty(shape=(*im.shape[:2], 4), dtype=im.dtype)
```

3. Copiez-y l'image initiale, mettez le quatrième canal à `128` et affichez l'image

```{code-cell} ipython3
# votre code
```

```{code-cell} ipython3
# prune-cell
# 3.
ima[:, :, 0:3] = im
ima[:, :, 3] = 128
plt.imshow(ima)
plt.show()
```

## image en niveaux de gris en `float`

+++

1. Relire l'image `data/les-mines.jpg`

```{code-cell} ipython3
# votre code
```

```{code-cell} ipython3
# prune-cell
import numpy as np
from matplotlib import pyplot as plt

# 1.
filename = 'data/les-mines.jpg'
im = plt.imread(filename)
```

2. Passez ses valeurs en flottants entre 0 et 1 et affichez-la

```{code-cell} ipython3
# votre code
```

```{code-cell} ipython3
# prune-cell
# 2.
plt.title('q2: flottant entre 0 et 1')
imf = im/255
plt.imshow(imf)
plt.show()
```

3. Transformer l'image en deux images en niveaux de gris :  
a. en mettant pour chaque pixel la moyenne de ses valeurs R, G, B  
b. en utilisant la correction `Y` (qui corrige le constrate) basée sur la formule  
   `Y = 0.299 * R + 0.587 * G + 0.114 * B`  
c. optionnel: si vous pensez à plusieurs façons de faire la question a., utilisez `%%timeit` pour les benchmarker et choisir la plus rapide

```{code-cell} ipython3
# votre code
```

```{code-cell} ipython3
# prune-cell
# 3.a
plt.title("q3.1: niveaux de gris : moyenne")
gr = (imf[:, :, 0] + imf[:, :, 1] + imf[:, :, 2])/3
# pour les geeks; par contre il semble que c'est plus lent...
gr = (imf[:, :, :].sum(axis=2))/3
plt.imshow(gr, cmap='gray')
plt.show()
```

```{code-cell} ipython3
# prune-cell
# 3.b
plt.title('q3.2: niveaux de gris : correction Y')
grY = 0.299*imf[:, :, 0] + 0.587*imf[:, :, 1] + 0.114*imf[:, :, 2]
plt.imshow(grY, cmap='gray')
plt.show()

# ou encore
plt.title('q3.2: niveaux de gris : correction Y avec .dot()')
Y = np.array([0.299, 0.587, 0.114])
grY2 = np.dot(imf, Y)
plt.imshow(grY2, cmap='gray')
plt.show()
```

```{code-cell} ipython3
:tags: [raises-exception]

%%timeit
# prune-cell 3.c

gr = (imf[:, :, 0] + imf[:, :, 1] + imf[:, :, 2])/3
```

```{code-cell} ipython3
:tags: [raises-exception]

%%timeit
# prune-cell 3.c

# pour les geeks; mais pas efficace apparemment...
gr = (imf[:, :, :].sum(axis=2))/3
```

4. Prenez l'image de 3.a (moyenne des 3 canaux), passez les pixels au carré, et affichez le résultat
   Quel est l'effet sur l'image ?

```{code-cell} ipython3
# votre code
```

```{code-cell} ipython3
# prune-cell
# 4.
plt.imshow(np.power(gr, 2), cmap='gray')
plt.title('q4: niveaux de gris - moyenne, au carré')
plt.show()
```

5. Pareil, mais cette fois utilisez la racine carrée; quel effet cette fois ?

```{code-cell} ipython3
# votre code
```

```{code-cell} ipython3
# prune-cell
# 5.
plt.imshow(np.sqrt(gr), cmap='gray')
plt.title('q5: niveaux de gris - moyenne, racine carrée')
plt.show()
```

6. Convertissez l'image (de 3.a toujours) en type entier, et affichez la

```{code-cell} ipython3
# votre code
```

```{code-cell} ipython3
# prune-cell
# 6.
gr8 = (gr*255).astype(np.uint8)
plt.imshow(gr8, cmap='gray')
plt.title('q6: en uint8')
plt.show()
```

## affichage grille de figures

+++

`````{admonition} Mettre plusieurs figures dans une grille

Mettons l'exercice sur pause pour l'instant, et voyons comment avec matplotlib, on peut mettre faire une figure composite, i.e. qui contienne plusieurs figures disposés dans une grille

**0) on dessine toujours la même chose**, juste avec des couleurs différentes

```python
# pas important, juste un exemple de truc à dessiner

X = np.linspace(0, 2*np.pi, 50)
Y = np.sin(X)
```

**1) on créé une figure globale et des sous-figures**

les sous-figures sont appelées `axes` par convention `matplotlib`  
on construit notre grille ici de 2 lignes et 3 colonnes

```python
# ici axes va être un tableau numpy de shape .. (2, 3)
fig, axes = plt.subplots(2, 3)
```

les cases pour les sous-figures sont ici dans la variable `axes`  
qui est un `numpy.ndarray` de taille 2 lignes et 3 colonnes

**2) on affiche des sous-figure dans des cases de la grille**

```python
# en haut à gauche
axes[0, 0].plot(X, Y, 'b')
axes[0, 1].plot(X, Y, 'r')
# en haut à droite
axes[0, 2].plot(X, Y, 'y')
axes[1, 0].plot(X, Y, 'k')
axes[1, 1].plot(X, Y, 'g')
axes[1, 2].plot(X, Y, 'm')
```

````{admonition} 3) cosmétique (optionnel)
:class: dropdown tip
on peut faire un peu de cosmétique, mais je vous mets en garde: 
quand on commence on ne s'arrête plus et on perd beaucoup de temps; 
préférez au début des affichages minimalistes à peu près lisibles
```python
fig.suptitle("sinus en couleur", fontsize=20) # titre général
axes[0, 0].set_title('sinus bleu')            # titre d'une sous-figure
axes[0, 2].set_xlabel('de 0 à 2 pi')          # label des abscisses
axes[1, 1].set_ylabel('de -1 à 1')            # label d'ordonnées
axes[1, 2].set_title('sinus magenta')
plt.tight_layout()                            # ajustement automatique des paddings
```
````
`````

```{code-cell} ipython3
# ce qui nous donne, mis bout à bout
import numpy as np
import matplotlib.pyplot as plt

X = np.linspace(0, 2*np.pi, 50)
Y = np.sin(X)

# le code
fig, axes = plt.subplots(2, 3)
print(f"{type(axes)=}")
print(f"{axes.shape=}")

axes[0, 0].plot(X, Y, 'b')
# axes[0, 1].plot(X, Y, 'r')
axes[0, 2].plot(X, Y, 'y')
axes[1, 0].plot(X, Y, 'k')
axes[1, 1].plot(X, Y, 'g')
axes[1, 2].plot(X, Y, 'm')

fig.suptitle("sinus en couleur", fontsize=20)
axes[0, 0].set_title('sinus bleu')
axes[0, 2].set_xlabel('de 0 à 2 pi')
axes[1, 1].set_ylabel('de -1 à 1')
axes[1, 2].set_title('sinus magenta')
plt.tight_layout();
```

## reprenons le TP

+++

**exercice**

Reprenez les trois images en niveau de gris que vous aviez produites ci-dessus:  
  A: celle obtenue avec la moyenne des rgb  
  B: celle obtenue avec la correction Y  
  C: celle obtenue avec la racine carrée

1. Affichez les trois images côte à côte
   ```text
   A B C
   ```

```{code-cell} ipython3
# votre code
```

```{code-cell} ipython3
# prune-cell

# on retrouve les 3 images
A, B, C = gr, grY, np.sqrt(gr)

1.
fig, axes = plt.subplots(1, 3, figsize=(15, 4))
fig.suptitle('cote à cote')
axes[0].imshow(A, cmap='gray')
axes[0].set_title('moyenne')
axes[1].imshow(B, cmap='gray')
axes[1].set_title('corr. Y')
axes[2].imshow(C, cmap='gray')
axes[2].set_title('racine')
plt.show()
```

2. Affichez-les en damier:
   ```text
   A B C
   C A B
   B C A
   ```

```{code-cell} ipython3
# votre code
```

```{code-cell} ipython3
# prune-cell

2.
images = [A, B, C]
titles = ['moyenne', 'corr. Y', 'racine']

fig, axes = plt.subplots(3, 3, figsize=(15, 15))
fig.suptitle('en damier')
fig.tight_layout()

for i in range(3):
    for j in range(3):
        index = (i-j)%3
        image = images[index]
        title = titles[index]
        axes[i, j].imshow(image, cmap='gray')
        axes[i, j].set_title(title)
plt.show()
```
