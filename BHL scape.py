import pygame
pygame. init()

#arrière plan du jeu
fond = pygame.image.load('bg4.png')

#imagejoueur
joueur = pygame.transform.scale(pygame.image.load('Standing.png'), (233,160))
#joueur informations

x = 100
y = 500
width = 64
height = 64
vit = 10
#fenêtre du jeu
pygame.display.set_caption("notre jeu")
fenetre = pygame.display.set_mode((1200, 600))

#movement fond
fond_x_pos = 0
def mov_fond():
    fenetre.blit(fond, (fond_x_pos,0))
    fenetre.blit(fond,(fond_x_pos+600,0))
    fenetre.blit(fond,(fond_x_pos+1200,0))


run = True

#main loop
while run:

    #fermer fenetre
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            run= False
            pygame.quit()



    #mouvement joueur
    keys = pygame.key.get_pressed()

    if keys[pygame.K_LEFT]:
        x-= vit
    elif keys[pygame.K_RIGHT]:
        x+= vit




    # arrière plan du jeu
    fenetre.blit(fond, (0, 0))

    #movement fond
    fond_x_pos -= 1
    mov_fond()
    if fond_x_pos <= -600:
        fond_x_pos = 0


    #joueur
    fenetre.blit(joueur, (100, 320))
    # mise à jour de l'écran
    pygame.display.flip()
