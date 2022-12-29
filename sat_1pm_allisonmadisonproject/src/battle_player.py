from pygame.sprite import Sprite
import pygame
from config import *


class BattlePlayer(Sprite):

    def __init__(self, x, y, direction, size, screen):
        super().__init__()
        self.x = x
        self.y = y
        self.screen = screen
        self.direction = direction
        self.size = size
        self.player_image_timer = IMAGE_DELAY

        self.speed = 8

        self.right_images = []
        self.left_images = []
        for idx in range(1,2):
            self.image = pygame.image.load(f'assets/Avatar_MAGI_back.png')
            self.image = pygame.transform.scale(self.image, (int(size * 2.0), (int(size * 2.5))))
            self.right_images.append(self.image)

            left_image = pygame.transform.flip(self.image, True, False)
            self.left_images.append(left_image)

            self.image_index = 0

            if self.direction == RIGHT:
                self.images = self.right_images
            if self.direction == LEFT:
                self.images = self.left_images

            self.image = self.get_next_image()
            self.rect = pygame.Rect(x, y, self.image.get_width(), self.image.get_height())

    def get_next_image(self):
        self.player_image_timer -= 1
        if self.player_image_timer == 0:
            self.player_image_timer = IMAGE_DELAY
            self.image_index += 1
        if self.image_index == len(self.images):
            self.image_index = 0
        if self.direction == RIGHT:
            self.images = self.right_images
        if self.direction == LEFT:
            self.images = self.left_images
        return self.images[self.image_index]

    def reset_battle_player(self, x, y):
        self.x = x
        self.y = y
        self.rect.x = self.x
        self.rect.y = self.y

    def update(self):
        keys_pressed = pygame.key.get_pressed()

        if keys_pressed[pygame.K_a]:
            self.x -= self.speed
            self.direction = LEFT
        if keys_pressed[pygame.K_d]:
            self.x += self.speed
            self.direction = RIGHT

        self.image = self.get_next_image()
        
        self.rect.x = self.x
        self.rect.y = self.y

        if DEBUG_MODE:
            pygame.draw.rect(self.screen, BLUE, self.rect)
        self.screen.blit(self.image, (self.x, self.y))

