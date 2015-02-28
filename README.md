# MPF - Milk Production Forecast

![Build Status](https://travis-ci.org/Vayel/MPF.svg?branch=master)

Les producteurs de lait ont des **quotas** à respecter, c'est-à-dire une 
**quantité maximale** de lait à produire par année (la campagne laitière dure 
du 1er avril au 31 mars) : en dessous de cette limite, ils effectuent moins de 
profits et au dessus, ils paient une ammende. Or, il est clair que la production 
est en corélation avec l'alimentation : le type et la quantité. L'objectif est 
donc de **prévoir la production** et, à partir de ces résultats, d'**ajuster 
l'alimentation** pour correspondre aux quotas.

Pour information, sans compter les aléas tels que les maladies, une 
vache suit le cycle suivant, qu'on appelle *lactation* :

* **Vêlage :** la vache donne naissance.
* **Production :** la vache est traite.
* **Insémination :** la vache est inséminée. Il est parfois nécessaire de 
répéter cette étape.
* **Production :** la vache est traite.
* **Tarissement :** le vêlage est proche, la vache n'est plus traite jusqu'au 
vêlage.

Ce projet est mené en collaboration avec mon oncle agriculteur en 
possession d'un **robot de traite**. Il est donc en mesure de fournir des 
données sur chaque vache, de leur première lactation jusqu'à aujourd'hui. Pour 
un animal et un jour donnés, on possède :

* La date
* La production laitière
* La consommation en granulés
* Le numéro de la lactation (première, deuxième...)
* Le numéro du jour de lactation (nième jour après le vêlage)

De plus, le robot de traite permet d'enregistrer des évènements, desquels 
certains jours, pour un animal donné, sont estampillés :

* Vêlage
* Tarissement
* Gestante/non gestante (suite à une échographie)
* Insémination
* Maladie/traitement

Plus d'informations dans la documentation.
