from pygame.sprite import Sprite
import pygame
from config import *


class Enemy2_Bullet1(Sprite):

    def __init__(self, x, y, size, screen):
        super().__init__()
        self.x = x
        self.y = y
        self.screen = screen

        self.image = pygame.image.load(f'assets/Enemy_Bullet.png')
        self.image = pygame.transform.scale(self.image, (int(size*1.0), size))

        self.speed = 8

        self.rect = pygame.Rect(x, y, self.image.get_width(), self.image.get_height())

    def update(self):
        self.y += self.speed
        self.rect.y = self.y

        if DEBUG_MODE:
            pygame.draw.rect(self.screen, RED, self.rect)

        self.screen.blit(self.image, (self.x, self.y))
