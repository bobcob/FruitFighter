import pygame

class Apple:
    def __init__(self, x, y):
        self.x = x
        self.y = y
        self.image_list = ["apple.png", "button.png"]
        self.image = pygame.image.load(self.image_list[0])
        self.rescale_image(self.image)
        self.image_size = self.image.get_size()
        self.rect = pygame.Rect(self.x, self.y, self.image_size[0], self.image_size[1])
        self.delta = 1
        self.duck = False

    def rescale_image(self, image):
        self.image_size = self.image.get_size()
        scale_size = (self.image_size[0] * .1, self.image_size[1] * .1)
        self.image = pygame.transform.scale(self.image, scale_size)

    def move_direction(self, direction):
        if direction == "right":
            self.x = self.x + self.delta
            if self.x >= 900:
                self.x = 900
        if direction == "left":
            self.x = self.x - self.delta
            if self.x <= 0:
                self.x = 0
        # if direction == "jump":
        #     self.y =
        if direction == "duck":
            self.duck = True
            self.ducking()

        self.rect = pygame.Rect(self.x, self.y, self.image_size[0], self.image_size[1])

    def ducking(self):
        image_number = 1
        if not self.duck:
            image_number = 0
        self.image = pygame.image.load(self.image_list[image_number])
        self.rescale_image(self.image)
        self.image_size = self.image.get_size()
        self.duck = not self


