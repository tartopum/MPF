# Théorie des données

Le projet nécessite la manipulation de données afin d'en extraire des 
informations et de prédire celles futures. Un ensemble de données peut 
représenter tout et n'importe quoi :

* La liste des numéros des animaux
* La production par jour, pour une vache fixée et toutes ses lactations
* La production selon la consommation, pour toutes les vaches et toutes les 
lactations
* La consommation par jour, pour la nième lactation de certaines vaches
* ...

## Structure

Les analyses manipulent des ensembles de données, représentés sous forme d'un 
dictionnaire Python. Chaque ensemble est alors partagé en sous-ensembles, 
eux-mêmes pouvant l'être, etc.

Par exemple :

```python
data_0001 = {
    "lact-1": {
        "days": [1, 2, 3, ..., 350],
        "prods": [30, 25, 40, ..., 33]
    },
    "lact-2": {
        ...
    }
}
```

## Manipulations

Au fur et à mesure des analyses, les données verront leur structure changer. Il 
existe trois manières à cela.

### En place

La structure ne change pas, seules les données sont modifiées. 

Par exemple, en lissant des données, on conserve une liste mais le contenu a 
changé :

```python
data_0001 = {
    "lact-1": {
        "days": [1, 2, 3, ..., 350],
        "prods": [30, 25, 40, ..., 33]
    },
    "lact-2": {
        ...
    }
}
```

```python
data_0001 = {
    "lact-1": {
        "days": [2, 3, ...],
        "prods": [27.5, 32.5, ...]
    },
    "lact-2": {
        ...
    }
}
```

### Ajouts

Il sera parfois nécessaire d'ajouter des données. 

Par exemple, suite à une régression linéaire, on peut souhaiter préciser 
l'erreur obtenue :


```python
data_0001 = {
    "lact-1": {
        "days": [1, 2, 3, ..., 350],
        "prods": [30, 25, 40, ..., 33]
    },
    "lact-2": {
        ...
    }
}
```

```python
data_0001 = {
    "lact-1": {
        "days": [1, 2, 3, ..., 350],
        "prods": [30, 25, 40, ..., 33],
        "linreg-error": 12.5
    },
    "lact-2": {
        ...
    }
}
```

Puis faire la moyenne des erreurs pour toutes les lactations :

```python
data_0001 = {
    "lact-1": {
        "days": [1, 2, 3, ..., 350],
        "prods": [30, 25, 40, ..., 33],
        "linreg-error": 12.5
    },
    "lact-2": {
        ...
    }
}
```

```python
data_0001 = {
    "linreg-error-mean": 8.3,
    "lact-1": {
        "days": [1, 2, 3, ..., 350],
        "prods": [30, 25, 40, ..., 33],
        "linreg-error": 12.5
    },
    "lact-2": {
        ...
    }
}
```

### Combinaisons

Il s'avèrera nécessaire de combiner des données. 

Par exemple, une régression linéaire a été faite sur la production par jour de 
trois vaches et les erreurs ont été intégrées aux données, et on souhaite 
effectuer la moyenne de ces erreurs :


```python
data_0001 = {
    "linreg-error-mean": 8.3,
    "lact-1": {
        "days": [1, 2, 3, ..., 350],
        "prods": [30, 25, 40, ..., 33],
        "linreg-error": 12.5
    },
    "lact-2": {
        ...
    }
}

data_0002 = {
    "linreg-error-mean": 12.1,
    "lact-1": {
        "days": [1, 2, 3, ..., 350],
        "prods": [28, 32, 26, ..., 44],
        "linreg-error": 9.6
    },
    "lact-2": {
        ...
    }
}
```

```python
data = {
    "linreg-error-mean": 10.2,
    "0001": {
        "linreg-error-mean": 8.3,
        "lact-1": {
            "days": [1, 2, 3, ..., 350],
            "prods": [30, 25, 40, ..., 33],
            "linreg-error": 12.5
        },
        "lact-2": {
            ...
        }
    },
    "0002": {
        "linreg-error-mean": 12.1,
        "lact-1": {
            "days": [1, 2, 3, ..., 350],
            "prods": [28, 32, 26, ..., 44],
            "linreg-error": 9.6
        },
        "lact-2": {
            ...
        }
    }
}
```
