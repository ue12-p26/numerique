---
celltoolbar: Edit Metadata
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

# modules

+++

## bibliothèque standard

un grand nombre d'outils installés d'office  
pour des tâches très variées
[voir liste complète](https://docs.python.org/3/library/#the-python-standard-library)  


cette boite à outils est exposée au travers de **modules**  
que l'on peut charger dans son appli grâce au mot-clé `import`

+++

## `import`

```{code-cell} ipython3
:cell_style: split

# import permet de charger un code
import math
```

```{code-cell} ipython3
:cell_style: split

# cela définit une variable, ici 'math'
# qui est une référence
# vers un objet module
math
```

```{code-cell} ipython3
:cell_style: split

type(math)
```

```{code-cell} ipython3
:cell_style: split

# cet objet possède des attributs
# auxquels on peut accéder
# avec la notation module.attribut

math.pi
```

## autres formes

```{code-cell} ipython3
:cell_style: split

# avec cette forme on ne définit pas la variable math
# mais directement la variable pi

from math import pi
pi
```

```{code-cell} ipython3
:cell_style: split

# ici on n'a importé que le nom 'pi'
# et donc 'cos' n'est pas défini
# mais grâce au 'import math'
# on peut y accéder par math.cos

math.cos(pi)
```

## installation de librairies tierces

si on a besoin d'installer un module  
qui ne fait pas partie de la bibliothèque standard :

* répertoire disponible sur <https://pypi.org/>
* installation à faire avec l'outil `pip`  
  (se lance depuis le terminal)

```{code-cell} ipython3
# cette astuce avec le ! me permet
# d'appeler une commande normalement destinée au terminal
# mais depuis Python

!pip install nbautoeval
```

```{code-cell} ipython3
import nbautoeval
```

## c'est quoi un module ?

+++

un module est un objet Python qui correspond à un fichier (ou répertoire) source  
depuis cet objet vous pouvez accéder à des **attributs**  
avec la notation `module.attribut`  
  (qui est *btw* la même notion que, par ex., `str.capitalize`)    
le module a autant d'attributs que d'objets globaux dans le code source  
dans le cas d'un répertoire les attributs référencent d'autres modules

```{code-cell} ipython3
:cell_style: split

# regarder le contenu
!cat mod.py
```

```{code-cell} ipython3
:cell_style: split

import mod

# tous les noms dans le module (y compris les noms "internes")
dir(mod)
```

```{code-cell} ipython3
:cell_style: split

# pour afficher tous les attributs du module
# et une fois le bruit éliminé
[x for x in dir(mod) if '__' not in x]
```

## notion de point d'entrée

+++

votre programme Python est toujours exécuté par un interpréteur  
qui "commence" quelque part: c'est le point d'entrée

+++ {"cell_style": "split"}

si vous lancez  
```bash
$ python3 foo.py
```

+++ {"cell_style": "split"}

le point d'entrée dans ce cas est
(le module correspondant à) `foo.py`

+++

## recherche des modules

Python recherche les modules dans plusieurs d'endroits (répertoires)

* le répertoire qui contient le point d'entrée  
* en option, la variable d'environnement `PYTHONPATH`
* là où sont installés les morceaux de la librairie standard

conseil : évitez de bidouiller `PYTHONPATH`

+++

## organisation de votre code

cela signifie que pour commencer,  
on peut sans souci couper son code en fichiers  
et les mettre tous dans le même répertoire

+++

c'est une pratique courante et recommandée  
il faut apprendre à découper  
notamment pour augmenter la réutilisabilité

+++

## librairies utiles

liste largement non exhaustive

* gestion des fichiers: `from pathlib import Path`  
* génération de nombres aléatoires `import random`
* télécharger depuis Internet: `import requests`
* ouverture de fichiers au format JSON: `import json` (standard)

* Python scientifique: `numpy`, `pandas`, `matplotlib`, ...

+++

## module `pathlib`

+++

fait partie de la librairie standard  
permet de faire des calculs sur les fichiers  

* lister les fichiers présents
* calculs sur les chemins et noms de fichier  
* accéder aux métadata (taille, date, ...)

```{code-cell} ipython3
:cell_style: center

# ici Path correspond à une classe
# on verra la théorie très bientôt
from pathlib import Path

# on recherche dans le répertoire courant '.'
# les fichiers/répertoires d'extension '.ipynb'
local_files = Path('.').glob('*.ipynb')

# observons les fichiers trouvés
for file in local_files:
    print('name', file.name)
    print('stem', file.stem)
    print('suffix', file.suffix)
    print('absolute()', file.absolute())
    print('size', file.stat().st_size)
    break
```

## module `random`

+++

une fois que vous avez le nom du module,  
il vous suffit de consulter [la doc
complète](https://docs.python.org/3/library/random.html)  
pour cela taper dans google `python random module`  
(nous reviendrons sur ce module lors de l'étude des librairies numériques)

```{code-cell} ipython3
:cell_style: split

import random

# entre 0 et 1
random.random()
```

```{code-cell} ipython3
:cell_style: split

# un entier entre deux bornes
# inclusivement
random.randint(0, 10)
```

## module `requests`

+++

télécharger du contenu depuis une URL  
accéder à l'entête http
plus flexible que l'équivalent dans la librairie standard `urllib2`

```{code-cell} ipython3
import requests

url = ""
url = "https://github.com/timeline.json"

request = requests.get(url)

print(f"code de retour HTTP: {request.status_code}")
```

```{code-cell} ipython3
:cell_style: split

raw_content = request.text
# une chaine de caractères
type(raw_content)
```

```{code-cell} ipython3
:cell_style: split

# le début de cette chaine
raw_content[:120]
# son contenu est en format json (voir slide suivante)
```

## module `json`

le cas qu'on vient de voir est très fréquent  
JSON est un format texte (compatible réseau donc Internet)  
mais qui conserve un minimum de structure :
permet de transmettre listes et dictionnaires

```{code-cell} ipython3
:cell_style: split

# pour décoder le JSON qu'on a lu
# et qui est dans la str raw_content
import json

decoded = json.loads(raw_content)
type(decoded) # la chaîne contenait un dict Pyhon
```

```{code-cell} ipython3
:cell_style: split

# cette fois on a un peu
# de structure
for k, v in decoded.items():
    print(f"{k}\n\t{v[:20]}...")
```

## gestion de fichiers

```{code-cell} ipython3
:cell_style: center

# pour écrire dans un fichier
with open("tutu.txt", "w") as writer:
    for i in range(4):
        print(f"i={i}", file=writer)
```

+++ {"cell_style": "center"}

`with open...` ouvre le fichier `tutu.txt` en écriture `"w"`  
  et crée la variable `writer` de type `File`  
`writer` n'est visible que dans le `with`  
`print(..., file=writer)` écrit dans ce fichier  
`with` ferme le fichier à la sortie  
(nous allons maintenant lire ce fichier)

+++

## fichiers - suite

```{code-cell} ipython3
:cell_style: split

# à l'envers, on relit le fichier
with open('tutu.txt') as reader:
    for line in reader:
        print(line, end="")
```

+++ {"cell_style": "split"}

sans préciser le mode d'ouverture  
`open` ouvre le fichier en lecture  
l'objet `reader` est **itérable**


la variable `line` contient une fin de ligne  
pas besoin que `print` en rajoute une

+++

## exercice

écrire une fonction `json_random()` qui retourne :

* une chaine de caractères
* qui correspond à l'encodage en JSON
* d'une liste contenant - au hasard - entre 2 et 5 valeurs numériques
* elles-mêmes tirées au hasard dans l'intervalle $[2 .. 5]$

```{code-cell} ipython3
:cell_style: center

 # n'oubliez pas d'importer les modules
# dont vous avez besoin
def random_json():
    """
    returns a JSON-encoded of a list
    of 2 to 5 values between 2 and 5
    """
    # votre code ici
    pass
```

```{code-cell} ipython3
:tags: [raises-exception]

from check_random_json import check_random_json

check_random_json(random_json)
```
