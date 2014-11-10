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

* **Vêlage :** oh ! un veau ! 
* **Production :** la vache est traite.
* **Insémination :** la vache est inséminée. Il est parfois nécessaire de répéter 
cette étape.
* **Production :** la vache est traite.
* **Tarissement :** le vêlage est proche, la vache n'est plus traite jusqu'au 
vêlage.

## Organisation

Dans un premier temps, les facteurs influençant la production ne seront pas 
pris en compte pour des raisons de simplicité. Peut-être l'insémination 
induit-elle une baisse de la production, peut-être pas. Ici, seules les 
données de production passées seront considérées.

Le dépôt, quant à lui, se partagera en plusieurs parties :

* **Les données :** les productions quotidiennes de chaque vache, illustrées 
par des courbes.
* **Les scripts :** les morceaux de code permettant d'analyser les données. 
Python 3 sera utilisé pour cela.
* **Les analyses :** l'étude des premières, générées par les seconds.

D'autre part, comme, accessoirement, ce projet constitue mon TIPE d'année de 
Spé, il faudra veiller à rester simple et concis, de manière à pouvoir 
présenter une soutenance potable à la fin de l'année. Le plus dur sera donc 
de dénicher des outils compréhensibles permettant de produire un résultat 
satisfaisant.

## Pistes

Suite à quelques recherches, plusieurs pistes se dégagent :

* Droite des moindres carrés
* Transformée de Fourier
* *Machine learning*
* Modèle ARMA

Plus de détails 
[ici](http://zestedesavoir.com/forums/sujet/1514/prevoir-une-evolution-a-partir-de-courbes/).

Dans tous les cas, il semble nécessaire de partager les données en deux : 

* Certaines permettant de générer un modèle ;
* D'autres, et pourquoi pas les précédentes également, pour le vérifier.

En outre, il faudra au préalable éliminer le bruit des données, c'est-à-dire 
faire en sorte que les évènements aléatoires et peu représentatifs - 
la vache était malade par exemple - n'influencent pas trop l'analyse. Lisser 
les courbes - avec une moyenne mobile notamment - semble être judicieux.

## Sources

* Mathématiques
    * [Méthodes de prévision](http://drupal.mgi.polymtl.ca/?q=book/export/html/19)
    * [Corrélation](http://fr.wikipedia.org/wiki/Corr%C3%A9lation_%28statistiques%29)
* Excel
    * [Méthodes de prévision](http://www.lokad.com/fr/methodes-previsions-et-formules-excel)
