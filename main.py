
import pygame
import time
from Test import Test
from AppleTest import Apple
from Banana import Banana

pygame.init()
pygame.font.init()
my_font = pygame.font.SysFont('Arial', 15)
pygame.display.set_caption("Fruit Fighter")

size = (1000, 600)
screen = pygame.display.set_mode(size)
start_time = time.time()
current_time = 0

test = Test(50,50)
test2 = Test(350, 50)
apple = Apple(50,150)
banana = Banana(400, 150)
move = False
a_attack = False
a_attack_cd = False
b_attack = False
b_attack_cd = False
cd = 0
cd2 = 0
stun = 0
stun2 = 0
hit = False
hit2 = False
a_move = True
b_move = True
display_time = my_font.render(str(current_time), True, (255, 255, 255))
display_cd = my_font.render(str(cd), True, (255, 255, 255))

run = True

while run:
    current_time = round((time.time() - start_time), 2)
    display_time = my_font.render(str(current_time), True, (255, 255, 255))
    test = Test(apple.x + 300, 200)
    test2 = Test(banana.x - 250, 200)
    keys = pygame.key.get_pressed()

    if a_move:
        if keys[pygame.K_d]:
            apple.move_direction("right")
        if keys[pygame.K_a]:
            apple.move_direction("left")

    if b_move:
        if keys[pygame.K_RIGHT]:
            banana.move_direction("right")
        if keys[pygame.K_LEFT]:
            banana.move_direction("left")

    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            run = False
        if event.type == pygame.KEYUP:
            if keys[pygame.K_f]:
                a_attack = True
                a_attack_cd = True
            elif keys[pygame.K_m]:
                b_attack = True
                b_attack_cd = True

    if a_attack_cd:
        cd += 1
        a_move = False
        if cd >= 150:
            a_attack = False
            a_attack_cd = False
            a_move = True
            cd = 0

    if b_attack_cd:
        cd2 += 1
        b_move = False
        if cd2 >= 150:
            b_attack = False
            b_attack_cd = False
            b_move = True
            cd2 = 0

    if test.rect.colliderect(banana.rect) and a_attack:
        stun2 += 1
        b_move = False
        hit2 = True
        if stun2 >= 200:
            hit2 = False
            b_move = True
            stun2 = 0

    if test2.rect.colliderect(apple.rect) and b_attack:
        stun += 1
        a_move = False
        hit = True
        if stun >= 200:
            hit = False
            a_move = True
            stun = 0

    screen.fill((0, 0, 0))
    screen.blit(apple.image, apple.rect)
    screen.blit(banana.image, banana.rect)
    screen.blit(display_time, (0, 45))
    screen.blit(display_cd, (0, 15))
    if a_attack and a_attack_cd:
        screen.blit(test.image, test.rect)
    if b_attack and b_attack_cd:
        screen.blit(test2.image, test2.rect)

    pygame.display.update()

# Once we have exited the main program loop we can stop the game engine:
pygame.quit()

