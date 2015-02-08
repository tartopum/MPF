# Concepts et généralités

## Problématique

L'objectif est d'appliquer une suite d'opérations sur des données afin d'en 
extraire des informations. Ces opérations seront regroupées en **analyses**, 
lesquelles correspondent à un ensemble de traitements sur les données ayant 
pour but d'extraire des informations sur ces dernières. Par exemple, une 
analyse peut être une moyenne mobile ou une régression linéaire. L'étude des 
données revient alors à chaîner des analyses :

<p align="center">
    <img src="img/analysis.png" alt="Principe des analyses" />
</p>

Par exemple :

* Sur les productions de chaque vache pour chaque lactation en fonction du temps
    * Première série
        * Moyenne mobile
    * Deuxième série
        * Régression linéaire
        * Moyenne des erreurs des régressions
    * Troisième série
        * ARMA
* Sur les productions de chaque vache pour chaque lactation en fonction de la consommation
    * Première série
        * Moyenne mobile
    * Deuxième série
        * Régression linéaire
        * Moyenne des erreurs des régressions

En n'oubliant pas que d'autres traitements peuvent s'ajouter au cours du temps, 
on obtient alors un **graphe d'analyses** :

<p align="center">
    <img src="img/analysis-graph.png" alt="Graphe d'analyses" />
</p>

Une vue devra être générée pour chaque résultat, sous quelque forme que ce soit 
(graphe, texte...), afin qu'il soit simple de faire des déductions. De plus, 
comme calculer prend du temps, un système de cache devra être mis en place.

## Structure des données

Les données sont cumulatives. Autrement dit, au fur et à mesure des analyses, 
les données s'étofferont. La structure des données pourra également être 
changée au cours du temps. Par exemple :

```python
# Original data
# All data of one cow

{
    "cow": "0001",
    "lact-1": {
        "lact": 1,
        "days": [1, 2, 3, ..., 350],
        "prods": [30, 25, 40, ..., 33],
        "cons": [11, 9, ...]
    },
    "lact-2": {
        "lact": 2,
        "days": [1, 2, 3, ..., 343],
        "prods": [14, 21, 37, ..., 25],
        "cons": [12, 8, 9]
    }
}

# Moving average

{
    "cow": "0001",
    "lact-1": {
        "lact": 1,
        "days": [1, 2, 3, ..., 350],
        "prods": [30, 25, 40, ..., 33],
        "cons": [11, 9, ...],
        "days-ma-step3": [3, 4, ..., 348],
        "prods-ma-step3": [37, ...]
    },
    "lact-2": {
        "lact": 2,
        "days": [1, 2, 3, ..., 343],
        "prods": [14, 21, 37, ..., 25],
        "cons": [12, 8, 9],
        "days-ma-step3": [3, 4, ..., 348],
        "prods-ma-step3": [30, ...]
    }
}

# Linear regression
# B = AX
# B: prods
# A: day, lactation, consumption...

{
    "cow": "0001",
    "lact-1": {
        "lact": 1,
        "days": [1, 2, 3, ..., 350],
        "prods": [30, 25, 40, ..., 33],
        "cons": [11, 9, ...],
        "days-ma-step3": [3, 4, ..., 348],
        "prods-ma-step3": [37, ...],
        "X": [...],
        "A": [...],
        "linreg-error": 12.5
    },
    "lact-2": {
        "lact": 2,
        "days": [1, 2, 3, ..., 343],
        "prods": [14, 21, 37, ..., 25],
        "cons": [12, 8, 9],
        "days-ma-step3": [3, 4, ..., 348],
        "prods-ma-step3": [30, ...],
        "X": [...],
        "A": [...],
        "linreg-error": 11.7
    }
}

# Statistics measures

{
    "cow": "0001",
    "linreg-error-mean": 12.1,
    "lact-1": {
        "lact": 1,
        "days": [1, 2, 3, ..., 350],
        "prods": [30, 25, 40, ..., 33],
        "cons": [11, 9, ...],
        "days-ma-step3": [3, 4, ..., 348],
        "prods-ma-step3": [37, ...],
        "X": [...],
        "A": [...],
        "linreg-error": 12.5
    },
    "lact-2": {
        "lact": 2,
        "days": [1, 2, 3, ..., 343],
        "prods": [14, 21, 37, ..., 25],
        "cons": [12, 8, 9],
        "days-ma-step3": [3, 4, ..., 348],
        "prods-ma-step3": [30, ...],
        "X": [...],
        "A": [...],
        "linreg-error": 11.7
    }
}
```

Les données d'origine seront récupérées en interrogeant une base de données, 
avec de simples requêtes SQL.

### Un exemple

<p align="center">
    <img src="img/analysis-graph-example.png" alt="Exemple de graphe d'analyses" />
</p>

