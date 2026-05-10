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

# types containers

+++

## la liste

permet de créer des collections très souples :

* séquence d'objets de n'importe quel type
* on peut insérer / détruire des objets
* pas de contrainte sur la taille

```{code-cell} ipython3
:cell_style: split

# on crée une liste avec des [ ]
homogene = [0, 12]
homogene
```

```{code-cell} ipython3
:cell_style: split

# on peut mélanger
# les types
heterogene = [2.3, "abc"]
heterogene
```

```{code-cell} ipython3
:cell_style: split

# des listes dans des listes
groupe = [True, homogene,
          "chaine", heterogene]
groupe
```

```{code-cell} ipython3
:cell_style: split

type(groupe)
```

```{code-cell} ipython3
:cell_style: split

groupe
```

```{code-cell} ipython3
:cell_style: split

# comme avec les chaines
# on peut accéder au i-ème élément
# les indices commencent à 0

# le premier élément est
# donc le booléen
groupe[0]
```

```{code-cell} ipython3
:cell_style: split

# on peut remplacer un élément
groupe[1] = '-'
groupe
```

```{code-cell} ipython3
:cell_style: split

# et le dernier
groupe[-1]
```

```{code-cell} ipython3
:cell_style: split

# est heterogene
groupe[-1] == heterogene
```

```{code-cell} ipython3
:cell_style: split

# le slicing s'applique aussi
# comme sur les chaines de caractère
groupe[::2] # du début à la fin avec un pas de 2
```

## liste et opérateurs

+++

de nombreux opérateurs sont définis aussi sur les listes

```{code-cell} ipython3
:cell_style: split

# on peut ajouter deux listes,
# ça les concatène
[1, 2, 3] + [4, 5, 6]
```

```{code-cell} ipython3
:cell_style: split

# la comparaison est
# lexicographique

[1, 2, 3] <= [1, 2, 4]
```

```{code-cell} ipython3
:cell_style: split

# l'opérateur d'appartenance
'chaine' in groupe
```

```{code-cell} ipython3
:cell_style: split

# et sa négation
'tutu' not in groupe
```

## itérations

approfondi dans une section ultérieure  
mais dans sa forme la plus simple: `for .. in .. :`

```{code-cell} ipython3
for item in groupe:
    print(item)
```

## listes et performances

+++

**À savoir**  
la liste est une structure de données très souple du coup elle n'est que *relativement
efficace*  
elle est surtout optimisée pour être modifiée **par la fin**  
habituellement à base des méthodes `append` et `pop`

```{code-cell} ipython3
:cell_style: split

tutu = []

# on n'a pas encore vu le for
# mais vous pouvez deviner ce que ça fait
for c in 'abc':
    tutu.append(c)
    print(tutu)
```

```{code-cell} ipython3
:cell_style: split

# et à l'envers
while tutu:
    c = tutu.pop()
    print(c)
```

MAIS cela n'est un problème qu'avec des données nombreuses - $10^4$  
du coup pour des preuves de concept la liste est **TRÈS** flexible et pratique

+++

## le tuple

