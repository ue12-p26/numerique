---
date: 2026/10/01
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
---

# TP World Bank indicators 1) merge

+++

In this assignment we deal with World Bank indicators. The data comes in several separate files, so we will

1. **merge** them into a single, clean dataframe

```{code-cell} ipython3
import numpy as np
import pandas as pd
```

## the data

+++

put the four files in the `data/` folder: `life-expectancy.csv`, `gdp_per_capita.csv`, `population.csv`, `countries.csv`

+++

| file | one row per | main column |
|-|-|-|
| `life-expectancy.csv` | country and year | `life_exp` (years) |
| `gdp-per-capita.csv` | country and year | `gdp_per_capita` (current US$) |
| `population.csv` | country and year | `population` |
| `countries.csv` | country | `region`, `income_level` |

+++

### loading

+++

load each of the four files into a dataframe, named respectively `life`, `gdp`, `pop` and `countries`  
and have a look at each of them: shape, first rows, types

```{code-cell} ipython3
# your code
countries = pd.read_csv('data/countries.csv')
gdp = pd.read_csv('data/gdp-per-capita.csv')
life = pd.read_csv('data/life-expectancy.csv')
pop = pd.read_csv('data/population.csv')
```

### content

to better understand what we have at hand, answer these questions

1. how many rows do we have in each table  
2. the three indicator files have the same columns `country_code`, `country`, `year`  
   what are the rows that identify a measure uniquely ? so, what are the **two columns** we need to merge on ?

+++

your answer :

```{code-cell} ipython3
# your code
for df in [countries, gdp, life, pop]:
    print(df.shape[0], ' rows')
    display(  df.head(2)   )
    print(  df.duplicated().sum(), ' duplicated rows')
```

## merging

+++

### how many rows for the merge ?

+++

we're trying to foresee how many rows a merge would yield

the three files do not have the same number of rows: what does that tell you ?  
it is not enough to conclude by itself, we need to know how the keys of the 3 dataframes compare:

1. how do the keys of `life` and `pop` compare ? (number)
2. same question for `life` and `gdp` ?

3. (see hint) and so, how many rows do you expect from an inner merges  
    https://pandas.pydata.org/docs/reference/api/pandas.DataFrame.merge.html  
**inner**: use intersection of keys from both frame  
4. and from an outer merge ? how many undefined data will the outer merge contain ?  
**outer**: use union of keys from both frames  
 

**Hints**

1. note that you can pass a list of columns to `set_index` (you obtain a multi-index)    
    and access the index  
    ```python
    df = pop.set_index(['country_code', 'year'])
    df.index
    ->
    MultiIndex([('AFE', 2020),
                ('AFE', 2019),
                .../...
    ```
2. then, note that the `index` can be considered as a `set`  
   with operations such as `union`, `intersection`

----------

3. the hint: **a common trick** is to:
    - compute the index made of the key columns:
    ```python
    keys = df.set_index([..., ...]).index
    ```
    
    - and then use set-like operations (`difference`, `intersection`, `union`) on these keys;
    - note however that `==` to compare 2 indexes **is not the right tool here**
    consider using `symmetric_difference()` instead

```{code-cell} ipython3
# your code
# inner is intersection
s1 = pop.set_index(['country_code', 'year']).index.intersection(gdp.set_index(['country_code', 'year']).index)
len(s1)
```

```{code-cell} ipython3
# your code
# outer is union
s2 = pop.set_index(['country_code', 'year']).index.union(gdp.set_index(['country_code', 'year']).index)
len(s2)
```

```{code-cell} ipython3
# your code (1)
try:
    s1 == s2
except ValueError as e:
    print(e)
```

```{code-cell} ipython3
# your code (2)
len(   s1.symmetric_difference(s2)   )
```

### merging the indicators

+++

merge `life`, `gdp` and `pop` into a single dataframe `indicators`, with **these 6 columns**

`country_code, country, year, life_exp, gdp_per_capita, population`

do this twice:

1. once with the default (inner) merge,
2. and once with `how="outer"`
3. compare the number of rows with the expectations
4. finally check for missing data in both; does that add up with the previous question ?

:::{admonition} hint
:class: tip dropdown

the `country` column is already in `life`, so you do not want to get it again from the other dataframes
:::

```{code-cell} ipython3
# your code
df_aux = pd.merge(left=life, left_on=['country_code', 'year'],
                  right=gdp, right_on=['country_code', 'year'],
                  how='inner')
df_inner = pd.merge(left=df_aux, left_on=['country_code', 'year'],
                    right=pop, right_on=['country_code', 'year'],
                    how='inner')
```

```{code-cell} ipython3
# your code
df_aux = pd.merge(left=life, left_on=['country_code', 'year'],
                  right=gdp, right_on=['country_code', 'year'],
                  how='outer')
df_outer = pd.merge(left=df_aux, left_on=['country_code', 'year'],
                    right=pop, right_on=['country_code', 'year'],
                    how='outer')
```

```{code-cell} ipython3
df_inner.isna().sum(axis=0)
```

```{code-cell} ipython3
df_outer.isna().sum(axis=0)
```

```{code-cell} ipython3
df_outer.shape[0]- df_inner.shape[0] # yep
```

```{code-cell} ipython3
len(   df_outer.set_index(['country_code', 'year']).index.difference(df_inner.set_index(['country_code', 'year']).index)   )
```

```{code-cell} ipython3
df_outer.set_index(['country_code', 'year']).loc[('AFG', 1990)]  # gdp is missing (gdp has less entries that pop and life
```

which kind of merge one do you prefer here, and why ?  
(for the rest of the assignment, we keep the outer version, to see the missing values)

+++

### adding the regions

+++

now we want to add the `region` and `income_level` columns to `indicators`, taken from `countries`  
this time we merge on one column only: `country_code`

1. how many rows do you expect in the result ?  
   (for a given country, is there one row or several in the `countries` table ?)
2. merge, and call the result `df`; check that you get the number of rows you expected
3. you now have both a `country` and a `name` column, that seem to contain the same thing;
  (optional step) double-check they genuinely are identical
4. drop the `name` column

:::{admonition} hint
:class: tip dropdown
maybe `Series.is_unique` can come in handy
:::

```{code-cell} ipython3
# your code
pd.merge(left=df_inner, left_on='country_code',
         right=countries, right_on='country_code',
         how='left')
```

### cleaning

+++

Suppress the redundant columns if any

```{code-cell} ipython3
# your code
```

## appendix: where does the data come from

+++

all the data was downloaded once from the [World Bank open data API](https://datahelpdesk.worldbank.org/knowledgebase/topics/125589), restricted to the years 1990 to 2020

* life expectancy at birth: indicator `SP.DYN.LE00.IN`
* GDP per capita, current US$: indicator `NY.GDP.PCAP.CD`
* total population: indicator `SP.POP.TOTL`
* country metadata (region, income level): the `country` endpoint

for example, with [httpie](https://httpie.io/), the life expectancy for all countries, in 2019 only, as json (`format==json` and the other `==` are query parameters)

```bash
http "https://api.worldbank.org/v2/country/all/indicator/SP.DYN.LE00.IN" format==json date==2019 per_page==300
```

for the years used here, replace the date with `date==1990:2020`, and use `per_page==20000` to get everything in one page  
the country metadata is at `https://api.worldbank.org/v2/country`  
the script `fetch-data.py`, next to this notebook, does the whole job with Python's `requests` library instead

rows with no value were dropped from the three indicator files, which is why they do not all cover the same country / year pairs
