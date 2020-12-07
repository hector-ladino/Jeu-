from jeu import Jeu
import pygame
import math

pygame. init()

#arrière plan du jeu
fond = pygame.image.load('bg4.png')

#fenêtre du jeu
pygame.display.set_caption("notre jeu")
fenetre = pygame.display.set_mode((1200, 600))

#création d'un écran start
banner = pygame.transform.scale(pygame.image.load('noel.png'), (700,400))
banner_rect = banner.get_rect()
banner_rect.x = math.ceil(fenetre.get_width()/4.5)
banner_rect.y = math.ceil(fenetre.get_height()/6)

#bouton pour lancer partie
play_bouton = pygame.transform.scale(pygame.image.load('start.png'), (200, 60))
play_bouton_rect = play_bouton.get_rect()
play_bouton_rect.x = math.ceil(fenetre.get_width()/2.23)
play_bouton_rect.y = math.ceil(fenetre.get_height()/1.5)


#FPS
fps = pygame.time.Clock()
#movement fond
fond_x_pos = 0
def dupli_fond():
    fenetre.blit(fond, (fond_x_pos, 0))
    fenetre.blit(fond, (fond_x_pos+600, 0))


#instances
jeu = Jeu()

run = True
#main loop
while run:

    # fps
    fps.tick(30)
    #fond
    dupli_fond()

    #récupérer les projectiles du joueur
    for projectile in jeu.player.all_projectiles:
        projectile.move()

    #appliquer l'ensemble des images du groupe projectile
    jeu.player.all_projectiles.draw(fenetre)

    #game starting
    if jeu.is_playing:
        jeu.actualiser(fenetre)

    else: #si le jeu n'as pas commencé
        fenetre.blit(banner, banner_rect)
        fenetre.blit(play_bouton, play_bouton_rect)


    #mettre a jour l'écran
    pygame.display.flip()
    #fermer fenetre
    for event in pygame.event.get():
        #fermeture de fenetre
        if event.type == pygame.QUIT:
            run = False
            pygame.quit()
    #le joueur presse une touche
        elif event.type == pygame.KEYDOWN:
            jeu.pressed[event.key] = True

            #détecter la touche espace enclanchée
            if event.key == pygame.K_SPACE:
                jeu.player.lancer_projectile()

        elif event.type == pygame.KEYUP:
            jeu.pressed[event.key] = False

        elif event.type == pygame.MOUSEBUTTONDOWN:
            if play_bouton_rect.collidepoint(event.pos): #vérifier si la souris touche le bouton start
               jeu.start()



    #movement fond

    dupli_fond()




