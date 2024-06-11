import pygame

class Hitbox:

    def __init__(self, x, y):
        self.x = x
        self.y = y
        self.image = pygame.image.load("hitbox.png")
        self.rescale_image(self.image)
        self.image_size = self.image.get_size()
        self.rect = pygame.Rect(self.x, self.y, self.image_size[0], self.image_size[1])
        self.delta = 1

    def rescale_image(self, image):
        self.image_size = self.image.get_size()
        scale_size = (self.image_size[0] * 5, self.image_size[1] * 5)
        self.image = pygame.transform.scale(self.image, scale_size)


    def attack(self):
        initial = self.x
        while self.x < initial + 100:
            self.x += 1
            if self.x == initial + 100:
                while self.x != initial:
                    self.x -= 1
        self.rect = pygame.Rect(self.x, self.y, self.image_size[0], self.image_size[1])







