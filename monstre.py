import pygame

#méchant monstre

class Monstre (pygame.sprite.Sprite):
    def __init__(self):
        super().__init__()
        self.health = 1
        self.max_health = 1
        self.attack = 10
        self.image = pygame.transform.scale(pygame.image.load("méchant.png"), (117, 193))
        self.rect = self.image.get_rect()
        self.rect.x = 1000
        self.rect.y = 250
        self.vit = 5

    def move(self):
        self.rect.x -= self.vit


