# Projet YuGiOh

## 1. Installation de PyGame

PyGame est une librairie, ou un *package* en anglais, qui peut être utilisée dans un fichier Python avec une des lignes suivantes : 
```python
# importer toute la librairie :
import pygame
exemple = pygame.function1

# importer toute la librairie et lui donner un surnom plus court :
import pygame as p
exemple = p.function1

# importer un nombre fini d'éléments de la librairie :
from pygame import function1, function2 
exemple = function1

# importer toutes les éléments de pygame : peut créer des conflits, peu recommandé :
from pygame import *
exemple = function1
```

Pour gérer les librairies Python installées sur ton ordinateur, on utilise des outils comme **pip** ou **conda**.
Par défaut et par souci de simplicité, c'est *pip* que l'on va utiliser.

*pip* c'est l'installateur de base, qui est installé en même temps que Python. Tu peux voir la [documentation officielle ici](https://pypi.org/project/pip/). Pour l'utiliser, il faut se trouver dans une invite de commande, aussi appelée *shell* ou terminal.
Pour ouvrir une invite de commande, tu peux : 
- taper invite de commande dans la barre de recherche Windows ou
- aller dans Thonny > Tools > Open system shell...

Utilise la deuxième option tant que tu utilises le Python de Thonny.

Ensuite tu appelles *pip* ainsi : 
```bash
# Pour voir à quel application Python pip est rattaché :
pip --version
# ou
pip -V

# Pour voir dans le terminal la documentation de pip : 
pip --help

# Pour voir les librairies déjà installées :
pip list

# Pour installer une nouvelle librairie : 
pip install <nom-de-la-librairie>
# Note que des fois le nom pour installer la librairie est plus compliqué 
```

**Pour résumer, pour installer PyGame dans Thonny il faut simplement :**
1. Ouvrir Thonny > Tools > Open system shell...
2. Taper ```pip install pygame```

## 2. Premiers pas avec PyGame

### Liens utiles
Quand tu utilises une librairie python, l'idéal c'est d'avoir sous la main sa documentation, que tu consultes dès que tu as besoin de détails sur une fonction, et des exemples de codes, pour apprendre comment l'utiliser.
- Documentation : https://www.pygame.org/docs/
- Tutoriels : https://www.pygame.org/wiki/tutorials

### Ouvrir une fenêtre Pygame et afficher une image 
Je te fais une petite recette de cuisine, essaye de la suivre pour obtenir à la fin une fenêtre avec une image en fonc d'écran ! Si jamais tu as des questions, essaye de trouver la réponse dans la documentation, et sinon envoie moi un message.

1. Crée un nouveau fichier Python, et importe Pygame dedans.
2. Pygame a besoin d'être initialisé une première fois pour être utilisé, avec la fonction ```init()```.
3. Choisis une image de ton choix, note ses dimensions en pixels, et met une copie de l'image dans le même dossier que ton fichier Python.
4. Pour charger une image, utilises la fonction ```image.load()```.
5. Tu dois maintenant créer une fenêtre. Une fenêtre est un type d'objet de Pygame. Pour créer ton objet fenêtre, utilise la fonction ```display.set_mode()```, et donne lui les dimensions de ton image.
6. Pour afficher l'image dans ta fenêtre, utilises la *méthode* ```blit()```. Cette méthode prend en argument ton image et sa position dans la fenêtre. 
7. Il faut ensuite mettre à jour la fenêtre, avec la fonction de PyGame ```display.update()```.
8. C'est bon ta fenêtre s'affiche ! Mais pendant une fraction de seconde. Crée une boucle infinie pour que ta fenêtre ne se ferme jamais.
9. Envoie moi une capture d'écran du résultat !


### Le concept d'événement
Les événements rassemblent toutes les actions de l'utilisateur, qui peuvent être :
- cliquer sur une touche du clavier
- cliquer sur un des boutons de la souris
- déplacer la souris
- cliquer sur un élément de la fenêtre Pygame

Ces exemples sont tous prédéfinis dans la librairie, mais il est aussi possible de créer de nouveaux types d'événements.

Dès qu'un événement se produit, il est ajouté à la fin d'une liste appelée **la queue**.
Cette liste a une taille maximale au-delà de laquelle les événements les plus anciens en sont effacés.

Pour parcourir cette queue et accéder aux derniers événements, on peut, par exemple, appeler la fonction ```event.get()```.

> Documentation relative aux événements : https://www.pygame.org/docs/ref/event.html
> La liste complète des événements prédéfinis s'y trouve.

### Fermer Pygame
"Fermer Pygame" en traduction de programmation c'est prendre un événement (exemple cliquer sur le bouton X en haut à droite de la fenêtre) et lui associer l'action ```quit()``` et la fin de notre programme.

Il faut donc parcourir les événements, pour chacun vérifier s'il correspond à l'événement prédéfini ```pygame.QUIT```.
Si c'est le cas, il faut sortir appeler la fonction ```quit()``` et quitter la boucle infinie (dans n'importe quel ordre).

## 3. Schémas récapitulatifs
...