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
short_title: données géographiques
---

# données géographiques avec `geopandas` et `folium`

```{code-cell} ipython3
import pandas as pd
import matplotlib.pyplot as plt
import geopandas as gpd
```

## les données avec `geopandas`

+++ {"tags": ["framed_cell"]}

````{admonition} →
ce notebook est juste un **aperçu** de ce qu'on peut faire avec `geopandas`  
c'est une librairie qui étend `pandas` pour traiter des **données géographiques**

l'idée est très simple

* un `GeoDataFrame` est une `DataFrame` (tout ce que vous avez vu jusqu'ici fonctionne)
* qui possède en plus une colonne spéciale, en général nommée `geometry`  
  dont chaque case contient une **forme** (point, ligne, polygone..)  
  ces formes viennent de la librairie `shapely`

on va prendre comme exemple les **quartiers de Paris**
````

### lire un shapefile

+++ {"tags": ["framed_cell"]}

````{admonition} →
un format très répandu pour échanger des données géographiques est le **shapefile**  
en réalité ce n'est pas un fichier mais un petit paquet de fichiers de même nom

* `.shp` les formes
* `.dbf` la table des attributs (nom, code, etc..)
* `.shx` un index, `.prj` le système de coordonnées..

on les trouve souvent regroupés dans un `.zip`  
et `gpd.read_file()` sait lire directement dans le zip
````

```{code-cell} ipython3
# on lit les quartiers de Paris, fournis sous forme de shapefile zippé
# l'encodage est nécessaire pour que les accents soient corrects

quartiers = gpd.read_file('zip://data/quartier_paris.zip', encoding='utf-8')
```

```{code-cell} ipython3
type(quartiers)
```

```{code-cell} ipython3
# un 'GeoDataFrame' ressemble à s'y méprendre à une 'DataFrame'

quartiers.head(3)
```

```{code-cell} ipython3
# on ne garde que les colonnes utiles
# c_ar est le numéro de l'arrondissement, mais lu comme une chaine
# et surface est la surface du quartier, en m2

quartiers = quartiers[['l_qu', 'c_ar', 'surface', 'geometry']]
quartiers['c_ar'] = quartiers['c_ar'].astype(int)
quartiers = quartiers.rename(columns={'l_qu': 'quartier', 'c_ar': 'arrondissement'})
quartiers.head(3)
```

### c'est une `DataFrame` comme les autres

```{code-cell} ipython3
# les formes sont des objets shapely

quartiers.loc[0, 'geometry']
```

```{code-cell} ipython3
# et tout ce qu'on sait faire avec pandas fonctionne

quartiers[quartiers.arrondissement == 6]
```

```{code-cell} ipython3
# les 3 plus grands quartiers, grâce à la colonne 'surface' (en m2)

quartiers.sort_values('surface', ascending=False).head(3)
```

```{code-cell} ipython3
# et on a en plus un .plot() qui dessine les formes
# on peut colorier selon une colonne

quartiers.plot(column='arrondissement', cmap='tab20', figsize=(8, 6))
```

+++ {"tags": ["framed_cell"]}

### le système de coordonnées** (`crs`)

les coordonnées d'une forme ne veulent rien dire tant qu'on ne sait pas dans quel système elles sont exprimées  
il faut donc toujours savoir de quel système on parle, et l'attribut `crs` nous le dit

```{code-cell} ipython3
# ici ce sont des (longitude, latitude), c'est le système WGS84 (EPSG:4326)
# celui du GPS, et de la plupart des données qu'on trouve

quartiers.crs
```

````{admonition} pour aller plus loin: calculer les surfaces nous-mêmes
:class: dropdown seealso

ici la colonne `surface` était fournie avec les données  
mais on aurait pu la calculer à partir des formes, avec `quartiers.area`

sauf que dans le système WGS84 les coordonnées sont des **degrés**,
et une surface en degrés carrés n'a pas grand sens (`geopandas` nous le signale d'ailleurs par un warning)  
il faut donc d'abord convertir les formes dans un système **métrique**,
pour la France c'est le Lambert-93 (EPSG:2154)

```python
quartiers_m = quartiers.to_crs(epsg=2154)
quartiers_m.area            # des m2, qui correspondent à la colonne 'surface'
```

