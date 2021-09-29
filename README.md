# face-mask-dataset-ilc-2021
Le dataset des images du projet d'IA de 2021, **Indiquez vos id git dans la issue pour les droits**

TL;DR:
- Choisir 200 images JPEG avec environ 1/3 sans masque, 1/3 avec masque, et 1/3 mal mis
- Renommer les images avec le hash md5 du fichier 
- Annoter avec labelimg (ou autre pour fichier xml au format PASCAL-VOC)
- commit sur votre branch "contrib_NOM1_NOM2"
- Une fois toutes les images annotées, => Pull requests vers branche VALID
- Le discord ILC est pratique pour échanger


## 1. Répartition 
Les images sont repertoriées en 3 catégories :
- "with_mask", un masque correctment porté et qui recouvre la bouche et le nez
- "with_incorrect_mask", un masque porté sous le nez, ou de facon pas très covid-friendly
- "without_mask, Un visage sans masque

Le dataset doit faire environ 2300 images qui répartit par 23 doit donner environ **100 images à annoter par personne**


## 2. Gestion des images
Les images doivent être traitées de la sorte :
- Le nom correspond au md5sum du fichier
- Les masques rajoutés en mode photoshop sont à proscrire pour des raisons de performances
- on recherche les images similaires par exemple à l’aide du script python compare_images
- La répartition des images doivent être équilibrés (environ le même nombre d'image dans chaque catégorie à 100 images près)

## 3. Pour commit
L'idée va être d'avoir une branche "VALID" pour ajouter toutes les images en attentes de validation et de ne garder la branche "main" que pour le résultat final.
Pensez à bien mettre renseigner vos avancés dans vos commits et pull request.
-> Chaque binome ajoutera sur sa branche "contrib_NOM1_NOM2", et on effectuera un pull request vers la branche "VALID" une fois les 200 images ajoutées et annotées


## 4. Les outils qui vont bien
Pour annoter les images : labelimg
Pour trouver les doublons dans les images : Le script "compare_images.py" (run n'importe ou)
Pour renommer toutes ses images en leur hash MD5 (***A faire avant d'annoter***) : le script "rename_dir_md5.py" (à déplacer dans le dossier JPEGImages pour run)
