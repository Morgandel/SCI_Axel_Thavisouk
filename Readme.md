#SCI : Simulation Centrée Individu
#Axel Thavisouk

##Diagramme UML






##Partie particules

###Questions

####Questions 1

On peut faire tourner sur un ordinateur ayant un processeur Intel® Core™ i5-7200U CPU @ 2.50GHz × 4 et 8 Go de RAM
120000 particules qui bougent à une fréquence d'environ 1 tour/seconde

####Question 2


####Question 3
Dans le cas où l'on ne fait rien lorsque une bille est présente, on supprime les particules où l'on veut aller. si l'on utilise une seuxiéme grille tampon pour stocker les particules qui se font supprimer on peut contourner le problème et dans ce cas il n'y a plus aucune collision.

Dans le cas où j'inverse la direction lors d'une collision, j'ai eu d'abord des problèmes où certaines particules supprimaient d'autres qui étaient dans l'environnement, mais en utilisant la même solution qu'en ne faisant rien on obtiens des mouvement assez étrange car les particules que l'on rencontre ne sont donc pas du tout affectées par les collisions qui n'ont pas été réalisée par eux.

Le cas où l'on échange les pas des deux particules qui collisionnent est le comportement qui donne le meilleur rendu car en effet les deux particules sont dans ce cas affectée par la collision et il n'y a plus besoin de tableau tampons car il n'est plus possible d'avoir deux particules différentes sur la même case.


###Partie Wator

####Question 1
Il est préférable d'initialiser les différents compteurs de manière aléatoire car lorsque l'on fixe ces compteurs aux même valeurs on obtiens des poissons et leurs enfants qui naissent et qui meurent en même temps. On peut le voir par la croissance en bloc sur la grille lorsque l'on le lance ainsi.

####Question 2
Lorsque l'on fixe une action par tick on bloque lorsque la grille est remplie de poissons car il ne peuvent plus se reproduire car les poissons se seront reproduits là où les requins étaient avant

Se reproduire en bougeant donne le meilleur résultat, ils donnent aux requins une meilleure survie et les poissons se reproduisent assez rapidement aussi, on voit sur la courbe d'evolution que les poissons ont l'air de se stabiliser un peu mieux sur la fin
![alt text](./images/evolution_bouge.png)
![alt text](./images/fish_shark_bouge.png)

Se reproduire en mangeant ne permet pas aux poissons de stabiliser leurs populations comme le faisait le comportement précédent
![alt text](./images/mange.png)
![alt text](./images/fish_shark_mange.png)