c'est vrai aussi pour les distances (`.distance()`), et plus généralement
pour tout ce qui fait intervenir des mesures
````

### créer des points

+++ {"tags": ["framed_cell"]}

````{admonition} →
pour illustrer les jointures, on va créer une `GeoDataFrame` de **points**  
on part d'une `DataFrame` ordinaire, avec des colonnes longitude et latitude  
et on construit la colonne `geometry` avec `gpd.points_from_xy()`
````

```{code-cell} ipython3
lieux = pd.DataFrame({
    'nom': ['Mines Paris', 'Panthéon', 'Notre-Dame', 'Tour Eiffel', 'Sacré-Cœur', 'Gare de Lyon'],
    'lon': [2.3390, 2.3459, 2.3499, 2.2945, 2.3431, 2.3739],
    'lat': [48.8453, 48.8462, 48.8530, 48.8584, 48.8867, 48.8443],
})
lieux
```

```{code-cell} ipython3
lieux = gpd.GeoDataFrame(
    lieux,
    geometry=gpd.points_from_xy(lieux.lon, lieux.lat),
    crs='EPSG:4326',                  # nos coordonnées sont des longitude, latitude
)
lieux
```

```{code-cell} ipython3
# on superpose les points aux quartiers

fig, ax = plt.subplots(figsize=(8, 6))
quartiers.plot(ax=ax, color='lightgrey', edgecolor='white')
lieux.plot(ax=ax, color='red')
```

### jointure spatiale

+++ {"tags": ["framed_cell"]}

````{admonition} →
jusqu'ici les jointures (`merge`) se faisaient sur **égalité de valeurs** de colonnes  
avec des données géographiques, on peut aussi *joindre* sur des **propriétés géographiques**

par exemple ici, pour chaque lieu, on veut savoir **dans quel quartier** il se trouve  
c'est le rôle de `gpd.sjoin()` (*spatial join*), avec un `predicate`, par exemple

* `"within"` le point est à l'intérieur du polygone
* `"intersects"` les formes ont une intersection
* ..
````

```{code-cell} ipython3
# pour chaque lieu, on ajoute les colonnes du quartier qui le contient
# (les deux GeoDataFrames doivent avoir le même crs)

lieux_quartiers = gpd.sjoin(lieux, quartiers, predicate='within')
lieux_quartiers[['nom', 'quartier', 'arrondissement']]
```

+++ {"tags": ["framed_cell"]}

````{admonition} →
et on peut bien sûr ensuite utiliser les outils `pandas` habituels  
par exemple pour compter le nombre de lieux par quartier, et l'ajouter aux quartiers
````

```{code-cell} ipython3
# combien de lieux par quartier ?

compte = lieux_quartiers.groupby('quartier').size().rename('nb_lieux')
compte
```

```{code-cell} ipython3
# on l'ajoute aux quartiers; ceux qui n'ont aucun lieu ont NaN, qu'on remplace par 0

quartiers_compte = quartiers.merge(compte, on='quartier', how='left')
quartiers_compte['nb_lieux'] = quartiers_compte['nb_lieux'].fillna(0)
quartiers_compte.plot(column='nb_lieux', cmap='Reds', legend=True, figsize=(8, 6))
```

```{admonition} pour aller plus loin
:class: seealso

* `gpd.sjoin_nearest()` joint chaque forme avec la forme **la plus proche**, pratique pour 'trouver la station de métro la plus proche'
* `gdf.to_file('mon-fichier.shp')` pour sauver
```

### regrouper avec `dissolve`

+++ {"tags": ["framed_cell"]}

````{admonition} →
les quartiers sont regroupés en 20 arrondissements, et on a leur numéro dans la colonne `arrondissement`  
on peut donc **fabriquer les arrondissements** à partir des quartiers, en fusionnant les formes qui ont le même numéro

c'est le rôle de `gdf.dissolve(by=...)`; c'est un peu comme un `groupby`, sauf que  
les formes sont **fusionnées** (par union) au lieu d'être simplement rassemblées

comme avec un `groupby`, il faut dire ce qu'on fait des autres colonnes avec `aggfunc`  
ici on veut additionner les surfaces
````

