# Structure du code

Le code se partage en deux dossiers principaux : `mpf` et `analysis`. Le 
premier contient le code formant une API et le second utilise cette API.

## L'API

L'API fait intervenir plusieurs composants.

### Les *processors*

Un *processor* effectue du calcul brut.

### Les *views*

Une vue a pour objectif de représenter des données.

### Les *models*

Un modèle est chargé de manipuler les données : récupération dans la base, 
sérialisation, sauvegarde...

### Les *workers*

Un *worker* correspond à une analyse. Il prend en paramètres la vue, les 
données et des arguments utiles au calcul puis effectue l'analyse.

## Les analyses

Une analyse consiste tout simplement à configurer des composants et à 
démarrer un *worker*. 

Par exemple :

```python

```

## En résumé

TODO
