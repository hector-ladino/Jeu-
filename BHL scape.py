from jeu import Jeu
import pygame
pygame. init()

#arrière plan du jeu
fond = pygame.image.load('bg4.png')

#fenêtre du jeu
pygame.display.set_caption("notre jeu")
fenetre_width = 1200
fenetre_height = 600
fenetre = pygame.display.set_mode((fenetre_width, fenetre_height))


#FPS
fps = pygame.time.Clock()
#movement fond
fond_x_pos = 0
def dupli_fond():
    fenetre.blit(fond, (fond_x_pos,0))
    fenetre.blit(fond,(fond_x_pos+600,0))



#méchante boule de neige
class bouledeneige(object):
    boule = pygame.transform.scale(pygame.image.load("snowball.png"), (100,100))

    def __init__(self, x, y, width, height, end):
        self.x = 100
        self.y = 300
        self.width = 160
        self.height = 233
        self.end = end
        self.path = [self.x, self.end]
        self.walkCount = 0
        self.vit = 3

    def draw(self, fenetre):
        self.move()
        if self.walkCount + 1 <= 33:
            self.walCount = 0

        if self.vit > 0:
            fenetre.blit(self.boule, (self.x, self.y))
            self.walkCount += 1
        else:
            fenetre.blit(self.boule, (self.x, self.y))
            self.walkCount += 1

    def move(self):
        if self.vit > 0:
            if self.x + self.vit < self.path[1]:
                self.x += self.vit
            else:
                self.vit = self.vit * -1
                self.walkCount = 0
        else:
            if self.x - self.vit > self.path[0]:
                self.x += self.vit
            else:
                self.vit = self.vit * -1
                self.walkCount = 0



#Animation du personnage
def redrawGameWindow():
    b2neige.draw(fenetre)
    pygame.display.update()

#instances
jeu = Jeu()
b2neige = bouledeneige(1, 300, 100, 100, 1200)



run = True

#main loop
while run:
    # fps
    fps.tick(33)
    fenetre.blit(jeu.player.image, jeu.player.rect)


    for monstre in jeu.les_monstres:
        monstre.move()

    #apparition des monstres
    jeu.les_monstres.draw(fenetre)


    # commandes pour diriger le personnage
    if jeu.pressed.get(pygame.K_RIGHT) and jeu.player.rect.x + jeu.player.rect.width < fenetre_width:
        jeu.player.move_right()
    elif jeu.pressed.get(pygame.K_LEFT) and jeu.player.rect.x > 0:
        jeu.player.move_left()

    #mettre a jour l'écran
    pygame.display.flip()
    #fermer fenetre
    for event in pygame.event.get():
        #fermeture de fenetre
        if event.type == pygame.QUIT:
            run= False
            pygame.quit()
    # le joueur presse une touche
        elif event.type == pygame.KEYDOWN:
            jeu.pressed[event.key] = True
        elif event.type == pygame.KEYUP:
            jeu.pressed[event.key] = False



    #saut

    #if not (pnoel.isJump):
        #if keys[pygame.K_UP]:
            #pnoel.isJump = True
            #pnoel.right = False
            #pnoel.left = False
            #pnoel.walkCount = 0
    #else:
         #if pnoel.jumpCount >= -13:
            #neg = 1
            #if pnoel.jumpCount < 0:
                #neg = -1
            #pnoel.rect.y -= (pnoel.jumpCount ** 2) * 0.2 * neg
            #pnoel.jumpCount -= 1
         #else:
            #pnoel.isJump = False
            #pnoel.jumpCount = 13


    #Animation
    redrawGameWindow()


    #movement fond

    dupli_fond()




