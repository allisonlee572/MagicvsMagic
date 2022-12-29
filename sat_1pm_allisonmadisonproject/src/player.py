from pygame.sprite import Sprite
import pygame
from config import *


class Player(Sprite):

    def __init__(self, x, y, size, screen):
        super().__init__()
        self.x = x
        self.y = y
        self.screen = screen
        self.size = size
        self.speed = 6

        self.image = pygame.image.load(f'assets/Avatar_MAGI_right.png')
        self.image = pygame.transform.scale(self.image, (int(size * 2), (int(size * 2.5))))

        self.rect = pygame.Rect(x, y, self.image.get_width(), self.image.get_height())

    def set_position(self, x, y):
        self.x = x
        self.y = y
        self.rect.x = self.x
        self.rect.y = self.y

    def update(self):
        keys_pressed = pygame.key.get_pressed()

        if keys_pressed[pygame.K_d]:
            self.x += self.speed

        self.rect.x = self.x
        self.rect.y = self.y

        if DEBUG_MODE:
            pygame.draw.rect(self.screen, RED, self.rect)

        self.screen.blit(self.image, (self.x, self.y))
