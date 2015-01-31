# Concepts et généralités

Le projet nécessite la manipulation de <a href="data.md">données</a> afin d'en 
extraire des informations et de prédire celles futures. Cela s'organise sous 
forme d'un ensemble d'<a href="analysis.md">analyses</a> dont l'objectif est, 
à partir de données, d'en générer d'autres avec les résultats d'une suite de 
calculs. Ces données sont communiquées à l'analyse suivante, afin qu'elle 
puisse en profiter.

<p align="center">
    <img src="img/analysis.png" alt="Principe des analyses" />
</p>

On obtient alors un **graphe d'analyses** :

<p align="center">
    <img src="img/analysis-graph.png" alt="Graphe d'analyses" />
</p>

## Un exemple

<p align="center">
    <img src="img/analysis-graph-example.png" alt="Exemple de graphe d'analyses" />
</p>

### Les données

Les données d'origine sont simplement, pour une vache et une lactation fixées, 
la production laitière par jour.

### L'identité

On ne fait rien. Cela permet juste de bénéficier des effets de bord tels que la 
génération d'une vue (par exemple, un graphe).

### La moyenne mobile

On applique une moyenne mobile sur les données.

### La régression linéaire

On effectue une régression linéaire des données et ajoute l'erreur obtenue à 
ces dernières.

### Les statistiques

On calcule les grandeurs statistiques liées aux données. Par exemple, la 
moyenne des erreurs obtenues pour les régressions linéaires.

### La fusion

On rassemble des données entre elles en vue d'une opération sur elles. Par 
exemple, pour calculer les grandeurs statistiques mentionnées juste au-dessus.

## Les mathématiques dans tout ça

Les outils mathématiques utilisés pour effectuer les calculs de prévision sont 
explicités <a href="forecasting.md">ici</a>.
