import pygame
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