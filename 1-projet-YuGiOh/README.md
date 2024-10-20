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
...