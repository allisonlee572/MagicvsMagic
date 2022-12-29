from pygame.sprite import Sprite
import pygame
from config import *


class BattleEnemy3(Sprite):

    def __init__(self, x, y, size, screen):
        super().__init__()
        self.x = x
        self.y = y
        self.screen = screen
        self.direction = RIGHT
        self.size = size
        self.speed = 5
        self.enemy_image_timer = IMAGE_DELAY

        self.right_images = []
        self.left_images = []
        for idx in range(1,2):
            self.image = pygame.image.load(f'assets/Avatar_Cat.png')
            self.image = pygame.transform.scale(self.image, (int(size * 2), (int(size * 2))))
            self.left_images.append(self.image)

            right_image = pygame.transform.flip(self.image, True, False)
            self.right_images.append(right_image)

            self.image_index = 0

            if self.direction == RIGHT:
                self.images = self.right_images
            if self.direction == LEFT:
                self.images = self.left_images

            self.image = self.get_next_image()
            self.rect = pygame.Rect(x, y, self.image.get_width(), self.image.get_height())

        self.health = 15

    def get_next_image(self):
        self.enemy_image_timer -= 1
        if self.enemy_image_timer == 0:
            self.enemy_image_timer = IMAGE_DELAY
            self.image_index += 1
        if self.image_index == len(self.images):
            self.image_index = 0
        if self.direction == RIGHT:
            self.images = self.right_images
        if self.direction == LEFT:
            self.images = self.left_images
        return self.images[self.image_index]

    def reset_battle_enemy_3(self, x, y):
        self.x = x
        self.y = y
        self.rect.x = self.x
        self.rect.y = self.y
        self.health = 15

    def update(self):
        self.image = self.get_next_image()
        
        self.rect.x = self.x
        self.rect.y = self.y

        start_x = 100
        end_x = 900

        if self.direction == RIGHT:
            self.x += self.speed
        if self.direction == LEFT:
            self.images = self.left_images
            self.x -= self.speed

        if self.x <= start_x:
            self.direction = RIGHT
        if self.x >= end_x:
            self.direction = LEFT

        if DEBUG_MODE:
            pygame.draw.rect(self.screen, BLUE, self.rect)
        self.screen.blit(self.image, (self.x, self.y))
