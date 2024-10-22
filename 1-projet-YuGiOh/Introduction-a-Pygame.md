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

### Ouvrir une fenêtre Pygame 
Je te fais une petite recette de cuisine, essaye de la suivre pour obtenir à la fin une fenêtre avec une image en fonc d'écran ! Si jamais tu as des questions, essaye de trouver la réponse dans la documentation, et sinon envoie moi un message.

1. Crée un nouveau fichier Python, et importe Pygame dedans.
2. Pygame a besoin d'être initialisé une première fois pour être utilisé, avec la fonction ```init()```.
3. Choisis une image de ton choix, note ses dimensions en pixels, et met une copie de l'image dans le même dossier que ton fichier Python.
4. Pour charger une image, utilises la fonction ```image.load()```.
5. Tu dois maintenant créer une fenêtre. Une fenêtre est un type d'objet de Pygame. Pour créer ton objet fenêtre, utilise la fonction ```display.set_mode()```, et donne lui les dimensions de ton image.
6. Pour afficher ta fenêtre, utilises la *méthode* ```blit()```. Cette méthode prend en argument ton image et sa position dans la fenêtre. 
7. C'est bon ta fenêtre s'affiche ! Mais pendant une fraction de seconde. Crée une boucle infinie pour que ta fenêtre ne se ferme jamais.
8. Envoie moi une capture d'écran du résultat !