
import pygame
from Test import Test
from AppleTest import Apple
from Banana import Banana
from Button import Button

pygame.init()
pygame.font.init()
my_font = pygame.font.SysFont('Arial', 15)
pygame.display.set_caption("Fruit Fighter")

size = (1000, 600)
screen = pygame.display.set_mode(size)

# SPRITES
test = Test(50,50)
test2 = Test(350, 50)
apple = Apple(50,150)
banana = Banana(400, 150)
button = Button(375, 150)

# VARIABLES
game_start = False
a_attack = False
a_attack_cd = False
b_attack = False
b_attack_cd = False
a_hp = 100
b_hp = 100
cd = 0
cd2 = 0
stun = 0
stun2 = 0
hit = False
hit2 = False
a_move = True
b_move = True
a_hit = False
b_hit = False
run = True
jump = False
start = False
color = (255,0,0)
clock = pygame.time.Clock()


display_ahp = my_font.render(str(a_hp), True, (255, 255, 255))
display_bhp = my_font.render(str(b_hp), True, (255, 255, 255))


while run:
    clock.tick(360)
    keys = pygame.key.get_pressed()
    if start:

        test = Test(apple.x + 300, 200)
        test2 = Test(banana.x - 250, 200)

        # APPLE MOVEMENT
        if a_move:
            if keys[pygame.K_d]:
                apple.move_direction("right")
            if keys[pygame.K_a]:
                apple.move_direction("left")
            if keys[pygame.K_w]:
                apple.move_direction("jump")
            if keys[pygame.K_s]:
                apple.move_direction("duck")
            else:
                apple.move_direction("idle")

        # BANANA MOVEMENT
        if b_move:
            if keys[pygame.K_RIGHT]:
                banana.move_direction("right")
            if keys[pygame.K_LEFT]:
                banana.move_direction("left")
            if keys[pygame.K_UP]:
                banana.move_direction("jump")
            if keys[pygame.K_DOWN]:
                banana.move_direction("duck")
            else:
                banana.move_direction("idle")

    # APPLE ATTACK
        if a_attack:
            cd += 1
            a_move = False
            if test.rect.colliderect(banana.rect):
                b_move = False
                b_hit = True
            if cd >= 150:
                a_attack = False
                a_move = True
                b_move = True
                cd = 0
        if b_hit and not a_attack:
            b_hp -= 5
            display_bhp = my_font.render(str(b_hp), True, (255, 255, 255))
            b_hit = False

    # BANANA ATTACK
        if b_attack:
            cd2 += 1
            b_move = False
            if test2.rect.colliderect(apple.rect):
                a_move = False
                a_hit = True
            if cd2 >= 150:
                b_attack = False
                b_move = True
                a_move = True
                cd2 = 0
        if a_hit and not b_attack:
            a_hp -= 5
            display_ahp = my_font.render(str(a_hp), True, (255, 255, 255))
            a_hit = False


    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            run = False
        if event.type == pygame.MOUSEBUTTONUP:  # Start button
            mouse_position = pygame.mouse.get_pos()
            if (button.rect.collidepoint(mouse_position)):
                start = True
        if event.type == pygame.KEYUP:
            if keys[pygame.K_f] and start:
                a_attack = True
            elif keys[pygame.K_m] and start:
                b_attack = True
        # if event.type == pygame.KEYDOWN and keys[pygame.K_s]:
        #     apple.move_direction("duck")




    screen.fill((0, 0, 0))
    if start:
        screen.blit(apple.image, apple.rect)
        screen.blit(banana.image, banana.rect)
        screen.blit(display_ahp, (0,0))
        screen.blit(display_bhp, (800, 0))
        if a_attack:
            screen.blit(test.image, test.rect)
        if b_attack:
            screen.blit(test2.image, test2.rect)
    else:
        screen.blit(button.image, button.rect)

    pygame.display.update()

# Once we have exited the main program loop we can stop the game engine:
pygame.quit()

