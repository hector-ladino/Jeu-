
import pygame
import math
import random


pygame. init()

#arrière plan du jeu
fond = pygame.image.load('bg4.png')

#fenêtre du jeu
pygame.display.set_caption("C'est bientôt Noël !")
fenetre = pygame.display.set_mode((1200, 600))

#couleurs
black = (0, 0, 0)
white = (255, 255, 255)

#sound
gameoversound = pygame.mixer.Sound("gameover.mp3")

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

#ecran game over
embleme = pygame.image.load('game over.png')
embleme_rect = embleme.get_rect()
embleme_rect.x = math.ceil(fenetre.get_width()/4)
embleme_rect.y = math.ceil(fenetre.get_height()/7)

#bouton pour relancer la partie
tryagain_bouton = pygame.transform.scale(pygame.image.load('try again.png'), (200, 60))
tryagain_bouton_rect = play_bouton.get_rect()
tryagain_bouton_rect.x = math.ceil(fenetre.get_width()/2.45)
tryagain_bouton_rect.y = math.ceil(fenetre.get_height()/1.2)

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
font_name =pygame.font.match_font("04B_19.ttf",40)
def draw_text(surface,text,size,x,y):
    font = pygame.font.Font(font_name,size)
    text_surface = font.render(text,True, (0,0,0))
    text_rect = text_surface.get_rect()
    text_rect.midtop = (x,y)
    fenetre.blit(text_surface, text_rect)

 #class qui représente le jeu
class Jeu:
    def __init__(self):
        #jeu start ou non
        self.is_playing = False
        #fin du jeu
        self.gameover = False
        #joueur
        self.les_joueurs = pygame.sprite.Group()
        self.player = player(self)
        self.les_joueurs.add(self.player)
        #plusieurs méchants
        self.les_monstres = pygame.sprite.Group()
        #plusieurs super méchants
        self.les_supermonstres = pygame.sprite.Group()
        #barre d'évenements
        self.bloc_event = blocEvent(self)
        self.pressed = {}
        self.score = 0
        self.topscore = 0
        self.yourscore = 0

    def start(self):
        self.is_playing = True
        self.gameover = False
        self.spawn_monster()
        self.spawn_supermonster()
        if jeu.score > 500:
            self.spawn_monster()
            self.spawn_monster()
        if jeu.score > 1500:
            self.spawn_supermonster()

    def game_over(self):
        #reinitialisation du jeu
        self.les_monstres = pygame.sprite.Group()
        self.les_supermonstres = pygame.sprite.Group()
        self.player.rect.x = 100
        self.bloc_event.les_blocs = pygame.sprite.Group()
        self.player.health = self.player.max_health
        self.bloc_event.reset_percent()
        self.score = 0
        self.gameover = True
        self.is_playing = False
        gameoversound.play()



    def actualiser(self, fenetre):
        fenetre.blit(self.player.image, self.player.rect)

        # actualiser la barre de vie du joueur
        self.player.update_health_bar(fenetre)



        #actualiser la barre d'évenements du jeu
        self.bloc_event.update_bar(fenetre)

            #récuperer les monstre
        for monstre in self.les_monstres:
            monstre.move()

            #récupérer les supermonstres
        for supermonstre in self.les_supermonstres:
            supermonstre.move()
            supermonstre.update_health_bar(fenetre)

            # récupérer les projectiles du joueur
        for projectile in jeu.player.all_projectiles:
            projectile.move()

        #recup les bloc
        for bloc in self.bloc_event.les_blocs:
            bloc.move()
        # apparition des monstres
        self.les_monstres.draw(fenetre)
        self.les_supermonstres.draw(fenetre)

        #apparition des blocs

        self.bloc_event.les_blocs.draw(fenetre)

        # commande joueur

        if self.pressed.get(pygame.K_LEFT) and self.player.rect.x > self.player.vit_x:
            self.player.move_left()
        if self.pressed.get(pygame.K_RIGHT) and self.player.rect.x < 1200 - self.player.width - self.player.vit_x:
            self.player.move_right()

        if self.player.jump is False and self.pressed.get(pygame.K_UP):
            self.player.jump = True

        if self.player.jump is True:
            if not self.check_ifhit(self.player, self.bloc_event.les_blocs):
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

    def spawn_supermonster(self):
        supermonstre = Super_Monstre(self)
        self.les_supermonstres.add(supermonstre)

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
        self.attack = 10
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
            if jeu.score > jeu.topscore:
                jeu.topscore = jeu.score
            if jeu.score > 0:
                jeu.yourscore = jeu.score
            pygame.mixer.music.stop()
            self.jeu.game_over() #si plus de vie


    def update_health_bar(self, surface):
       #barre de vie
       pygame.draw.rect(surface, (60, 63, 60), [self.rect.x + 45, self.rect.y -20, self.max_health, 10])
       pygame.draw.rect(surface, (111, 210, 46), [self.rect.x + 45, self. rect.y - 20, self.health, 10])


    def move_right(self):
        #joueur ne touche pas un bloc
        if not self.jeu.check_ifhit(self, self.jeu.bloc_event.les_blocs) or self.jump:
            self.rect.x += self.vit_x

    def move_left(self):
        self.rect.x -= self.vit_x

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
        if self.rect.x <= 0:
            self.rect.x = 1000 + random.randint(300, 500)
            self.vit = random.randint(1, 5)

        if self.jeu.score >= 200:
          self.rect.x -= random.randint(5,10)

        if self.jeu.score >= 500:
            self.rect.x -= random.randint(10,20)

