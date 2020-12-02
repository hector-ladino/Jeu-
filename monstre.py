import pygame
import random


#méchant monstre

class Monstre (pygame.sprite.Sprite):
    def __init__(self, jeu):
        super().__init__()
        self.jeu = jeu
        self.health = 1
        self.attack = 30
        self.image = pygame.transform.scale(pygame.image.load("méchant.png"), (58, 96))
        self.rect = self.image.get_rect()
        self.rect.x = 1000 + random.randint(0,200)
        self.rect.y = 350
        self.vit = random.randint(1,10)

    def degats(self, amount):
        #infliger des degats
        self.health -= amount
        #voir si le nb de points de vie et plus petit ou égal à 0
        if self.health <= 0:
            self.rect.x = 1200 + random.randint(0,400)


    def remove(self):
        self.jeu.les_monstres.remove(self)

    def move(self):
        # le dépacement se fait uniquement lorsque le monstre ne touche pas le joueur
        self.rect.x -= self.vit

        if self.jeu.check_ifhit(self, self.jeu.les_joueurs):
            self.rect.x = 1000 + random.randint(300, 500)
            self.vit = random.randint(1, 10)
            self.jeu.player.damage(self.attack)




