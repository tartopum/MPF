# Les données

Les données brutes sont exportées de la base de données du robot de traite 
puis sont stockées dans le dossier `data/vms/`. 

Afin de les manipuler plus facilement par la suite, une base SQlite a été 
créée. Les fichiers relatifs à cette dernière sont stockés dans `data/db/`. Le 
programme `mpf/utils/build_database.py` est utilisé pour initialiser la base.

Une fois cela effectué, on emploie le programme `mpf/utils/vms_to_db.py` pour 
lire les données brutes, filtrer celles exploitables et les stocker dans la 
base.

Les analyses génèreront deux types de données : les résultats et les vues. Les 
premiers seront mis en cache dans le dossier `data/cache/` afin d'éviter la 
répétition des calculs. Les secondes seront des fichiers PDF permettant la 
visualisation des résultats. Ces fichiers seront stockés par thèmes dans des 
sous-dossiers du répertoire `views/`.