# super méchant monstre

class Super_Monstre (pygame.sprite.Sprite):
    def __init__(self, jeu):
        super().__init__()
        self.jeu = jeu
        self.health = 100
        self.max_health = 100
        self.attack = 30
        self.image = pygame.transform.scale(pygame.image.load("super_méchant.png"), (172,264))
        self.rect = self.image.get_rect()
        self.rect.x = 1000 + random.randint(0,200)
        self.rect.y = 210
        self.vit = random.randint(1,10)

    def degats(self, amount):
        #infliger des degats
        self.health -= amount
        #voir si le nb de points de vie et plus petit ou égal à 0
        if self.health <= 0:
            self.remove()


    def remove(self):
        self.jeu.les_supermonstres.remove(self)

    def move(self):
        # le dépacement se fait uniquement lorsque le monstre ne touche pas le joueur
        self.rect.x -= self.vit

        if self.jeu.check_ifhit(self, self.jeu.les_joueurs):
            self.rect.x = 1000 + random.randint(300, 500)
            self.vit = random.randint(1, 10)
            self.jeu.player.damage(self.attack)
        if self.rect.x <= 0:
            self.rect.x = 1000 + random.randint(300, 500)
            self.vit = random.randint(1, 5)

    def update_health_bar(self, surface):
       #barre de vie
       pygame.draw.rect(surface, (60, 63, 60), [self.rect.x + 40, self.rect.y - 20 , self.max_health, 10])
       pygame.draw.rect(surface, (255, 0, 0), [self.rect.x + 40, self. rect.y - 20 , self.health, 10])



#projectile

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

        #voir si le projectil touche un supermonstre
        for supermonstre in self.player.jeu.check_ifhit(self,self.player.jeu.les_supermonstres):
            self.remove()
            supermonstre.degats(self.player.attack)
        #projectile plus présent sur l'écran

        if self.rect.x > 1200:
            self.remove()







class blocEvent:
    #lors du chargement -> créer un compteur
    def __init__(self, jeu):
        self.jeu = jeu
        self.percent = 0
        self.speed = 100


        #groupe de sprite pour stocker les blocs
        self.les_blocs = pygame.sprite.Group()



    def add_percent(self):
        self.percent += self.speed/100


    def jauge_max(self):
        return self.percent >= 100


    def reset_percent(self):
        self.percent = 0


    def bloc_arrive(self):
        self.les_blocs.add(bloc(self))

    def lesblocs(self):
        # la jauge au max
        if self.jauge_max():
            self.bloc_arrive()
            self.reset_percent()

    def update_bar(self, fenetre):

        #ajouter du pourcentage à la barre
        self.add_percent()

        #arrivée de blocs
        self.lesblocs()

        #barre noir (en arriere plan)
        pygame.draw.rect(fenetre, (0, 0, 0), [
            0,
            fenetre.get_height() - 40,
            fenetre.get_width(),
            20
        ])
        #barre rouge (jauge d'event)
        pygame.draw.rect(fenetre, (255, 215, 0, 255), [
            0,
            fenetre.get_height() - 40,
            (fenetre.get_width() / 100)*self.percent,
            20
            ])


#bloc

class bloc(pygame.sprite.Sprite):

    def __init__(self, bloc_event):
        super().__init__()
        self.image = pygame.transform.scale(pygame.image.load('brique.png'),(150,300))
        self.rect = self.image.get_rect()
        self.vit = random. randint(5,10)
        self.rect.x = 1200
        self.rect.y = 255
        self.bloc_event = bloc_event

    def remove(self):
        # suppression de du bloc
        self.bloc_event.les_blocs.remove(self)


    def move(self):
        if not self.bloc_event.jeu.check_ifhit(self, self.bloc_event.jeu.les_joueurs) or self.bloc_event.jeu.player.jump:
            self.rect.x -= self.vit

    #arrive au bout
        if self.rect.x <= 0:
          self.remove()


        if self.bloc_event.jeu.check_ifhit(self, self.bloc_event.jeu.les_joueurs):
            self.bloc_event.jeu.player.damage(1)






#instances
jeu = Jeu()


#main loop
run = True

while run:

    # fps
    fps.tick(30)

    #fond
    dupli_fond()






    #appliquer l'ensemble des images du groupe projectile
    jeu.player.all_projectiles.draw(fenetre)

    #gamestarting
    if jeu.is_playing:
        jeu.score += 1
        draw_text(fenetre, "Score : " +str(jeu.score),30,600,30)

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


    if jeu.gameover:


        fenetre.fill(white)
        fenetre.blit(embleme, embleme_rect)
        fenetre.blit(tryagain_bouton, tryagain_bouton_rect)
        draw_text(fenetre, "Top Score : " + str(jeu.topscore), 60, 600, 300)
        draw_text(fenetre, "Your Score : " + str(jeu.yourscore), 50, 600, 350)







    #mettre a jour l'écran
    pygame.display.flip()
    #fermer fenetre
    for event in pygame.event.get():


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
                pygame.mixer.music.load("rock-your-heart-out.mp3")
                pygame.mixer.music.play(-1, 0.0)

            if tryagain_bouton_rect.collidepoint(event.pos):  # vérifier si la souris touche le bouton try again
                gameoversound.stop()
                jeu.start()



           


