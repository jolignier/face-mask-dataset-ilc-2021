# face-mask-dataset-ilc-2021
Le dataset des images du projet d'IA de 2021

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
