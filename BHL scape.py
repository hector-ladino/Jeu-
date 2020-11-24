import pygame
pygame. init()

#playerImages
joueur = pygame.transform.scale(pygame.image.load('Standing.png'), (233, 160))

RunRight = [pygame.transform.scale(pygame.image.load('RR1.png'), (233, 160)),
            pygame.transform.scale(pygame.image.load('RR2.png'), (233, 160)),
            pygame.transform.scale(pygame.image.load('RR3.png'), (233, 160)),
            pygame.transform.scale(pygame.image.load('RR4.png'), (233, 160)),
            pygame.transform.scale(pygame.image.load('RR5.png'), (233, 160)),
            pygame.transform.scale(pygame.image.load('RR6.png'), (233, 160)),
            pygame.transform.scale(pygame.image.load('RR7.png'), (233, 160)),
            pygame.transform.scale(pygame.image.load('RR8.png'), (233, 160)),
            pygame.transform.scale(pygame.image.load('RR9.png'), (233, 160)),
            pygame.transform.scale(pygame.image.load('RR10.png'), (233, 160)),
            pygame.transform.scale(pygame.image.load('RR11.png'), (233, 160))]
RunLeft = [pygame.transform.scale(pygame.image.load('RL1.png'), (233, 160)),
           pygame.transform.scale(pygame.image.load('RL2.png'), (233, 160)),
           pygame.transform.scale(pygame.image.load('RL3.png'), (233, 160)),
           pygame.transform.scale(pygame.image.load('RL4.png'), (233, 160)),
           pygame.transform.scale(pygame.image.load('RL5.png'), (233, 160)),
           pygame.transform.scale(pygame.image.load('RL6.png'), (233, 160)),
           pygame.transform.scale(pygame.image.load('RL7.png'), (233, 160)),
           pygame.transform.scale(pygame.image.load('RL8.png'), (233, 160)),
           pygame.transform.scale(pygame.image.load('RL9.png'), (233, 160)),
           pygame.transform.scale(pygame.image.load('RL10.png'), (233, 160)),
           pygame.transform.scale(pygame.image.load('RL11.png'), (233, 160))]






#arrière plan du jeu
fond = pygame.image.load('bg4.png')

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




class player(object):

    def __init__(self, x, y, width, height):
        self.x = 100
        self.y = 300
        self.width = 160
        self.height = 233
        self.vit = 10
        self.left = False
        self.right = False
        self.walkCount = 0
        self.isJump = False
        self.jumpCount = 13

    def draw(self,fenetre):
        if self.walkCount + 1 >= 33:
            self.walkCount = 0

        if self.left:
            fenetre.blit(RunLeft[self.walkCount // 3], (self.x, self.y))
            self.walkCount += 1
        elif self.right:
            fenetre.blit(RunRight[self.walkCount // 3], (self.x, self.y))
            self.walkCount += 1
        else:
            fenetre.blit(joueur, (self.x, self.y))

#méchante boule de neige
class bouledeneige(object):
    boule = pygame.transform.scale(pygame.image.load("snowball.png"), (100,100))

    def __init__(self, x, y, width, height, end):
        self.x = x
        self.y = y
        self.width = width
        self.height = height
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
    pnoel.draw(fenetre)
    b2neige.draw(fenetre)
    pygame.display.update()

#instances
pnoel = player(100, 300, 160, 233)
b2neige = bouledeneige(1, 300, 100, 100, 1200)



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

    if keys[pygame.K_LEFT] and pnoel.x > pnoel.vit:
        pnoel.x-= pnoel.vit
        pnoel.left = True
        pnoel.right = False
    elif keys[pygame.K_RIGHT] and pnoel.x < 1200 - pnoel.width - pnoel.vit:
        pnoel.x += pnoel.vit
        pnoel.left = False
        pnoel.right = True
    else:
        pnoel.right = False
        pnoel.left = False
        pnoel.walkCount = 0

    #saut

    if not (pnoel.isJump):
        if keys[pygame.K_UP]:
            pnoel.isJump = True
            pnoel.right = False
            pnoel.left = False
            pnoel.walkCount = 0
    else:
         if pnoel.jumpCount >= -13:
            neg = 1
            if pnoel.jumpCount < 0:
                neg = -1
            pnoel.y -= (pnoel.jumpCount ** 2 ) * 0.2 * neg
            pnoel.jumpCount -= 1
         else:
            pnoel.isJump = False
            pnoel.jumpCount = 13


    #Animation
    redrawGameWindow()


    #movement fond

    dupli_fond()