1. **Vache X, lact Y :** productions journalières pendant la lactation Y de la 
vache X.
2. **1. Vache 1, lact 1, identité :** uniquement pour bénéficier des effets de bord 
tels que la vue et le cache.
3. **Vache 1, lact 1, moyenne mobile :** on applique une moyenne mobile aux 
données.
4. **Vache 1, lact 1, régression linéaire :** on effectue une régression 
linéaire des données. On ajoute alors à ces dernières l'erreur obtenue ainsi 
que les matrices A et X (B = AX, B étant les productions).
5. **Vache 1, lact 2, identité :** comme 2.
6. **Vache 1, lact 2, régression linéaire :** comme 4.
7. **Vache 2, lact 1, identité :** comme 2.
8. **Vache 2, lact 1, régression linéaire :** comme 4.
9. **Vache 1, fusion :** on fusionne les données reçues des régressions afin de 
mener des mesures statistiques dessus.
10. **Vache 1, statistiques :** on calcule la moyenne des erreurs obtenues lors 
des régressions.
11. **Vaches 1 et 2, fusion :** comme 9.
12. **Vaches 1 et 2, statistiques :** comme 10.

L'idéal serait d'en déduire un code comme ça (cf : [facteur]
(https://github.com/Vayel/Facteur)), en ce qui concerne la vache 1 :

```python
# Create nodes
id_node_lact1 = Node(
    worker = identity, 
    collector = ["origin"], 
    key_out = "identity_1"
)

id_node_lact2 = Node(
    worker = identity, 
    collector = ["origin"], 
    key_out = "identity_2"
)

ma_node_lact1 = Node(
    worker = moving_averaging, 
    collector = ["origin"], 
    key_out = "ma_1"
)

linreg_node_lact1 = Node(
    worker = linear_regression, 
    collector = ["identity_1"], 
    key_out = "linreg_1"
)

linreg_node_lact2 = Node(
    worker = linear_regression, 
    collector = ["identity_2"], 
    key_out = "linreg_2"
)

stats_node = Node(
    worker = statistics, 
    collector = ["linreg_1", "linreg_2"], 
    key_out = "stats"
)

# Connect nodes
id_node_lact1 >> linreg_node_lact1 >> stats_node
id_node_lact2 >> linreg_node_lact2 >> stats_node

# Launch
original_data = {
    "cow": "0001",
    "lact-1": {
        "lact": 1,
        "days": [1, 2, 3, ..., 350],
        "prods": [30, 25, 40, ..., 33],
        "cons": [11, 9, ...]
    },
    "lact-2": {
        "lact": 2,
        "days": [1, 2, 3, ..., 343],
        "prods": [14, 21, 37, ..., 25],
        "cons": [12, 8, 9]
    }
}

id_node.collect({"origin": original_data})

ma_node.collect({"origin": original_data})
```

Même s'il faut améliorer le fait de devoir créer deux fois le même noeud (par 
exemple, `id_node_lact1` et `id_node_lact2`).

## Structure des analyses

Une analyse consiste à effectuer une série d'opérations sur un ensemble de 
données. Le résultat de ces opérations devra être mis en cache, représenté par 
une vue (un graphe par exemple) et transmis aux analyses suivantes. Une analyse 
comporte alors plusieurs composants :

### Un système de cache

Le système de cache permet de sauvegarder le résultat d'un calcul afin de 
pouvoir le récupérer directement par la suite. Chaque calcul se verra attribué 
un identifiant, en générant un condensat de ses propriétés :

* Vache
* Lactation
* Arguments

Les deux premières n'étant valable que dans certains cas, puisqu'un calcul ne 
fait pas nécessairement intervenir une lactation entière, une seule lactation 
ou une seule vache.

Le système de cache prend donc en argument l'identifiant du calcul et le 
résultat du calcul.

### Une *view*

Une vue s'occupe de représenter les données dans un format facilement 
exploitable par l'homme.

### Un *processor*

Composant chargé du calcul brut.

En pratique, le *processor* est attaché au *worker*.

### Un *worker*

Le *worker* est la pièce maîtresse. Il se charge de récupérer les données qui 
l'intéressent, de demander au *processor* d'en générer d'autres à partir 
d'elles, de stocker le résultat dans les données, d'appeler le système de mise 
en cache et la vue.

### La configuration

Configurer une analyse revient à lui fournir un *worker*, une *view*, un 
système de cache et d'autres paramètres.

#### Les *getters*

La structure des données reçues par un *worker* dépend des analyses effectuées 
auparavant. Ainsi, il faut fournir au *worker* un moyen de récupérer, parmi le 
dictionnaire reçu en argument, les données dont il a besoin.

En pratique, on lui fournira une fonction, appelée *getter*, se chargeant de 
faire cela.

#### Les *setters*

De même, il faut lui spécifier où sauvegarder les résultats dans le 
dictionnaire.

En pratique, cela sera fait en lui fournissant une fonction, appelée *setter*, 
se chargeant de faire cela.

