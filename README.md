# MPF - Milk Production Forecast

## Problématique

Les producteurs de lait ont des **quotas** à respecter, c'est-à-dire une 
**quantité maximale** de lait à produire par semaine/mois/année... En 
dessous de cette limite, ils effectuent moins de profits. Au dessus, 
ils paient une ammende. Or, il est clair que la production est en 
corélation avec l'alimentation : le type et la quantité. L'objectif est 
donc de **prévoir la production** sur le moyen terme - mois suivant - et, 
à partir de ces résultats, d'**ajuster l'alimentation** pour correspondre 
aux quotas.

Ce projet est mené en collaboration avec mon oncle agriculteur en 
possession d'un robot de traite. Il est donc en mesure de fournir 
les productions quotidiennes de chaque vache, de leur première 
lactation jusqu'à aujourd'hui.

Pour information, sans compter les aléas tels que les maladies, une 
vache suit le cycle suivant, qu'on appelle *lactation* :

* **Vêlage :** la vache donne naissance.
* **Production :** la vache est traite.
* **Insémination :** la vache est inséminée. Il est parfois nécessaire de répéter 
cette étape.
* **Production :** la vache est traite.
* **Tarissement :** le vêlage est proche, la vache n'est plus traite jusqu'au 
vêlage.

## Organisation

Le dépôt, se partagera en plusieurs parties :

* **Les données :** les productions quotidiennes de chaque vache.
* **Les scripts :** les morceaux de code permettant d'analyser les données. 
Python 3 sera utilisé pour cela.
* **Les analyses :** l'étude des premières, générées par les seconds.

D'autre part, comme, accessoirement, ce projet constitue mon TIPE d'année de 
Spé, il faudra veiller à rester simple et concis, de manière à pouvoir 
présenter une soutenance potable à la fin de l'année. Le plus dur sera donc 
d'utiliser des outils compréhensibles permettant de produire un résultat 
satisfaisant.

En outre, dans un premier temps, seuls le temps et l'alimentation seront 
considérés : les autres facteurs pouvant influencer la production ne seront pas 
pris en compte pour des raisons de simplicité.

## Pistes

Suite à quelques recherches, deux pistes principales se dégagent :

* Régression
* Modèle ARMA

Plus de détails 
[ici](http://zestedesavoir.com/forums/sujet/1514/prevoir-une-evolution-a-partir-de-courbes/).

Dans tous les cas, il semble nécessaire de partager les données en deux : 

* Certaines permettant de générer un modèle ;
* D'autres pour le vérifier.

Cela peut se faire en considérant différentes lactations ou vaches, mais 
également en supprimant des points au hasard lors de la génération du modèle et 
en vérifiant ce dernier sur les points mis de côté.

En outre, il faudra au préalable éliminer le bruit des données, c'est-à-dire 
faire en sorte que les évènements aléatoires et peu représentatifs - 
la vache était malade par exemple - n'influencent pas trop l'analyse. Lisser 
les courbes - avec une moyenne mobile notamment - semble être judicieux.

## Sources

* Global
    * [Méthodes de prévision](http://drupal.mgi.polymtl.ca/?q=book/export/html/19)
    * [Notions de base](http://unt-ori2.crihan.fr/unspf/2010_Limoges_Vignoles_StatsDescriptives/co/03-4-4%20interpolation-extrapolation.html)
* Régression
    * [Présentation](http://fr.wikipedia.org/wiki/R%C3%A9gression_%28statistiques%29)
* ARMA
    * [Présentation](http://fr.wikipedia.org/wiki/ARMA)