```{code-cell} ipython3
# as_index=False pour que 'arrondissement' reste une colonne

arrondissements = quartiers.dissolve(
    by='arrondissement', aggfunc={'surface': 'sum'}, as_index=False)
arrondissements.head(3)
```

```{code-cell} ipython3
# on a 20 formes, une par arrondissement

arrondissements.plot(column='surface', cmap='viridis', legend=True,
                     edgecolor='white', figsize=(8, 6))
```

```{admonition} attention à l'aggfunc
:class: warning

si on ne précise pas `aggfunc`, c'est `'first'` qui s'applique:  
on garderait pour chaque arrondissement les valeurs du **premier** quartier rencontré,  
ce qui n'a pas de sens pour la surface (ni pour le nom du quartier)
```

````{admonition} pour aller plus loin: sans dissolve
:class: dropdown seealso

on aurait pu obtenir le même résultat avec un `groupby` ordinaire  
la fusion des formes d'un groupe se fait avec `union_all()`

```python
arrondissements = gpd.GeoDataFrame({
    'surface': quartiers.groupby('arrondissement')['surface'].sum(),
    'geometry': quartiers.groupby('arrondissement')['geometry'].apply(lambda s: s.union_all()),
}, crs=quartiers.crs).reset_index()
```

`dissolve` est simplement plus pratique, et gère pour nous le `crs`
````

````{admonition} pour aller plus loin: dissolve ne sait faire que des unions
:class: dropdown seealso

`aggfunc` ne concerne que les colonnes **autres** que `geometry`  
pour les formes, `dissolve` fait toujours une **union**, et il n'y a pas de paramètre pour changer cela

pour une autre opération, par exemple une **intersection**, il faut passer par un `groupby` ordinaire  
et réduire soi-même les formes de chaque groupe

```python
from functools import reduce

quartiers.groupby('arrondissement')['geometry'].apply(
    lambda s: reduce(lambda a, b: a.intersection(b), s))
```
````

## les cartes avec `folium`

### une carte interactive avec `folium`

+++ {"tags": ["framed_cell"]}

````{admonition} →
pour finir, la librairie `folium` permet de produire des **cartes interactives** (basées sur *leaflet*)  
on peut les déplacer, zoomer, et afficher des infobulles (*tooltips*) au survol  
et cela reste vrai dans un fichier HTML

`folium` fonctionne avec les coordonnées **(latitude, longitude)**, dans cet ordre
````

```{code-cell} ipython3
import folium

# une carte centrée sur Paris
carte = folium.Map(location=[48.8566, 2.3522], zoom_start=12)

# les quartiers, avec leur nom en infobulle
folium.GeoJson(
    quartiers,
    tooltip=folium.GeoJsonTooltip(fields=['quartier', 'arrondissement']),
    style_function=lambda feature: {'weight': 1, 'color': 'grey', 'fillOpacity': 0.1},
).add_to(carte)

# nos lieux
for _, lieu in lieux.iterrows():
    folium.Marker(
        location=[lieu.lat, lieu.lon],
        tooltip=lieu.nom,
    ).add_to(carte)

carte
```

### encore plus court avec `explore`

+++ {"tags": ["framed_cell"]}

````{admonition} →
`geopandas` sait faire tout cela directement: `gdf.explore()` construit une carte `folium` à partir d'une `GeoDataFrame`  
on peut colorier selon une colonne comme avec `.plot()`, et choisir les colonnes à afficher en infobulle  

et comme `explore()` renvoie une carte `folium`, on peut superposer plusieurs couches  
en passant la carte déjà construite avec le paramètre `m=`

pour fonctionner, `explore()` a besoin du package `mapclassify`
````

```{code-cell} ipython3
# les arrondissements, coloriés selon leur surface
# en km2 pour que les valeurs de la légende restent courtes

carte = arrondissements.assign(km2=arrondissements.surface / 1e6).explore(
    column='km2', cmap='viridis', tooltip=['arrondissement', 'km2'])

# et par-dessus, nos lieux
lieux[['nom', 'geometry']].explore(m=carte, color='red', tooltip='nom')
```
