import pygame

class Projectile (pygame.sprite.Sprite):

    def __init__(self, player):
        super().__init__()
        self.vit = 20
        self.player = player
        self.image = pygame.transform.scale(pygame.image.load("snowball.png"), (46,40))
        self.rect = self.image.get_rect()
        self.rect.x = player.rect.x + 120
        self.rect.y = player.rect.y + 70
        self.image_origin = self.image
        self.angle = 0

    def rotation(self): #fait tourner la boule de neige pendant son lancement
        self.angle += 40
        self.image = pygame.transform.rotozoom(self.image_origin, self.angle, 1)
        self.rect = self.image.get_rect(center=self.rect.center)

    def remove(self):
        self.player.all_projectiles.remove(self) #supprimer les projectiles en cas de collision

    def move(self):
        self.rect.x += self.vit
        self.rotation()

        #projectile plus présent sur l'écran

        if self.rect.x > 1200:
            self.remove()

