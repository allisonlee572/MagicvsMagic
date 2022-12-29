from pygame.sprite import Sprite
import pygame
from config import *


class BattleEnemy1(Sprite):

    def __init__(self, x, y, direction, size, screen):
        super().__init__()
        self.x = x
        self.y = y
        self.screen = screen
        self.direction = direction
        self.size = size

        self.image = pygame.image.load(f'assets/Avatar_Boli.png')
        self.image = pygame.transform.scale(self.image, (int(size * 2), (int(size * 2))))
        self.rect = pygame.Rect(x, y, self.image.get_width(), self.image.get_height())

        self.health = 10

    def reset_battle_enemy_1(self, x, y):
        self.x = x
        self.y = y
        self.rect.x = self.x
        self.rect.y = self.y
        self.health = 10

    def update(self):
        self.rect.x = self.x
        self.rect.y = self.y

        if DEBUG_MODE:
            pygame.draw.rect(self.screen, BLUE, self.rect)
        self.screen.blit(self.image, (self.x, self.y))
