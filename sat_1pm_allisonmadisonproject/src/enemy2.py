from pygame.sprite import Sprite
import pygame
from config import *


class Enemy2(Sprite):

    def __init__(self, x, y, size, screen):
        super().__init__()
        self.x = x
        self.y = y
        self.screen = screen
        self.size = size

        self.image = pygame.image.load(f'assets/Avatar_Bunny_front.png')
        self.image = pygame.transform.scale(self.image, (int(size * 2), (int(size * 2))))

        self.rect = pygame.Rect(x, y, self.image.get_width(), self.image.get_height())

    def update(self):
        self.rect.x = self.x
        self.rect.y = self.y

        if DEBUG_MODE:
            pygame.draw.rect(self.screen, RED, self.rect)
        self.screen.blit(self.image, (self.x, self.y))
