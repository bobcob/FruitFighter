import random

import pygame
import time
from Test import Test

pygame.init()
pygame.font.init()
my_font = pygame.font.SysFont('Arial', 15)
pygame.display.set_caption("Fruit Fighter")
size = (1000, 600)
screen = pygame.display.set_mode(size)
current_time = time.time() - time.time()
test = Test(50,50)
move = False


run = True

while run:
    keys = pygame.key.get_pressed()
    if keys[pygame.K_d]:
        test.move_direction("right")
    if keys[pygame.K_a]:
        test.move_direction("left")
    # if keys[pygame.K_f]:
    #     test.attack()

    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            run = False
        if event.type == pygame.KEYUP and keys[pygame.K_f]:
            test.attack()




    screen.fill((0, 0, 0))

    screen.blit(test.image, test.rect)
    pygame.display.update()

# Once we have exited the main program loop we can stop the game engine:
pygame.quit()

