import pygame
pygame. init()


#Animation
RunRight = [pygame.transform.scale(pygame.image.load('RR1.png'), (233,160)), pygame.transform.scale(pygame.image.load('RR2.png'), (233,160)), pygame.transform.scale(pygame.image.load('RR3.png'), (233,160)), pygame.transform.scale(pygame.image.load('RR4.png'), (233,160)), pygame.transform.scale(pygame.image.load('RR5.png'), (233,160)), pygame.transform.scale(pygame.image.load('RR6.png'), (233,160)), pygame.transform.scale(pygame.image.load('RR7.png'), (233,160)), pygame.transform.scale(pygame.image.load('RR8.png'), (233,160)), pygame.transform.scale(pygame.image.load('RR9.png'), (233,160)),pygame.transform.scale(pygame.image.load('RR10.png'), (233,160)),pygame.transform.scale(pygame.image.load('RR11.png'), (233,160))]
RunLeft = [pygame.transform.scale(pygame.image.load('RL1.png'), (233,160)), pygame.transform.scale(pygame.image.load('RL2.png'), (233,160)), pygame.transform.scale(pygame.image.load('RL3.png'), (233,160)), pygame.transform.scale(pygame.image.load('RL4.png'), (233,160)), pygame.transform.scale(pygame.image.load('RL5.png'), (233,160)), pygame.transform.scale(pygame.image.load('RL6.png'), (233,160)), pygame.transform.scale(pygame.image.load('RL7.png'), (233,160)), pygame.transform.scale(pygame.image.load('RL8.png'), (233,160)), pygame.transform.scale(pygame.image.load('RL9.png'), (233,160)),pygame.transform.scale(pygame.image.load('RL10.png'), (233,160)),pygame.transform.scale(pygame.image.load('RL11.png'), (233,160))]

#Animation info
left = False
right = False
walkCount = 0

#jump info
isJump = False
jumpCount = 13

#arrière plan du jeu
fond = pygame.image.load('bg4.png')

#imagejoueur
joueur = pygame.transform.scale(pygame.image.load('Standing.png'), (233,160))

#joueur informations
x = 100
y = 300
width = 160
height = 233
vit = 10
#fenêtre du jeu
pygame.display.set_caption("notre jeu")
fenetre = pygame.display.set_mode((1200, 600))


#FPS
fps = pygame.time.Clock()
#movement fond
fond_x_pos = 0
def dupli_fond():
    fenetre.blit(fond, (fond_x_pos,0))
    fenetre.blit(fond,(fond_x_pos+600,0))


#Animation du personnage
def redrawGameWindow():
    global walkCount

    if walkCount + 1 >=33:
        walkCount = 0

    if left:
        fenetre.blit(RunLeft[walkCount//3], (x,y))
        walkCount += 1
    elif right:
        fenetre.blit(RunRight[walkCount//3], (x,y))
        walkCount += 1
    else:
        fenetre.blit(joueur, (x,y))

    pygame.display.update()


class boule de neige(object):
    boule = pygame.image.load(snowbal)



class boule de neige(object):
    boule = pygame.image.load(snowba)


run = True

#main loop
while run:

    #fermer fenetre
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            run= False
            pygame.quit()

    #fps
    fps.tick(33)

    #mouvement joueur
    keys = pygame.key.get_pressed()

    if keys[pygame.K_LEFT] and x > vit:
        x-= vit
        left = True
        right = False
    elif keys[pygame.K_RIGHT] and x < 1200 - width - vit:
        x+= vit
        left = False
        right = True
    else:
        right = False
        left = False
        walkCount = 0

    #saut

    if not (isJump):
        if keys[pygame.K_UP]:
            isJump = True
            right = False
            left = False
            walkCount = 0
    else:
         if jumpCount >= -13:
            neg = 1
            if jumpCount < 0:
                neg = -1
            y -= (jumpCount ** 2 ) * 0.2 * neg
            jumpCount -= 1
         else:
            isJump = False
            jumpCount = 13


    #Animation
    redrawGameWindow()


    #movement fond

    dupli_fond()




