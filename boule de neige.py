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

                # bloc de glace
                bloc_surface = pygame.transform.scale(pygame.image.load('brique.png'), (200, 400))
                bloc_list = []
                SPAWNBLOC = pygame.USEREVENT
                pygame.time.set_timer(SPAWNBLOC, 4000)


                def move_bloc(blocs):
                    for bloc in blocs:
                        bloc.centerx -= 5
                    return blocs

                def draw_bloc(blocs):
                    for bloc in blocs:
                        fenetre.blit(bloc_surface, bloc)
                        bloc_list = move_bloc(bloc_list)
                        draw_bloc(bloc_list)
                        if event.type == SPAWNBLOC:
                            bloc_list.append(create_bloc())