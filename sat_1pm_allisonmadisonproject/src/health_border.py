from pygame.sprite import Sprite
import pygame


class HealthBorder(Sprite):

    def __init__(self, x, y, size, screen):
        super().__init__()
        self.x = x
        self.y = y
        self.screen = screen

        self.image = pygame.image.load(f'assets/Health_Border.jpg')
        self.image = pygame.transform.scale(self.image, (int(size * 6.5), (int(size * 1.5))))

    def update(self):
        self.screen.blit(self.image, (self.x, self.y))
