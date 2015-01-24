# Les méthodes de prévision

## De la prévision en général 

Suite à quelques recherches, deux pistes principales se dégagent :

* Régression
* Modèle ARMA

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

### Sources

* [Méthodes de prévision](http://drupal.mgi.polymtl.ca/?q=book/export/html/19)
* [Notions de base](http://unt-ori2.crihan.fr/unspf/2010_Limoges_Vignoles_StatsDescriptives/co/03-4-4%20interpolation-extrapolation.html)

## Régression linéaire

### Sources

* [Présentation](http://fr.wikipedia.org/wiki/R%C3%A9gression_%28statistiques%29)

## Modèle ARMA

### Sources

* [Présentation](http://fr.wikipedia.org/wiki/ARMA)
* [Séries temporelles](http://www.itl.nist.gov/div898/handbook/pmc/section4/pmc4.htm)
