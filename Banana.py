import pygame
import time

class Banana:

    def __init__(self, x, y):
        self.x = x
        self.y = y
        self.image_list = ["banana.png", "button.png"]
        self.image = pygame.image.load(self.image_list[0])
        # self.rescale_image(self.image)
        self.image_size = self.image.get_size()
        self.rect = pygame.Rect(self.x, self.y, self.image_size[0], self.image_size[1])
        self.delta = 5

    # def rescale_image(self, image):
    #     self.image_size = self.image.get_size()
    #     scale_size = (self.image_size[0] * .5, self.image_size[1] * .5)
    #     self.image = pygame.transform.scale(self.image, scale_size)

    def move_direction(self, direction):

        if direction == "right":
            self.x = self.x + self.delta
        if direction == "left":
            self.x = self.x - self.delta
        # if direction == "jump":
        #     self.y =
        if direction == "duck":
            image_number = 1
            self.image = pygame.image.load(self.image_list[image_number])
        if direction == "idle":
            image_number = 0
            self.image = pygame.image.load(self.image_list[image_number])
            # self.rescale_image(self.image)
            self.image_size = self.image.get_size()

        self.rect = pygame.Rect(self.x, self.y, self.image_size[0], self.image_size[1])


        self.rect = pygame.Rect(self.x, self.y, self.image_size[0], self.image_size[1])