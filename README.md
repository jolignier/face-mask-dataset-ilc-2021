# face-mask-dataset-ilc-2021
Le dataset des images du projet d'IA de 2021, **Indiquez vos id git dans la issue pour les droits**

## 1. Répartition 
Les images sont repertoriées en 3 catégories :
- "with_mask", un masque correctment porté et qui recouvre la bouche et le nez
- "with_incorrect_mask", un masque porté sous le nez, ou de facon pas très covid-friendly
- "without_mask, Un visage sans masque
La dataset doit faire environ 2300 images qui répartit par 23 doit donner environ **100 images à annoter par personne**


## 2. Gestion des images
Les images doivent être traitées de la sorte :
- Le nom correspond au md5sum du fichier
- Les masques rajoutés en mode photoshop sont à proscrire pour des raisons de performances
- on recherche les images similaires par exemple à l’aide de https://betterprogramming.pub/how-to-measure-imagesimilarities-in-python-12f1cb2b7281 et on choisit un bon descripteur pour éliminer les doublons
- La répartition des images doivent être équilibrés (environ le même nombre d'image dans chaque catégorie à 100 images près)

## 3. Pour commit
L'idée va être d'avoir une branche "VALID" pour ajouter toutes les images en attentes de validation et de ne garder la branche "main" que pour le résultat final.
Pensez à bien mettre renseigner vos avancés dans vos commits et pull request.
-> Chaque binome ajoutera sur sa branche "contrib_NOM1_NOM2", et on effectuera un pull request vers la branche "VALID" une fois les 200 images ajoutées et annotées


## 4. Les outils qui vont bien
Pour annoter les images : labelimg
