from joueur import player
from monstre import Monstre
import pygame
import random

# class qui représente le jeu
class Jeu:
    def __init__(self):
        #start
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
        if self.pressed.get(pygame.K_RIGHT) and self.player.rect.x + self.player.width < fenetre.get_width():
            self.player.move_right()
        elif self.pressed.get(pygame.K_LEFT) and self.player.rect.x > 0:
            self.player.move_left()
        if self.pressed.get(pygame.K_DOWN) and self.player.rect.y + self.player.height + 70 < fenetre.get_height():
            self.player.move_down()

    def check_ifhit(self, sprite, group):
        return pygame.sprite.spritecollide(sprite, group, False, pygame.sprite.collide_mask)


    def spawn_monster(self):
        monstre = Monstre(self)
        self.les_monstres.add(monstre)