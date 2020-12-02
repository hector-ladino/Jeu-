import time
import pygame
from projectile import Projectile

# classe representant notre joueur
class player(pygame.sprite.Sprite):

    def __init__(self, jeu):
        super().__init__()
        self.jeu = jeu
        self.health = 100
        self.max_health = 100
        self.width = 160
        self.height = 233
        self.vit_x = 10
        self.vit_y = 10
        self.all_projectiles = pygame.sprite.Group()
        self.jumpHeight = 10
        self.jump = False
        self.image = pygame.transform.scale(pygame.image.load('Standing.png'), (233, 160))
        self.rect = self.image.get_rect()
        self.RunRight = [pygame.transform.scale(pygame.image.load('RR1.png'), (233, 160)),
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
        self.RunLeft = [pygame.transform.scale(pygame.image.load('RL1.png'), (233, 160)),
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
        self.rect.x = 100
        self.rect.y = 300

    def lancer_projectile(self):
        self.all_projectiles.add(Projectile(self))

    def damage(self, amount):
        if self.health - amount > amount:
            self.health -= amount
        else:
            self.jeu.game_over()


    def update_health_bar(self, surface):
       #barre de vie
       pygame.draw.rect(surface, (60, 63, 60), [self.rect.x + 45, self.rect.y -20, self.max_health, 10])
       pygame.draw.rect(surface, (111, 210, 46), [self.rect.x + 45, self. rect.y - 20, self.health, 10])


    def move_right(self):
        #joueur ne touche pas un monstre
        if not self.jeu.check_ifhit(self, self.jeu.les_monstres):
            self.rect.x += self.vit
            self.right = True
            self.left = False
    def move_left(self):
        self.rect.x -= self.vit
        self.right = False
        self.left = True


















    #def draw(self,fenetre):
        #if self.walkCount + 1 >= 33:
            #self.walkCount = 0

        #if self.left:
            #fenetre.blit(RunLeft[self.walkCount // 3], (self.rect.x, self.rect.y))
            #self.walkCount += 1
        #elif self.right:
            #fenetre.blit(RunRight[self.walkCount // 3], (self.rect.x, self.rect.y))
            #self.walkCount += 1
        #else:
            #fenetre.blit(self.image, self.rect)


