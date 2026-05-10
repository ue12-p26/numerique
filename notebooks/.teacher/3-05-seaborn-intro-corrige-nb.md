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

# courte introduction à seaborn

une librairie de visualisation plus évoluée que matplotlib pour faire de l'exploration de données

```{code-cell} ipython3
import seaborn as sns
```

## quelques goodies

```{code-cell} ipython3
# assez pratique, les jeux de données courants

# celui-ci vous le connaissez :)
titanic = sns.load_dataset('titanic')

# et nous ici on va utiliser celui-ci
tips = sns.load_dataset('tips')
```

```{code-cell} ipython3
# voyons les pingouins
df = tips

df.head(5)
```

```{code-cell} ipython3
# at aussi, tout à fait optionnel
# mais seaborn vient avec des styles

sns.set_style('darkgrid')
```

## les grandes familles de plot

nous allons voir quelques-uns des plot exposés par seabord

- `relplot` pour afficher des **relations** statistiques
- `distplot` pour afficher la **distribution** d'une ou deux variables
- `catplot` pour afficher la *distribution* de valeurs **catégorielles*

et aussi

- `jointplot` une version un peu plus élaborée de `relplot`
- `pairplot` pour étudier en une seule figure les corrélations entre plusieurs colonnes

voyons cela sur quelques exemples

+++

## `relplot()`

dans la table des pingouins, on choisit les deux colonnes `total_bill` et `tip` pour voir leur corrélation

```{code-cell} ipython3
# commençons par une forme
# pas trop intéressante

sns.relplot(data=df, x='total_bill', y='tip');
```

jusque-là, rien de bien original; mais en fait avec `seaborn` on peut utiliser davantage que ces deux dimensions `x` et `y`, et notamment (on va voir des exemples tout de suite)

- `hue` pour choisir la couleur 
- `style` pour choisir la forme (genre x ou o) 
- `size` pour la taille des points

et même d'autres plus intéressantes

- `col` : par exemple avec une colonne catégorielle à trois valeurs, choisir cette colonne avec le paramètre `col` va construire 3 figures situées côte à côte
- `row` : pareil mais les figures sont situées l'une au-dessus de l'autre

