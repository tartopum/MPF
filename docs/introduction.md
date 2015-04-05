# Introduction 

L'objectif des analyses des données est double :

* Prévoir la production future sur court terme (un mois)
* Etudier l'influence de certains paramètres sur la production (âge, 
consommation...)

## De la prévision en général 

Suite à quelques recherches, deux pistes principales se dégagent :

* La régression linéaire
* Les séries temporelles

Plus de détails 
[ici](http://zestedesavoir.com/forums/sujet/1514/prevoir-une-evolution-a-partir-de-courbes/).

Dans tous les cas, il est nécessaire de partager les données en deux : 

* Certaines permettant de générer un modèle ;
* D'autres pour le vérifier.

Cela peut se faire en considérant différentes lactations ou vaches, mais 
également en supprimant des points au hasard lors de la génération du modèle et 
en vérifiant ce dernier sur les points mis de côté.

En outre, on pourra au préalable éliminer le bruit des données, c'est-à-dire 
faire en sorte que les évènements aléatoires et peu représentatifs - 
la vache était malade par exemple - n'influencent pas trop l'analyse. Lisser 
les courbes - avec une moyenne mobile notamment - semble être judicieux.
