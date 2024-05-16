import pygame
import time

class Banana:

    def __init__(self, x, y):
        self.x = x
        self.y = y
        self.image = pygame.image.load("banana.png")
        # self.rescale_image(self.image)
        self.image_size = self.image.get_size()
        self.rect = pygame.Rect(self.x, self.y, self.image_size[0], self.image_size[1])
        self.delta = 1

    # def rescale_image(self, image):
    #     self.image_size = self.image.get_size()
    #     scale_size = (self.image_size[0] * .5, self.image_size[1] * .5)
    #     self.image = pygame.transform.scale(self.image, scale_size)

    def move_direction(self, direction):

        if direction == "right":
            self.x = self.x + self.delta
        if direction == "left":
            self.x = self.x - self.delta
        self.rect = pygame.Rect(self.x, self.y, self.image_size[0], self.image_size[1])