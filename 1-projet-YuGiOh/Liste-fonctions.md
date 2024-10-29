# Travail prémâché
Liste de fonctions de Pygame utiles.

## Afficher du texte

### 1. Charger une police
Exemple : 
```python
import pygame

# Pour importer des polices déjà existantes sur ton ordi, exemple Arial, Times New Roman etc.
police = pygame.font.SysFont('nom-de-la-police', taille, bold=False, italic=False)

# Pour importer une police que tu as téléchargé (va voir le site dafont.com)
police = pygame.font.Font("chemin\\vers\\le\\fichier\\nom-fichier-police.TTF", taille, bold=False, italic=False)
# Question : sais-tu pourquoi il faut mettre 2 "\" dans les chaînes de caractères ?
```

### 2. Créer l'objet avec ton texte 
```python
# fonction render utilisée : 
render(text, antialias, color, background=None)
# exemple :
police.render("salut ça va", True, (200, 25, 25), background=(0,0,0))
```
On utilise la police que l'on a chargé, le 2è argument correspond à l'antialiasing, je te laisse essayer avec *True* ou *False*, et le 3è argument c'est la couleur en RGB.
 > Pour la couleur en RGB, tu peux utilisere Gimp où il devrait y avoir quelque part une roue des couleurs pour choisir et les valeurs RGB correspondantes


### 3. Affichage
Avec la fonction ```blit```, par exemple :
```python
screen.blit(police.render("Fin du jeu !", True, (200, 25, 25)), (600, 200))
```

## Changer la transparence d'une image
Une nouvelle fonction rend l'opération très simple : 

```python
# Valeur en 0 (transparent) et 255 (opaque)
Surface.set_aplha(value)

# Désactiver la transparence (= mettre 255)
Surface.set_alpha(None)
```

> Attention : pas sûre de la réaction avec une image dans un autre format que PNG.

## Autres fonctions
### display.set_mode(pos, flags)
Valeurs possibles pour flags : 
- FULLSCREEN
- SCALED
- RESIZABLE
Recommendation : SCALED | RESIZABLE


### transform.scale
pour changer la taille de l'image dans pygame plutôt que à la main au préalable
existe 


## To-Do
- clic bouton = changer transparence image...

- comment afficher rectangles barres de vie
