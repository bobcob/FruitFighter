import random

import pygame
import time
from Test import Test
from AppleTest import Apple

pygame.init()
pygame.font.init()
my_font = pygame.font.SysFont('Arial', 15)
pygame.display.set_caption("Fruit Fighter")

size = (1000, 600)
screen = pygame.display.set_mode(size)
start_time = time.time()
current_time = 0

test = Test(50,50)
apple = Apple(50,150)
move = False
attack = False
attack_cd = False
cd = 0
display_time = my_font.render(str(current_time), True, (255, 255, 255))
display_cd = my_font.render(str(cd), True, (255, 255, 255))

run = True

while run:
    current_time = round((time.time() - start_time), 2)
    display_time = my_font.render(str(current_time), True, (255, 255, 255))
    test = Test(apple.x + 300, 200)
    keys = pygame.key.get_pressed()
    if keys[pygame.K_d]:
        apple.move_direction("right")
    if keys[pygame.K_a]:
        apple.move_direction("left")

    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            run = False
        if event.type == pygame.KEYUP and keys[pygame.K_f]:
            attack = True
            attack_cd = True
    if attack_cd:
        cd = time.time() - start_time
        if cd >= 3.5:
            attack_cd = False
            cd =0
        display_cd = my_font.render(str(cd), True, (255, 255, 255))





    screen.fill((0, 0, 0))
    screen.blit(apple.image, apple.rect)
    screen.blit(display_time, (0, 45))
    screen.blit(display_cd, (0, 15))
    if attack and attack_cd:
        screen.blit(test.image, test.rect)

    pygame.display.update()

# Once we have exited the main program loop we can stop the game engine:
pygame.quit()

