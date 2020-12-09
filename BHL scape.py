
import pygame
import math
import random


pygame. init()

#arrière plan du jeu
fond = pygame.image.load('bg4.png')

#fenêtre du jeu
pygame.display.set_caption("C'est bientot Noel")
fenetre = pygame.display.set_mode((1200, 600))


#couleurs
black = (0, 0, 0)
white = (255, 255, 255)


#création d'un écran start
banner = pygame.transform.scale(pygame.image.load('noel.png'), (850,320))
banner_rect = banner.get_rect()
banner_rect.x = math.ceil(fenetre.get_width()/8)
banner_rect.y = math.ceil(fenetre.get_height()/1000)

#bouton pour lancer partie
play_bouton = pygame.transform.scale(pygame.image.load('start.png'), (200, 60))
play_bouton_rect = play_bouton.get_rect()
play_bouton_rect.x = math.ceil(fenetre.get_width()/2.45)
play_bouton_rect.y = math.ceil(fenetre.get_height()/1.2)

#ecran "how to play"
ecran_htp = pygame.transform.scale(pygame.image.load("écran_how_to_play.png"), (340, 230))
ecran_htp_rect = ecran_htp.get_rect()
ecran_htp_rect.x = math.ceil(fenetre.get_width()/2.8)
ecran_htp_rect.y = math.ceil(fenetre.get_height()/2.6)


#FPS
fps = pygame.time.Clock()

#movement fond
#sol qui bouge
floor_surface = pygame.transform.scale(pygame.image.load('ground.PNG'), (1200,160))

floor_x_pos = 0
fond_x_pos = 0

def mouv_sol() :
    fenetre.blit(floor_surface, (floor_x_pos, 441))
    fenetre.blit(floor_surface, (floor_x_pos +600, 441))
    fenetre.blit(floor_surface, (floor_x_pos + 1200, 441))


def dupli_fond():
    fenetre.blit(fond, (fond_x_pos,0))
    fenetre.blit(fond,(fond_x_pos+600,0))

#score
score_value = 0
font = pygame.font.Font('freesansbold.ttf', 32)
text_x = 10
text_y = 10


 #class qui représente le jeu
class Jeu:
    def __init__(self):
        #jeu start ou non
        self.is_playing = False
        #joueur
        self.les_joueurs = pygame.sprite.Group()
        self.player = player(self)
        self.les_joueurs.add(self.player)
        #plusieurs méchants
        self.les_monstres = pygame.sprite.Group()
        self.pressed = {}

    def start(self):
        self.is_playing = True
        self.spawn_monster()
        self.spawn_monster()
        self.spawn_monster()
        self.spawn_monster()
        self.spawn_monster()
        self.spawn_monster()
        self.spawn_monster()
        self.spawn_monster()
        self.spawn_monster()


    def game_over(self):
        #reinitialisation du jeu
        self.les_monstres = pygame.sprite.Group()
        self.player.health = self.player.max_health
        self.is_playing = False

    def actualiser(self, fenetre):
        fenetre.blit(self.player.image, self.player.rect)

        # actualiser la barre de vie du joueur
        self.player.update_health_bar(fenetre)

        for monstre in self.les_monstres:
            monstre.move()

        # apparition des monstres
        self.les_monstres.draw(fenetre)

        # commande joueur

        if self.pressed.get(pygame.K_LEFT) and self.player.rect.x > self.player.vit_x:
            self.player.rect.x -= self.player.vit_x

        if self.pressed.get(pygame.K_RIGHT) and self.player.rect.x < 1200 - self.player.width - self.player.vit_x:
            self.player.rect.x += self.player.vit_x

        if self.player.jump is False and self.pressed.get(pygame.K_UP):
            self.player.jump = True

        if self.player.jump is True:
            self.player.rect.y -= self.player.vit_y*4 #augmenter ou diminuer la hauteur du saut
            self.player.vit_y -= 1
            if self.player.vit_y < -10:
                self.player.jump = False
                self.player.vit_y = 10


    def check_ifhit(self, sprite, group):
        return pygame.sprite.spritecollide(sprite, group, False, pygame.sprite.collide_mask)


    def spawn_monster(self):
        monstre = Monstre(self)
        self.les_monstres.add(monstre)

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
        self.attack = 1
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
            self.jeu.game_over() #si plus de vie


    def update_health_bar(self, surface):
       #barre de vie
       pygame.draw.rect(surface, (60, 63, 60), [self.rect.x + 45, self.rect.y -20, self.max_health, 10])
       pygame.draw.rect(surface, (111, 210, 46), [self.rect.x + 45, self. rect.y - 20, self.health, 10])


    def move_right(self):
        #joueur ne touche pas un monstre
        if not self.jeu.check_ifhit(self, self.jeu.les_monstres):
            self.rect.x += self.vit_x
            self.right = True
            self.left = False
    def move_left(self):
        self.rect.x -= self.vit_x
        self.right = False
        self.left = True



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

        #voir si le projectile touche un monstre
        for monster in self.player.jeu.check_ifhit(self, self.player.jeu.les_monstres):
            #si c'est vrai alors on supprime le projectile
            self.remove()
            #infliger degats
            monster.degats(self.player.attack)

        #projectile plus présent sur l'écran

        if self.rect.x > 1200:
            self.remove()









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
        # movement fond
        floor_x_pos -= 1
        mouv_sol()
        if floor_x_pos <= -600:
            floor_x_pos = 0

        jeu.actualiser(fenetre)

    else:
        fenetre.fill(white)
        fenetre.blit(banner, banner_rect)
        fenetre.blit(play_bouton, play_bouton_rect)
        fenetre.blit(ecran_htp, ecran_htp_rect)



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

            if event.key == pygame.K_SPACE:
                jeu.player.lancer_projectile()

        elif event.type == pygame.KEYUP:
            jeu.pressed[event.key] = False

        elif event.type == pygame.MOUSEBUTTONDOWN:
            if play_bouton_rect.collidepoint(event.pos):  # vérifier si la souris touche le bouton start
                jeu.start()


