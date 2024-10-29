import pygame


# Démarrage de Pygame
pygame.init()

# Chargement d'une image
img = pygame.image.load("hxppy_thxughts.png")

# Création d'un objet d'affichage
fenetre = pygame.display.set_mode((456, 386), pygame.SCALED | pygame.RESIZABLE)

# Chargement d'une police
police = pygame.font.SysFont("Arial Black", 18, italic=True)

# Boucle infinie
run = True
while run:

    # Affichage de l'image dans la fenêtre
    fenetre.blit(img, (0, 0))
    fenetre.blit(police.render("coucou", False, (200, 50, 50), (0, 0, 0)), (5, 5))
    
    # Mise à jour de la fenêtre
    pygame.display.update()

    # Gestion des événements
    for event in pygame.event.get():
        
        # Si l'événement correspond à cliquer sur la croix
        if event.type == pygame.QUIT:

            # Fin de la boucle infinie
            run = False

# Quitter Pygame
pygame.quit()
