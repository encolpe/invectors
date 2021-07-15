import pygame
from player import Player
from invader_line_1 import Invader10
from line1 import ApparitionLine1
from line2 import ApparitionLine2
from line3 import ApparitionLine3
from line4 import ApparitionLine4
from line5 import ApparitionLine5
from line6 import ApparitionLine6

class Game:

    def __init__(self):
        self.is_playing = False
        self.player = Player()
        self.line1 = ApparitionLine1()
        self.line2 = ApparitionLine2()
        self.line3 = ApparitionLine3()
        self.line4 = ApparitionLine4()
        self.line5 = ApparitionLine5()
        self.line6 = ApparitionLine6()
        self.all_players = pygame.sprite.Group()
        self.all_players.add(Player())
        self.pressed = {}

    def start(self):
        self.is_playing = True

    def update(self, screen):
        # affichage du joueur
        screen.blit(self.player.image, self.player.rect)

        # recuperer les projectiles du joueur
        for projectile_player in self.player.all_projectiles:
            projectile_player.move()

        # dessin des projectiles ennemis
        self.player.all_projectiles.draw(screen)
        self.line1.dessin(screen)
        self.line2.dessin(screen)
        self.line3.dessin(screen)
        self.line4.dessin(screen)
        self.line5.dessin(screen)
        self.line6.dessin(screen)

        # spawn des invaders
        self.line1.spawn_invader()
        self.line2.spawn_invader()
        self.line3.spawn_invader()
        self.line4.spawn_invader()
        self.line5.spawn_invader()
        self.line6.spawn_invader()

        if self.pressed.get(pygame.K_RIGHT) and self.player.rect.x < 980:
            self.player.move_right()
        elif self.pressed.get(pygame.K_LEFT) and self.player.rect.x > 50:
            self.player.move_left()


