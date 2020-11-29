from jeu import Jeu
import pygame, sys
from pygame.locals import *

pygame. init()

#arrière plan du jeu
fond = pygame.image.load('bg4.png')

#fenêtre du jeu
pygame.display.set_caption("notre jeu")
fenetre = pygame.display.set_mode((1200, 600))

#création d'un écran start
banner = pygame.transform.scale(pygame.image.load('snowball.png'), (300,200))
banner_rect = banner.get_rect()
banner_rect.x = fenetre.get_width()/2.5
banner_rect.y = fenetre.get_height()/4


#FPS
fps = pygame.time.Clock()
#movement fond
fond_x_pos = 0
def dupli_fond():
    fenetre.blit(fond, (fond_x_pos,0))
    fenetre.blit(fond,(fond_x_pos+600,0))


#instances
jeu = Jeu()

run = True

#main loop
while run:
    # fps
    fps.tick(60)
    #fond
    dupli_fond()

    #gamestarting
    if jeu.is_playing:
        jeu.actualiser(fenetre)

    else:
        fenetre.blit(banner, banner_rect)


    #mettre a jour l'écran
    pygame.display.flip()
    #fermer fenetre
    for event in pygame.event.get():
        #fermeture de fenetre
        if event.type == pygame.QUIT:
            run = False
            pygame.quit()
    # le joueur presse une touche
        elif event.type == pygame.KEYDOWN:
            jeu.pressed[event.key] = True

        elif event.type == pygame.KEYUP:
            jeu.pressed[event.key] = False




    #movement fond

    dupli_fond()




