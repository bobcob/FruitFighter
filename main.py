
import pygame
from Test import Test
from Apple import Apple
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
a_jump = False
b_jump = False
start = False
frame = 0
a_jumpCount = 10
b_jumpCount = 10
color = (255,0,0)

display_ahp = my_font.render(str(a_hp), True, (255, 255, 255))
display_bhp = my_font.render(str(b_hp), True, (255, 255, 255))


while run:
    clock = pygame.time.Clock()
    keys = pygame.key.get_pressed()
    if start:

        test = Test(apple.x + 300, 200)
        test2 = Test(banana.x - 250, 200)

        # APPLE MOVEMENT
        if a_move:
            if keys[pygame.K_d]:
                apple.move_direction("right")
            elif keys[pygame.K_a]:
                apple.move_direction("left")
            elif keys[pygame.K_s]:
                apple.move_direction("duck")
            else:
                apple.move_direction("idle")
                if frame % 12 == 0:
                    apple.switch_image()
        if a_jump:
            apple.move_direction("jump")
            if a_jumpCount >= -10:
                apple.y -= (a_jumpCount * abs(a_jumpCount)) * 0.5
                a_jumpCount -= 1
            else:
                a_jumpCount = 10
                a_jump = False


        # BANANA MOVEMENT
        if b_move:
            if keys[pygame.K_RIGHT]:
                banana.move_direction("right")
            elif keys[pygame.K_LEFT]:
                banana.move_direction("left")
            elif keys[pygame.K_DOWN]:
                banana.move_direction("duck")
            else:
                banana.move_direction("idle")
                if frame % 12 == 0:
                    banana.switch_image()

        if b_jump:
            banana.move_direction("jump")
            if b_jumpCount >= -10:
                banana.y -= (b_jumpCount * abs(b_jumpCount)) * 0.5
                b_jumpCount -= 1
            else:
                b_jumpCount = 10
                b_jump = False

    # APPLE ATTACK
        if a_attack:
            apple.move_direction("attack")
            cd += 1
            a_move = False
            if test.rect.colliderect(banana.rect):
                b_move = False
                b_hit = True
            if cd >= 30:
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
            banana.move_direction("attack")
            cd2 += 1
            b_move = False
            if test2.rect.colliderect(apple.rect):
                a_move = False
                a_hit = True
            if cd2 >= 30:
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
            elif keys[pygame.K_w]:   #apple jump
                a_jump = True
            elif keys[pygame.K_UP]:     #banana jump
                b_jump = True


    screen.fill((0, 208, 255))
    if start:
        screen.blit(apple.image, apple.rect)
        screen.blit(banana.image, banana.rect)
        screen.blit(display_ahp, (0, 0))
        screen.blit(display_bhp, (800, 0))
        if a_attack:
            screen.blit(test.image, test.rect)
        if b_attack:
            screen.blit(test2.image, test2.rect)
    else:
        screen.blit(button.image, button.rect)

    clock.tick(60)

    pygame.display.update()

    frame += 1

# Once we have exited the main program loop we can stop the game engine:
pygame.quit()

