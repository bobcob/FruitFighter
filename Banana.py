import pygame
class Banana:

    def __init__(self, x, y):
        self.x = x
        self.y = y
        self.image_list = ["banana.png", "button.png"]
        self.image = pygame.image.load(self.image_list[0])
        # self.rescale_image(self.image)
        self.image_size = self.image.get_size()
        self.rect = pygame.Rect(self.x, self.y, self.image_size[0], self.image_size[1])
        self.delta = 2

    # def rescale_image(self, image):
    #     self.image_size = self.image.get_size()
    #     scale_size = (self.image_size[0] * .5, self.image_size[1] * .5)
    #     self.image = pygame.transform.scale(self.image, scale_size)

    def move_direction(self, direction):
        if direction == "right":
            self.x = self.x + self.delta
            if self.x >= 900:
                self.x = 900
        elif direction == "left":
            self.x = self.x - self.delta
            if self.x <= 0:
                self.x = 0
        # elif direction == "jump":
        #     self.y =
        elif direction == "duck":
            self.image = pygame.image.load(self.image_list[1])
        elif direction == "idle":
            self.image = pygame.image.load(self.image_list[0])
            # self.rescale_image(self.image)

        self.image_size = self.image.get_size()
        self.rect = pygame.Rect(self.x, self.y, self.image_size[0], self.image_size[1])