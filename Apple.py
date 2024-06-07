import pygame

class Apple:
    def __init__(self, x, y):
        self.x = x
        self.y = y
        self.image_list = ["apple_idle1.png", "apple_idle2.png", "button.png"]
        self.image = pygame.image.load(self.image_list[0])
        self.rescale_image(self.image)
        self.image_size = self.image.get_size()
        self.rect = pygame.Rect(self.x, self.y, self.image_size[0], self.image_size[1])
        self.delta = 10
        self.idle1 = True

    def rescale_image(self, image):
        self.image_size = self.image.get_size()
        scale_size = (self.image_size[0] * 5, self.image_size[1] * 5)
        self.image = pygame.transform.scale(self.image, scale_size)

    def move_direction(self, direction):
        jump_count = 10
        if direction == "right":
            self.x = self.x + self.delta
            if self.x >= 850:
                self.x = 850
        elif direction == "left":
            self.x = self.x - self.delta
            if self.x <= 0:
                self.x = 0
        elif direction == "duck":
            self.image = pygame.image.load(self.image_list[2])
        elif direction == "idle":
            self.image = pygame.image.load(self.image_list[0])
            self.rescale_image(self.image)

        self.image_size = self.image.get_size()
        self.rect = pygame.Rect(self.x, self.y, self.image_size[0], self.image_size[1])

    def switch_image(self):
        image_number = 0
        if not self.idle1:
            image_number = 1
        self.image = pygame.image.load(self.image_list[image_number])
        self.rescale_image(self.image)
        self.image_size = self.image.get_size()
        self.idle1 = not self.idle1

