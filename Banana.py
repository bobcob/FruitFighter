import pygame
class Banana:

    def __init__(self, x, y):
        self.x = x
        self.y = y
        self.image_list = ["banana_idle1.png", "banana_idle2.png", "banana_duck.png", "banana_jump.png", "banana_attack.png"]
        self.image = pygame.image.load(self.image_list[0])
        self.rescale_image(self.image)
        self.image_size = self.image.get_size()
        self.rect = pygame.Rect(self.x, self.y, self.image_size[0], self.image_size[1])
        self.delta = 10
        self.idle1 = True
        self.current_direction = "right"

    def rescale_image(self, image):
        self.image_size = self.image.get_size()
        scale_size = (self.image_size[0] * 5, self.image_size[1] * 5)
        self.image = pygame.transform.scale(self.image, scale_size)

    def move_direction(self, direction):
        # DIRECTION FACING
        if self.current_direction == "right" and direction == "left":
            self.image = pygame.transform.flip(self.image, True, False)

        if self.current_direction == "left" and direction == "right":
            self.image = pygame.transform.flip(self.image, True, False)
        # MOVEMENT
        if direction == "right":
            self.current_direction = "right"
            self.x = self.x + self.delta
            if self.x >= 850:
                self.x = 850
        elif direction == "left":
            self.current_direction = "left"
            self.x = self.x - self.delta
            if self.x <= 0:
                self.x = 0
        elif direction == "jump":
            self.image = pygame.image.load(self.image_list[3])
            self.rescale_image(self.image)
        elif direction == "duck":
            self.image = pygame.image.load(self.image_list[2])
            self.rescale_image(self.image)
        elif direction == "idle":
            self.image = pygame.image.load(self.image_list[0])
            self.rescale_image(self.image)
        elif direction == "attack":
            self.image = pygame.image.load(self.image_list[4])
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

