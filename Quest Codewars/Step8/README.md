"solution" prend un entier n en entrée et qui renvoie sa représentation en chiffres romains sous forme de chaîne de caractères.

La fonction commence par initialiser une chaîne de caractères vide appelée roman_num. Ensuite, un dictionnaire appelé roman_let est défini avec des paires clé-valeur représentant les symboles romains et leur équivalent décimal.

Ensuite, une boucle est utilisée pour parcourir chaque clé du dictionnaire roman_let. À chaque itération de la boucle, la valeur de la clé courante est utilisée pour déterminer combien de fois cette valeur doit être soustraite de n pour obtenir sa représentation en chiffres romains. Si la valeur de la clé courante est inférieure ou égale à n, elle est ajoutée à la chaîne de caractères roman_num, et n est mis à jour en soustrayant la valeur de la clé courante. Le processus se répète jusqu'à ce que n soit égal à zéro.

Finalement, la fonction renvoie la chaîne de caractères roman_num contenant la représentation en chiffres romains de l'entier n fourni en entrée.
