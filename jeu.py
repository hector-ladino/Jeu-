from joueur import player
from monstre import Monstre
import pygame


# class qui représente le jeu
class Jeu:
    def __init__(self):
        self.player = player()
        #plusieurs méchants
        self.les_monstres = pygame.sprite.Group()
        self.pressed = {}
        self.spawn_monster()

    def spawn_monster(self):
        monstre = Monstre()
        self.les_monstres.add(monstre)