"score" calcule le score pour une combinaison de dés donnée, selon les règles d'un jeu fictif.

La fonction prend en entrée une liste "dice" de nombres entiers représentant les faces des dés.

Elle crée un dictionnaire "points" qui associe à chaque face un nombre de points, en suivant les règles du jeu : un triple de 1 vaut 1000 points, un triple de 6 vaut 600 points, un triple de 5 vaut 500 points, un triple de 4 vaut 400 points, un triple de 3 vaut 300 points et un triple de 2 vaut 200 points.

Ensuite, la fonction crée un dictionnaire "dices" qui compte le nombre de dés pour chaque face dans la liste "dice".

Enfin, la fonction calcule le score total en parcourant le dictionnaire "dices" et en appliquant les règles du jeu : elle ajoute au score total le nombre de points correspondant à chaque triple de dés (multiplié par le nombre de fois que ce triple apparaît dans la liste), et elle ajoute également les points pour chaque dé isolé qui a une valeur de 1 ou 5.

La fonction retourne le score total ainsi calculé.
