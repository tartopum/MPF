# Les données

Les données brutes sont exportées de la base de données du robot de traite 
puis sont stockées dans le dossier `data/vms/`. 

Afin de les manipuler plus facilement par la suite, une base SQlite a été 
créée. Les fichiers relatifs à cette dernière sont stockés dans `data/db/`. Le 
programme `mpf/utils/build_database.py` est utilisé pour initialiser la base.

Une fois cela effectué, on emploie le programme `mpf/utils/vms_to_db.py` pour 
lire les données brutes, filtrer celles exploitables et les stocker dans la 
base.