similaire à la liste, mais qu'**on ne peut pas modifier**  
(on parle d'objets **non mutables** - ou immuables)  
ne sera pas approfondi dans ce primer  
on va voir tout de suite à quoi ça peut bien servir

```{code-cell} ipython3
:cell_style: split

# ressemble à une liste, mais s'écrit avec des ()

paquet = (12, "abc")
paquet
```

```{code-cell} ipython3
:cell_style: split

# on ne peut plus y toucher
# paquet[0] = 15 n'est pas autorisé
# ni paquet.append(0)
```

## l'ensemble

+++

une autre forme de container, mais assez différent :  

* comme pour les ensembles mathématiques, un même élément  
  ne peut apparaitre qu'une seule fois dans un ensemble

* la **recherche d'un élément** dans un ensemble est **très efficace**  
  contrairement aux listes, on n'a pas besoin de balayer tous les éléments  
  repose sur la notion de table de hachage - détaillé dans le cours avancé

* par contre, limitation sur les éléments  
  certains types ne sont pas éligibles
  par ex. on ne peut pas mettre une liste dans un ensemble  
  utiliser à la place un `tuple`

```{code-cell} ipython3
:cell_style: split

# pour créer un ensemble
ensemble = {12, "abc"}
ensemble
```

```{code-cell} ipython3
:cell_style: split

# méthode add() pour ajouter
ensemble.add(True)
ensemble
```

```{code-cell} ipython3
:cell_style: split

# pas de doublon
ensemble.add("abc")
ensemble
```

```{code-cell} ipython3
:cell_style: split

# la recherche est rapide
# bien sûr, c'est surtout intéressant
# sur des grosses données

12 in ensemble
```

```{code-cell} ipython3
:cell_style: split

# on peut mettre un tuple dans un ensemble
ensemble.add((2, 3))
ensemble
```

```{code-cell} ipython3
:cell_style: split

# et pour enlever
ensemble.remove(12)
ensemble
```

### itérations sur l'ensemble

+++

forme la plus simple, idem : `for .. in ..`  
attention qu'un ensemble n'a pas d'ordre naturel  
depuis Python-3.7 le parcours se fait dans l'ordre des insertions

```{code-cell} ipython3
for item in ensemble:
    print(item)
```

## le dictionnaire

aussi un container, mais cette fois c'est conceptuellement  
un ensemble d'associations de la forme

    clé → valeur

```{code-cell} ipython3
:cell_style: split

# la syntaxe pour créer
# un dictionnaire en clair
annuaire = {'alice': 25, 'bob': 32}
```

```{code-cell} ipython3
:cell_style: split

# les clés sont ici les 2 chaines
# 'alice', 'bob'

annuaire
```

```{code-cell} ipython3
:cell_style: split

# on ne peut plus accéder par indice
# annuaire[0] ne veut rien dire!

# par contre on peut accéder par clé
annuaire['bob']
```

```{code-cell} ipython3
:cell_style: split

# pareil pour écrire
# si la clé est inconnue on l'ajoute

annuaire['eve'] = 40
annuaire
```

```{code-cell} ipython3
:cell_style: split

# si la clé existe déjà
# on écrase la valeur associée
annuaire['alice'] = 50
annuaire
```

```{code-cell} ipython3
:cell_style: split

# pour effacer une clé  
del annuaire['eve']
annuaire
```

```{code-cell} ipython3
:cell_style: split

annuaire
```

```{code-cell} ipython3
:cell_style: split

# la recherche d'une clé est aussi rapide
# que la recherche dans les ensembles

'alice' in annuaire
```

## digression : affectation multiple

```{code-cell} ipython3
:cell_style: split

# plutôt que de faire
a = 10
b = 20

print(f"a={a}, b={b}")
```

```{code-cell} ipython3
:cell_style: split

# on peut faire en Python
a, b = 10, 20

print(f"a={a}, b={b}")
```

dans ce contexte c'est un gadget, mais c'est intéressant parfois  
car les termes à droite de `=` sont tous évalués avant de faire les affectations

```{code-cell} ipython3
# et ainsi on peut par exemple
# échanger deux variables
a, b = b, a

print(f"a={a}, b={b}")
```

## itération sur un dictionnaire

+++

même remarque que les ensembles : pas d'ordre naturel  
depuis Python-3.7 le parcours se fait dans l'ordre des insertions

```{code-cell} ipython3
for cle, valeur in annuaire.items():
    print(f"{cle} → {valeur}")
```

cette forme est à mettre en rapport avec l'affectation multiple  
dans ce sens que ça revient à faire ceci :

```{code-cell} ipython3
# en décomposant un peu pour bien comprendre
for couple in annuaire.items():
    cle, valeur = couple # on appelle cela de l'unpacking
    print(f"{cle} → {valeur}")
```

## fonctions et arguments multiples (1)

**optionnel**

+++

mécanisme pour définir un nombre quelconque d'arguments à une fonction

```{code-cell} ipython3
# parfois on a envie qu'une fonction puisse
# accepter un nombre variable d'arguments

def foo(fixe, *variable):
    """
    fixe reçoit le premier argument
    variable reçoit un tuple avec tous les autres arguments de l'appel
    """
    print(f"premier argument: {fixe}")
    print(f"les autres: {variable} - de type {type(variable)}")
    for item in variable:
        print(f"item {item}")
```

```{code-cell} ipython3
:cell_style: split

foo(1)
```

```{code-cell} ipython3
:cell_style: split

foo(1, 2)
```

```{code-cell} ipython3
foo(1, 2, 3)
```

bien entendu on ne peut définir qu'un seul paramètre de ce genre, et il doit apparaitre en
dernier dans la signature de la fonction  
Si on pouvait en mettre plusieurs, il y aurait ambigüité quant à qui reçoit quoi.

+++

## fonctions et arguments multiples (2)

**optionnel**

+++

dans l'autre sens, si j'ai un container avec des objets
que je veux passer individuellement à une fonction

```{code-cell} ipython3
# par exemple j'ai une liste
args = [1, 2, 3]

# et en fait je veux appeler
# foo(1, 2, 3)
#
# je pourrais faire
# foo(args[0], args[1], arg[2])
#
# mais bien sûr ça ne marchera
# que si args contient 3 objets
```

```{code-cell} ipython3
:cell_style: split

# dans ce cas on peut utiliser à nouveau
# l'étoile, et faire plutôt
foo(*args)
```

```{code-cell} ipython3
:cell_style: split

# vérifions que c'est bien
# ce qu'on voulait
foo(1, 2, 3)
```

à l'appel de la fonction par contre on peut passer plusieurs arguments étoilés, leurs
composants sont simplement ajoutés dans l'ordre aux arguments de la fonction.

+++

## résumé

Python propose des types prédéfinis

* `list` : un container flexible et ordonné, accessible par indice
* plus accessoirement, `tuple` pour créer des containers similaires mais non modifiables
* `set` : un container non-ordonné, sans doublon, et à recherche rapide
* `dict` : un ensemble d'associations clé → valeur,  
  à recherche rapide, accessible par clé

* la forme `*args` permet aux fonctions d'accepter un nombre quelconque d'arguments
  * définition `def foo(*args):`
  * appel `foo(*args)`
