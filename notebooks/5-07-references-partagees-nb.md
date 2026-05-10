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

# références partagées

```{code-cell} ipython3
# pour visualiser le graphe de références
%load_ext ipythontutor
```

## imbrications

naturellement, les différents types de containers  
peuvent être combinés à l'infini

```{code-cell} ipython3
:cell_style: split

# une liste de dictionnaires
combo1 = [
    {'un': 'premier'},
    {'Alice': 25, 'Bob': 34},
]
combo1
```

```{code-cell} ipython3
:cell_style: split

# un dictionnaire de listes
combo2 = {
    1 : ['un', 'one', 'uno'],
    2 : ['deux', 'two', 'due'],
}
combo2
```

## références partagées

du coup on peut construire en mémoire des graphes,  
et atteindre le même objet par plusieurs chemins

```{code-cell} ipython3
# créons un objet - ici une liste
shared = ['a', 'b']
# si je mentionne cet objet deux fois
# dans une liste, je crée un partage
double = [shared, shared]
double
```

```{code-cell} ipython3
# si bien qu'en modifiant l'objet partagé
shared[0] = 'boom'
# j'ai en fait modifié les deux morceaux de la liste
double
```

```{code-cell} ipython3
%%ipythontutor

# idem visualisé sous pythontutor
shared = ['a', 'b']
double = [shared, shared]
shared[0] = 'boom'
print(double)
```

## quand ?

notamment, les références sont partagées dès qu'on fait :

* une affectation
* un appel de fonction

```{code-cell} ipython3
:cell_style: split

a = [100, 200]
b = a
# b référence le même
# objet que a
a[0] = 'boom'
b
```

```{code-cell} ipython3
:cell_style: split
:tags: [raises-exception]

def boom(x):
    x[0] = 'boom'

c = [100, 200]

# lors de cet appel
# le 'x' dans la fonction
# référence le même objet que c
boom(c)

c
```

***
**la fin est optionnelle**

+++

## références

en Python, on manipule très souvent  
des références vers des objets :

* une variable,
* un paramètre de fonction,
* un slot dans une liste,
* une valeur dans un dictionnaire,
* ...

sont tous des références vers des objets

+++

## références partagées

* le phénomène de références partagées se produit  
  dès lors qu'on peut accéder à un objet  
  par plusieurs chemins  
  dans le graphe des références

* cela permet d'éviter les copies inutiles
* mais à l'inverse il faut en être bien conscient  
  et faire explicitement des copies  
  lorsque le partage n'est pas souhaitable

+++

## mutable / immuable

* certains types d'objet ne sont pas modifiables :  
  par exemple: nombres, chaines, tuples

* dans ce cas le partage n'est pas un souci
* il faut être attentif lorsque l'objet partagé  
  est *mutable* - c'est-à-dire peut être modifié -  
  comme nos 3 sortes de containers `list`, `dict` et `set`

+++

On insiste bien sur le fait que les **nombres**  et les **chaines** ne sont **pas
mutables** en Python; pour vous en convaincre et à titre d'exercice, essayer de fabriquer
une référence partagée dans une chaine de caractères.
