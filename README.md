# BSQ

Une map de "." qui veut dire emplacement libre et de "o" qui veut dire emplacement prise. Le but est de trouver le plus grand carré dans cette map et le placer en "x". J'ai réaslisé un algorithme en python qui permet de trouver le plus grand carré selon les différents map.

Prends en paramètre le fichier contenant la map, généré par generator.sh

python3 bsq.py map

# generator

Gènére la map, néccéssite 3 paramètres: 
param 1: (integer) le nombre de lignes
param 2: (integer) le nombre de colonnes
param 3: (integer) la densité d'emplacement libre/occupé

perl generator.sh 10 10 10

#Anagram

Permet de trouver des anagram d'un mot, même nombre de caractères et mêmes caractères.
Prend en paramètre le mot:

python3 anagram.py marie

