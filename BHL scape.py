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
#sol qui bouge
floor_surface = pygame.transform.scale(pygame.image.load('ground.PNG'), (1200,160))


floor_x_pos = 0

fond_x_pos = 0

def mouv_sol() :
    fenetre.blit(floor_surface, (floor_x_pos, 443))
    fenetre.blit(floor_surface, (floor_x_pos +600, 443))
    fenetre.blit(floor_surface, (floor_x_pos + 1200, 443))


def dupli_fond():
    fenetre.blit(fond, (fond_x_pos,0))
    fenetre.blit(fond,(fond_x_pos+600,0))


#bloc de glace
bloc_surface = pygame.transform.scale(pygame.image.load('brique.png'), (200,400))
bloc_list = []
SPAWNBLOC = pygame.USEREVENT
pygame.time.set_timer(SPAWNBLOC,4000)

def create_bloc():
    new_bloc = bloc_surface.get_rect(midtop = (1250,200))
    return new_bloc

def move_bloc(blocs):
    for bloc in blocs :
        bloc.centerx -= 5
    return blocs
def draw_bloc(blocs):
    for bloc in blocs:
       fenetre.blit(bloc_surface,bloc)

#instances
jeu = Jeu()

run = True

#main loop
while run:
    # fps
    fps.tick(30)

    #fond
    dupli_fond()

    bloc_list = move_bloc(bloc_list)


    #récupérer les projectiles du joueur
    for projectile in jeu.player.all_projectiles:
        projectile.move()

    #appliquer l'ensemble des images du groupe projectile
    jeu.player.all_projectiles.draw(fenetre)

    #gamestarting
    if jeu.is_playing:
        draw_bloc(bloc_list)
        jeu.actualiser(fenetre)





    else:
        fenetre.blit(banner, banner_rect)


    #mettre a jour l'écran
    pygame.display.flip()
    #fermer fenetre
    for event in pygame.event.get():
        # bloc
        if event.type == SPAWNBLOC:
            bloc_list.append(create_bloc())


        #fermeture de fenetre
        if event.type == pygame.QUIT:
            run = False
            pygame.quit()
    # le joueur presse une touche
        elif event.type == pygame.KEYDOWN:
            jeu.pressed[event.key] = True

            #détecter la touche espace enclanchée
            if event.key == pygame.K_SPACE:
                jeu.player.lancer_projectile()



        elif event.type == pygame.KEYUP:
            jeu.pressed[event.key] = False

        elif event.type == pygame.MOUSEBUTTONDOWN:
            if banner_rect.collidepoint(event.pos):
                #lancer le jeu
               jeu.start()

     # movement fond
            floor_x_pos -= 1
            mouv_sol()
            if floor_x_pos <= -600:
                floor_x_pos = 0





