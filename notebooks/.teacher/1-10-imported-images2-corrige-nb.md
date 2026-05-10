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
  title: suite du TP simple avec des images
---

# TP images (2/2)

merci à Wikipedia et à stackoverflow

```{admonition} disclaimer
:class: danger

**le but de ce TP n'est pas d'apprendre le traitement d'image - on se sert d'images pour égayer des exercices avec `numpy`  
(et parce que quand on se trompe ça se voit)**
```

```{code-cell} ipython3
import numpy as np
from matplotlib import pyplot as plt
```

+++ {"tags": ["framed_cell"]}

````{admonition} → **notions intervenant dans ce TP**

* sur les tableaux `numpy.ndarray`
  * `reshape()`, masques booléens, *ufunc*, agrégation, opérations linéaires
  * pour l'exercice `patchwork`:  
    on peut le traiter sans, mais l'exercice se prête bien à l'utilisation d'une [indexation d'un tableau par un tableau - voyez par exemple ceci](https://numerique.info-mines.paris/numpy-optional-indexing-nb/)

  * pour l'exercice `sepia`:  
    ici aussi on peut le faire "naivement" mais l'utilisation de `np.dot()` peut rendre le code beaucoup plus court

* pour la lecture, l'écriture et l'affichage d'images
  * utilisez `plt.imread()`, `plt.imshow()`
  * utilisez `plt.show()` entre deux `plt.imshow()` si vous affichez plusieurs images dans une même cellule

  ```{admonition} **note à propos de l'affichage**
  :class: seealso dropdown admonition-small

  * nous utilisons les fonctions d'affichage d'images de `pyplot` par souci de simplicité
  * nous ne signifions pas là du tout que ce sont les meilleures!  
    par exemple `matplotlib.pyplot.imsave` ne vous permet pas de donner la qualité de la compression  
    alors que la fonction `save` de `PIL` le permet

  * vous êtes libres d'utiliser une autre librairie comme `opencv`  
    si vous la connaissez assez pour vous débrouiller (et l'installer), les images ne sont qu'un prétexte...
  ```
````

+++

## Création d'un patchwork

### v1

on se propose d'écrire un code pour créer des tableaux dans le genre de celui-ci (affiché avec `plt.imshow`):

![](media/patchwork-sample.png)

```{code-cell} ipython3
# pour cela on se définirait par exemple
colors = [
[255, 0, 0],
[0, 255, 0],
[0, 0, 255],
[255, 255, 0],
[255, 0, 255],
]
```

après quoi on appellerait la fonction `patchwork` - que vous allez devoir écrire - comme ceci:

```python
plt.imshow(patchwork(colors))
```

remarquez les choses suivantes:

- si par exemple on avait passé 9 couleurs, on aurait créé un carré 3x3, mais comme ici on a passé à la fonction une liste de 5 couleurs, pour que ça tienne dans un rectangle, on se décide sur un rectangle de taille 2x3
- la taille totale de l'image est de 10x15, car par défaut chaque petite tuile a une taille de 5 pixels
- du coup le dernier carré est rempli avec une couleur par défaut - ici DarkGray
  (dans la v2 on pourra utiliser les couleurs par leur nom, mais n'anticipons pas; pour l'instant notez que DarkGray c'est 169, 169, 169) 

on va permettre à l'appelant de changer ces valeurs par défaut  
ça signifie que si on appelait

```python
# cette fois on passe 10 couleurs (colors + colors est une liste de 10 couleurs)
# et on fixe la taille des tuiles, et la couleur de fond noire
plt.imshow(patchwork(colors + colors, side=10, background=[0, 0, 0]))
```

on obtiendrait cette fois (observez la taille en pixels de l'image)

![](media/patchwork-sample2.png)

+++

**exercice**

+++

1. écrivez une fonction `rectangle_size` qui calcule la taille du rectangle en fonction du nombre de couleurs

```{admonition} indice
:class: tip dropdown

* votre fonction retourne un tuple avec deux morceaux: le nombre de lignes, et le nombre de colonnes
* dans un premier temps, vous pouvez vous contenter d'une version un peu brute: on pourrait utiliser juste la racine carrée, et toujours fabriquer des carrés
  
  par exemple avec 5 couleurs créer un carré 3x3 (et remplir les 4 cases restantes avec la couleur de fond)

* mais si vous avez le temps, pour 5 couleurs, un rectangle 3x2 c'est quand même mieux !

  voici pour vous aider à calculer le rectangle qui contient n couleurs

  n | rect | n | rect | n | rect | n | rect |
  -|-|-|-|-|-|-|-|
  1 | 1x1 | 5 | 2x3 | 9 | 3x3 | 14 | 4x4 |
  2 | 1x2 | 6 | 2x3 | 10 | 3x4 | 15 | 4x4 |
  3 | 2x2 | 7 | 3x3 | 11 | 3x4 | 16 | 4x4 |
  4 | 2x2 | 8 | 3x3 | 12 | 3x4 | 17 | 4x5 |
```

```{code-cell} ipython3
# votre code

def rectangle_size(n):
    """
    return a tuple (lines, cols) for
    the smallest rectangle that contains n cells
    """
    # your code goes here...
    ...
```

```{code-cell} ipython3
# prune-cell 1.

# a rougher approach would just use a square
def rectangle_size(n):
    '''
    computes the optimal size for a square of rectangle
    to store that many colors;
    if a rectangle, it will be of the form n-1, n
    '''
    c = np.ceil(np.sqrt(n))
    l = np.ceil(n / c)
    return int(l), int(c)

for n in range(1, 18):
    print(f"{n=} -> {rectangle_size(n)=}")
```

2. écrivez la fonction `patchwork` telle que décrite en préambule

````{admonition} indices
:class: dropdown

* sont potentiellement utiles pour cet exo:
  * la fonction `np.indices()`
  * [l'indexation d'un tableau par un tableau](https://numerique.info-mines.paris/numpy-optional-indexing-nb/)
* souvenez-vous que chaque "tuile" a une taille réglable
* et qu'il vous faut peindre les tuiles surnuméraires avec une couleur de fond paamétrable
````

```{code-cell} ipython3
# votre code 

def patchwork(colors, side=10, background=[169, 169, 169]):
    """
    - colors is expected to be a list of n colors; it can be either
      * a list like e.g. [[255, 0, 0], [0, 255, 0], ... ]
      * or a numpy array of shape n, 3
    - side is the "width" of each square
    - optional background it used to pad the rest of the image when
      the <n> colors are not enough to fill a rectangle
      here we use DarkGray as the default
    """
    # your code here
    ...
```

```{code-cell} ipython3
# prune-cell 2.

def patchwork(raw_colors, side=5, background=[169, 169, 169]):

    if isinstance(raw_colors, list):
        colors = np.array(raw_colors, dtype=np.uint8)
    elif isinstance(raw_colors, np.ndarray):
        # if we wanted to be over protective
        # assert colors.shape[1] == 3
        colors = raw_colors

    # we compute the number of lines and columns of the patchwork
    nb_colors = colors.shape[0]
    l, c = rectangle_size(nb_colors)

    # this one will have l*c entries
    colormap = np.empty( (l*c, 3), dtype=np.uint8)
    # we initialize it with the background 
    colormap[:] = background
    # and we assign the array with the provided colors
    # remember the remaining ones are already set with the background
    colormap[0:nb_colors] = colors

    # the final image is a rectangle of (l*side, c*side) of pixels
    # we compute its indices
    i, j = np.indices((l*side, c*side))
    # change of coordinates: in the patchwork of l*c patches (i.e. //side)
    I, J = i//side, j//side
    # if you are curious
    # print(f"{j[:2]=}")
    # print(f"{J[:2]=}")

    # c*I + J transforms I and J in the corresponding color indices in the colormap
    # its shape is the same as the final image
    pattern = c*I + J
    # print(f"{pattern}")

    # so all we are left with is .. a simple array-by-array indexation
    return colormap[pattern]
```

```{code-cell} ipython3
# si vous voulez tester
# plt.imshow(patchwork(colors));
```

```{code-cell} ipython3
# si vous voulez tester
# plt.imshow(patchwork(colors+colors, side=10, background=[0, 0, 0]))
```

```{code-cell} ipython3
# prune-cell

plt.imshow(patchwork(colors))
plt.savefig("media/patchwork-sample.png")
```

```{code-cell} ipython3
# prune-cell

plt.imshow(patchwork(colors+colors, side=10, background=[0, 0, 0]))
plt.savefig("media/patchwork-sample2.png")
```

### v2 (optionnel)

dans cette version, on a envie de pouvoir faire essentiellement la même chose, mais avec des **noms de couleurs**

et pour cela on vous fournit un **fichier textuel de description des couleurs** qui se trouve dans `data/rgb-codes.txt` et qui ressemble à ceci:

```text
AliceBlue 240 248 255
AntiqueWhite 250 235 215
Aqua 0 255 255
.../...
YellowGreen 154 205 50
```
Comme vous le devinez, le nom de la couleur est suivi des 3 valeurs 
de ses codes `R`, `G` et `B`

```{code-cell} ipython3
# with patchwork v2 one could use this data

color_names = [
    'DarkBlue', 'AntiqueWhite', 'LimeGreen', 'NavajoWhite',
    'Tomato', 'DarkGoldenrod', 'LightGoldenrodYellow', 'OliveDrab',
    'Red', 'Lime',
]
```

et ce qu'on veut, c'est pouvoir faire par exemple

```python
patchwork2(color_names)
```

pour obtenir ceci

![](media/patchwork-sample3.png)

+++

**exercice**

+++

1. lisez le fichier des couleurs en `Python`, et rangez cela dans la structure de données qui vous semble adéquate.

```{code-cell} ipython3
# votre code
```

```{code-cell} ipython3
# prune-cell 1.

# we store colors in a dictionary
# color-name -> [r, g, b]
COLORS_INDEX = dict()

with open('data/rgb-codes.txt', 'r') as f:
    for line in f:
        name, r, g, b = line.split()
        COLORS_INDEX[name] = [int(r), int(g), int(b)]
```

```{code-cell} ipython3
# prune-cell 1. 
# ou encore, en plus pédant

COLORS_INDEX = dict()
with open('data/rgb-codes.txt', 'r') as f:
    for line in f:
        name, *rgb = line.split()
        COLORS_INDEX[name] = list(map(int, rgb))
```

2. Affichez, à partir de votre structure, les valeurs rgb entières des couleurs suivantes  
`'Red'`, `'Lime'`, `'Blue'`

```{code-cell} ipython3
# votre code
```

```{code-cell} ipython3
# prune-cell 2.
for c in ['Red', 'Lime', 'Blue']:
    print(c, COLORS_INDEX[c])
```

3. Faites une fonction `patchwork2` qui fait ce qu'on veut

   Testez votre fonction en affichant le résultat obtenu sur un jeu de couleurs fourni

````{admonition} un commentaire
:class: tip admonition-small

telle qu'on l'a appelée ci-dessus i.e. `patchwork(color_names)`, on n'a pas prévu de passer en paramètre la table des couleurs - je veux dire la structure qu'on a construite à l'étape 1

c'est principalement pour simplifier: utilisez cette structure comme une variable globale ! 

bon sachez juste que dans la vraie vie, on évite cette pratique de passer par une variable globale; il y a plein de façons de faire ça, mais ce n'est pas notre sujet aujourd'hui, et on va rester simple :)

````

```{code-cell} ipython3
# votre code

def patchwork2(color_names, side=10, background_color="DarkGray"):
    '''
    create a patchwork image with <color_names>, which are resolved
    from the text file loaded above
    the other two parameters are passed to the `patchwork` function above
    except that the background color is expected to ba a color name too
    '''
    # your goes goes here
    ...
```

```{code-cell} ipython3
# ou encore

#plt.imshow(patchwork2(color_names, side=20, background="DarkGray"));
```

```{code-cell} ipython3
# prune-cell 3.

def patchwork2(color_names, side=5, background='DarkGray'):
    colors = [COLORS_INDEX[name] for name in color_names]
    background_color = COLORS_INDEX[background]
    return patchwork(colors, side=side, background=background_color)
```

```{code-cell} ipython3
# et pour le tester

#plt.imshow(patchwork2(color_names));
```

```{code-cell} ipython3
#prune-cell

plt.imshow(patchwork2(color_names))
plt.savefig("media/patchwork-sample3.png")
```

4. Tirez aléatoirement une liste de couleurs et appliquez votre fonction à ces couleurs.

```{code-cell} ipython3
# votre code
```

```{code-cell} ipython3
# prune-cell 4.

import random
k = 19
im = patchwork2(
    random.sample(list(COLORS_INDEX.keys()), k),
    side=10)

plt.imshow(im);
```

5. Sélectionnez toutes les couleurs à base de blanc (i.e. dont le nom contient `white`) et affichez leur patchwork  
   même chose pour des jaunes

```{code-cell} ipython3
# votre code
```

```{code-cell} ipython3
# prune-cell 5.

for s in ['white', 'yellow']: #, 'blue', 'medium', 'light', 'brown'
    colors = [k for k in COLORS_INDEX.keys() if s in k.lower()]
    print(f'{len(colors)} "{s}" colors')
    plt.imshow(patchwork2(colors))
    plt.show()
```

6. Appliquez la fonction à toutes les couleurs du fichier  
et sauver ce patchwork dans le fichier `patchwork.png` avec `plt.imsave`

```{code-cell} ipython3
# votre code
```

```{code-cell} ipython3
# prune-cell 6.

im_all = patchwork2(list(COLORS_INDEX.keys()), side=100)
plt.imshow(im_all);
```

7. Relisez et affichez votre fichier  
   attention si votre image vous semble floue c'est juste que l'affichage grossit vos pixels

```{code-cell} ipython3
# votre code
```

```{code-cell} ipython3
# prune-cell 7.

plt.imsave('patchwork-all.png', im_all)
plt.show()
pat = plt.imread('patchwork-all.png')
plt.imshow(pat);
```

vous devriez obtenir quelque chose comme ceci

```{image} media/patchwork-all.jpg
:width: 400px
:align: center
```

+++

## Image en sépia

+++

Pour passer en sépia les valeurs R, G et B d'un pixel, on applique la transformation suivante
```text
R' = 0.393 * R + 0.769 * G + 0.189 * B
G' = 0.349 * R + 0.686 * G + 0.168 * B
B' = 0.272 * R + 0.534 * G + 0.131 * B
```

```{admonition} notes sur les types

* dans notre cas on suppose qu'en entrée on a des entiers non-signé 8 bits
* mais attention, les calculs vont devoir se faire en flottants, et pas en uint8  
pour ne pas avoir, par exemple, 256 devenant 0

* toutefois on veut tout de même en sortie des entiers non-signé 8 bits !

ça signifie qu'il va sans doute vous falloir faire un peu de gymnastique avec les types de vos tableaux
```

+++

````{tip} indice
vous devriez jeter un coup d'oeil à la fonction `np.dot` qui est, si on veut, une généralisation du produit matriciel  
et dont voici un exemple d'utilisation:
````

```{code-cell} ipython3
:scrolled: true

# exemple de produit de matrices avec `numpy.dot`
# le help(np.dot) dit: dot(A, B)[i,j,k,m] = sum(A[i,j,:] * B[k,:,m])

i, j, k, m, n = 2, 3, 4, 5, 6
A = np.arange(i*j*k).reshape(i, j, k)
B = np.arange(m*k*n).reshape(m, k, n)

C = A.dot(B)
# or C = np.dot(A, B)

print(f"en partant des dimensions {A.shape} et {B.shape}")
print(f"on obtient un résultat de dimension {C.shape}")
print(f"et le nombre de termes dans chaque `sum()` est {A.shape[-1]} == {B.shape[-2]}")
```

**Exercice**

+++

1. Faites une fonction `sepia` qui prend en argument une image RGB et rend une image RGB sépia

```{code-cell} ipython3
# votre code
```

```{code-cell} ipython3
# prune-cell 1. pas à pas
# le même code que ci-dessous mais avec plein de print()

SEPIA = np.array([[0.393, 0.349, 0.272],
                  [0.769, 0.686, 0.534],
                  [0.189, 0.168, 0.131]])

img = plt.imread('data/les-mines.jpg') # dtype = uint8
print(img.dtype)
print(img.shape, SEPIA.shape) # (i, j, 3) (m, 3)

img_SEPIA = img.dot(SEPIA)
# ou img_SEPIA = np.dot(img, SEPIA)
print(img_SEPIA.dtype) # floats64

print(img_SEPIA.min(), img_SEPIA.max()) # de 0 à 344.505

# plt.imshow demande un type correct
# soit uint8 (donc des valeurs entre 0 et 255)
# soit float64 avec des valeurs entre 0 et 1
# (et pas entre 0 et 344.505)
# on doit donc seuiller au dessous de 255 et passer en uint8
img_SEPIA[img_SEPIA>255] = 255
img_SEPIA = img_SEPIA.astype(np.uint8)

plt.imshow(img_SEPIA);
```

```{code-cell} ipython3
# prune-cell 1. avec dot()
# dans ce cas de figure on peut utiliser indifféremment
# np.dot ou @ (aka np.matmul)
# https://numpy.org/doc/stable/reference/generated/numpy.dot.html

def sepia(im, SEPIA=np.array([[0.393, 0.349, 0.272],
                              [0.769, 0.686, 0.534],
                              [0.189, 0.168, 0.131]])):
# les deux marchent
    result = np.dot(im, SEPIA)
#    result = im @ SEPIA
    result[result>255] = 255
    return result.astype(np.uint8)

plt.imshow(
    sepia(plt.imread('data/les-mines.jpg')));
```

prune-cell: comment ça marche ?

la doc dit que
> `dot(a, b)[i,j,k,m] = sum(a[i,j,:] * b[k,:,m])`

dans notre cas:

* a est de dimension 3, et `a.shape = lines, cols, 3`, et
* b est de dimension 2, avec `b.shape = 3, 3`, ce qui donne

> `dot(image, SEPIA)[i, j, canal]
  = sum(image[i, j, :] * SEPIA[:, canal])`  
  cqfd $\diamond$

+++

2. Passez l'image `data/les-mines.jpg` en sépia

```{code-cell} ipython3
# votre code
```

```{code-cell} ipython3
# prune-cell 2.

im_sepia = sepia(plt.imread('data/les-mines.jpg'))
plt.imshow(im_sepia)
plt.imsave('media/les-mines-sepia.png', im_sepia)
```

Voici ce que vous devriez obtenir avec l'images des Mines

````{grid} 2 2 2 2
```{card}
:header: l'original
![](data/les-mines.jpg)
```
```{card}
:header: la version sepia
![](media/les-mines-sepia.png)
```
````

+++

## Somme dans une image & overflow

+++

0. Lisez l'image `data/les-mines.jpg`

```{code-cell} ipython3
# votre code
```

```{code-cell} ipython3
# prune-cell 0.
import numpy as np
from matplotlib import pyplot as plt

im = plt.imread('data/les-mines.jpg')
```

1. Créez un nouveau tableau `numpy.ndarray` en sommant **avec l'opérateur `+`** les valeurs RGB des pixels de votre image

```{code-cell} ipython3
# votre code
```

```{code-cell} ipython3
# prune-cell 1.
# en faisant comme demandé ce n'est pas très élégant
gr0 = im[:, :, 0] + im[:, :, 1] + im[:, :, 2]
```

2. Regardez le type de cette image-somme, et son maximum; que remarquez-vous?  
   Affichez cette image-somme; comme elle ne contient qu'un canal il est habile de l'afficher en "niveaux de gris" (normalement le résultat n'est pas terrible ...)


   ```{admonition} niveaux de gris ?
   :class: dropdown tip

   cherchez sur google `pyplot imshow cmap gray`
   ```

```{code-cell} ipython3
# votre code
```

```{code-cell} ipython3
# prune-cell 2.
print(f"type={gr0.dtype}, max={gr0.max()}") # uint8 -> overflow

# image pas correcte à cause des overflows
plt.imshow(gr0, cmap='gray')
plt.show()
```

3. Créez un nouveau tableau `numpy.ndarray` en sommant mais cette fois **avec la fonction d'agrégation `np.sum`** les valeurs RGB des pixels de votre image

```{code-cell} ipython3
# votre code
```

```{code-cell} ipython3
# prune-cell 3.

# de la manière précédente vous ne pouvez pas obtenir les valeurs
# en niveaux de gris des pixels de l'image, il faudrait faire:
# gr2 = im[:, :, 0]/3 + im[:, :, 1]/3 + im[:, :, 1]/3
# print(gr2.dtype, gr2.max())

gr1 = (np.sum(im, axis=2))
```

4. Comme dans le 2., regardez son maximum et son type, et affichez la

```{code-cell} ipython3
# votre code
```

```{code-cell} ipython3
# prune-cell 4.
print(f"type={gr1.dtype}, max={gr1.max()}") # int64 ok
plt.imshow(gr1, cmap='gray')
```

5. Les deux images sont de qualité très différente, pourquoi cette différence ? Utilisez le help `np.sum?`

```{code-cell} ipython3
# votre code / explication
```

```{code-cell} ipython3
# prune-cell 5.
# np.sum?
# dtype : dtype, optional
#     The type of the returned array and of the accumulator in which the
#     elements are summed.  The dtype of `a` is used by default unless `a`
#     has an integer dtype of less precision than the default platform
#     integer.  In that case, if `a` is signed then the platform integer
#     is used while if `a` is unsigned then an unsigned integer of the
#     same precision as the platform integer is used.
```

6. Passez l'image en niveaux de gris de type entiers non-signés 8 bits  
(de la manière que vous préférez)

```{code-cell} ipython3
# votre code
```

```{code-cell} ipython3
# prune-cell 6.
plt.imshow(gr1/3, cmap='gray')
plt.show()
```

```{code-cell} ipython3
# prune-cell 6.bis

gr2 = (im[:, :, 0]/3 + im[:, :, 1]/3 + im[:, :, 1]/3).astype(np.uint8)
plt.imshow(gr2, cmap='gray')
plt.show()
```

7. Remplacez dans l'image en niveaux de gris,  
les valeurs >= à 127 par 255 et celles inférieures par 0  
Affichez l'image avec une carte des couleurs des niveaux de gris  
vous pouvez utilisez la fonction `numpy.where`

```{code-cell} ipython3
# votre code
```

```{code-cell} ipython3
# prune-cell 7.
gr3 = gr2.copy()
gr3[gr3>=127] = 255
gr3[gr3<127] = 0
```

```{code-cell} ipython3
# prune-cell 7. avec where
gr3 = np.where(gr2>128, 255, 0)
plt.imshow(gr3, cmap='gray')
plt.show()
```

8. avec la fonction `numpy.unique`  
regardez les valeurs différentes que vous avez dans votre image en noir et blanc

```{code-cell} ipython3
# votre code
```

```{code-cell} ipython3
# prune-cell 8.
print(np.unique(gr3))
```

## Exemple de qualité de compression

+++

1. Importez la librairie `Image`de `PIL` (pillow)  
(vous devez peut être installer PIL dans votre environnement)

```{code-cell} ipython3
# prune-cell 1.
from PIL import Image
```

```{code-cell} ipython3
# votre code
```

2. Quelle est la taille du fichier `data/les-mines.jpg` sur disque ?

```{code-cell} ipython3
file = "data/les-mines.jpg"
```

```{code-cell} ipython3
# votre code
```

```{code-cell} ipython3
# prune-cell 2. - en bash
%ls -l $file
```

```{code-cell} ipython3
# prune-cell 2. - en Python pour cross-platform
from pathlib import Path
print(f"{file} {Path(file).stat().st_size} bytes")
```

3. Lisez le fichier 'data/les-mines.jpg' avec `Image.open` et avec `plt.imread`

```{code-cell} ipython3
# votre code
```

```{code-cell} ipython3
# prune-cell 3.
imPLT = plt.imread(file)
imPIL = Image.open(file)
```

4. Vérifiez que les valeurs contenues dans les deux objets sont proches

```{code-cell} ipython3
# votre code
```

```{code-cell} ipython3
# prune-cell 4.
np.all(np.isclose(imPLT, imPIL))
```

5. Sauvez (toujours avec de nouveaux noms de fichiers)  
l'image lue par `imread` avec `plt.imsave`  
l'image lue par `Image.open` avec `save` et une `quality=100`  
(`save` s'applique à l'objet créé par `Image.open`)

```{code-cell} ipython3
# votre code
```

```{code-cell} ipython3
# prune-cell 5.
plt.imsave(f'{file}-PLT.jpg', imPLT) # no quality
imPIL.save(f'{file}-PIL.jpg', quality=100)
```

6. Quelles sont les tailles de ces deux fichiers sur votre disque ?  
Que constatez-vous ?

```{code-cell} ipython3
# votre code
```

```{code-cell} ipython3
# prune-cell 6.
for ext in ['PLT', 'PIL']:
    print(f"{ext} {Path(f'{file}-{ext}.jpg').stat().st_size} bytes")
```

7. Relisez les deux fichiers créés et affichez avec `plt.imshow` leur différence

```{code-cell} ipython3
# votre code
```

```{code-cell} ipython3
:scrolled: true

# prune-cell 7.

imPLT_PLT = plt.imread(f"{file}-PLT.jpg")
imPLT_PIL = plt.imread(f"{file}-PIL.jpg")
print(np.all(np.isclose(imPLT_PLT, imPLT_PIL)))
plt.imshow(imPLT_PLT - imPLT_PIL);
```