ce qui en tout, permet de faire en principe des visualisations à 7 dimensions (`x`, `y`, `hue`, `style`, `size`, `col` et `row`

comme promis voici quelques exemples

```{code-cell} ipython3
# hue=
#
# la même visu mais qui fait ressortir 
# le déjeuner et le diner en couleurs

sns.relplot(data=df, x='total_bill', y='tip', 
            hue='time',   # time vaut 'Lunch' ou 'Dinner'
           );
```

```{code-cell} ipython3
# col=
#
# toujours la même donnée, mais cette fois
# on met le déjeuner à gauche et le diner à droite
sns.relplot(data=df, x='total_bill', y='tip', 
            col='time',
           );
```

```{code-cell} ipython3
# etc etc
# on peut tout combiner de cette façon...
# et donc en tout on peut mettre en évidence
# jusque 7 dimensions

sns.relplot(data=df, 
            x='total_bill', y='tip', 
            col='time', row='day',
            hue='sex', size='size', style='smoker',
           );
```

````{exercise} révision masques
:class: dropdown

vérifiez que les données contiennent une seule entrée pour le jeudi soir, et aucune pour les samedi et dimanche à midi

:::{admonition} solution
:class: dropdown

```python
df[ df.day.isin(['Sat', 'Sun']) & (df.time == 'Lunch')]

df[(df.day == 'Thur') & (df.time == 'Dinner')]
:::

````

+++

### affichage des incertitudes

+++

signalons enfin, pour le même genre de figures, que `seaborn` permet aussi de visualiser les variations pour les données multiples

```{code-cell} ipython3
# un exemple de données où on a plusieurs valeurs (signal) pour le méme X (ici timepoint)

fmri = sns.load_dataset("fmri")
fmri.head(10)
```

```{code-cell} ipython3
# si on ajoute `kind=line` on indique qu'on veut un "lineplot" 
# et non pas un "scatterplot" comme tout à l'heure
# dans ce cas seaborn va nous montrer 
# les intervalles de confiance autour de la moyenne

sns.relplot(data=fmri, x="timepoint", y="signal", kind="line");
```

```{raw-cell}
pour en savoir plus: <https://seaborn.pydata.org/tutorial/relational.html>
```

+++ {"jp-MarkdownHeadingCollapsed": true}

## `displot()`

avec displot on peut représenter la distribution d'une variable numérique; en reprenant les données sur les tips

```{code-cell} ipython3
df = tips
df.head(2)
```

```{code-cell} ipython3
# on peut voir qu'il vaut mieux faire
# le service du soir

sns.displot(
    data=df,
    x='tip',
    hue='time',
    kind='kde');
```

```{code-cell} ipython3
# ou encore, la même chose mais en cumulatif

sns.displot(
    data=df,
    x='tip',
    hue='time',
    kind='ecdf');
```

```{raw-cell}
pour en savoir plus: <https://seaborn.pydata.org/tutorial/distributions.html>
```

+++ {"jp-MarkdownHeadingCollapsed": true}

## `catplot()`

par exemple, la même donnée mais avec d'autres représentations

```{code-cell} ipython3
# en x une valeur catégorielle

sns.catplot(
    data=df,
    x='time', hue='time',
    y='tip',
    kind='box');
```

```{code-cell} ipython3
# la même chose avec `kind=swarm'

sns.catplot(
    data=df,
    x='time', hue='time',
    y='tip',
    kind='swarm');
```

```{raw-cell}
pour en savoir plus: <https://seaborn.pydata.org/tutorial/categorical.html>
```

## `jointplot()`

cet outil est très pratique pour fabriquer en un seul appel des vues croisées entre plusieurs colonnes; par exemple

```{code-cell} ipython3
# toujours la corrélation entre 
# les pourboires et le montant de l'addition

sns.jointplot(
    data=df,
    x='total_bill',
    y='tip',
    hue='time');
```

## `pairplot()`

+++

va nous montrer la corrélation entre toutes les colonnes numériques  
ici nous en avons 3:

```{code-cell} ipython3
df.dtypes
```

```{code-cell} ipython3
# ce qui donne un diagramme carré de 3x3 figures:

# sur la diagonale on retrouve un displot de cette colonne
# et dans les autres cases un relplot entre les deux colonnes
# on peut visualiser les colonnes de catégories pour
# par exemple la couleur

sns.pairplot(
    data=df,
    hue='time');
```

## exercice

````{admonition} pairplot
:class: seealso

à partir des données du titanic, affichez ce `pairplot`

```{image} media/3-05-exo-pairplot.png
:width: 600px
:align: center
```

```{admonition} attention
la table du titanic, telle qu'exposée par `seaborn`, n'a pas exactement les mêmes noms/types de colonnes que notre `data/titanic.csv`
```
````

```{code-cell} ipython3
# prune-begin
```

```{code-cell} ipython3
import pandas as pd
import matplotlib.pyplot as plt
```

```{code-cell} ipython3
df = pd.read_csv("data/titanic.csv")
df.dtypes
```

```{code-cell} ipython3
df.drop(columns='PassengerId,SibSp,Parch,Ticket,Cabin'.split(','), inplace=True)
```

```{code-cell} ipython3
# les colonnes numériques (merci stackoverflow)

num_cols = df.select_dtypes(include='number').columns
num_cols
```

```{code-cell} ipython3
df['Survived'] = df['Survived'].astype('category')
# df['Pclass'] = df['Pclass'].astype('category')
```

```{code-cell} ipython3
# les colonnes numériques (merci stackoverflow)

num_cols = df.select_dtypes(include='number').columns
num_cols
```

```{code-cell} ipython3
sns.pairplot(
    data=df,
    diag_kind='kde',
    hue='Sex',
);
plt.savefig("media/3-05-exo-pairplot.png")
```

```{code-cell} ipython3
# prune-end
```

## conclusion

ce (très) rapide survol devrait vous convaincre de l'utilité de cette librairie, qui permet de gagner beaucoup de temps pour l'analyse visuelle de vos données
