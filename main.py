import pygame
from Hitbox import Hitbox
from Apple import Apple
from Banana import Banana
from Button import Button

pygame.init()
pygame.font.init()
start_end_font = pygame.font.SysFont('Papyrus', 48)
hp_font = pygame.font.SysFont('Papyrus', 32)
pygame.display.set_caption("Fruit Fighter")

size = (1000, 600)
screen = pygame.display.set_mode(size)

# SPRITES
apple_box = Hitbox(0, 0)
banana_box = Hitbox(0, 0)
apple = Apple(50,320)
banana = Banana(700, 305)
button = Button(375, 150)
bg = pygame.image.load("bg.png")

# VARIABLES
a_attack = False
a_attack_cd = False
b_attack = False
b_attack_cd = False
a_hp = 100
b_hp = 100
cd = 0
cd2 = 0
a_move = True
b_move = True
a_hit = False
b_hit = False
run = True
a_jump = False
b_jump = False
start = False
game_over = False
a_win = False
b_win = False
frame = 0
a_jumpCount = 10
b_jumpCount = 10
color = (255,0,0)

# TEXT
display_start = start_end_font.render("TOUCH LEMONT", True, (255, 0, 0))
display_ahp = hp_font.render("APPLE: " + str(a_hp), True, (0, 0, 0))
display_bhp = hp_font.render("BANANA: " + str(b_hp), True, (0, 0, 0))
display_a_win = start_end_font.render("APPLE WINS", True, (0, 0, 0))
display_b_win = start_end_font.render("BANANA WINS", True, (0, 0, 0))

while run:
    clock = pygame.time.Clock()
    keys = pygame.key.get_pressed()
    if start and not game_over:
        apple_box = Hitbox(apple.x + 150, 375)
        banana_box = Hitbox(banana.x - 25, 350)
        if a_hp <= 0:
            b_win = True
            game_over = True
        if b_hp <= 0:
            a_win = True
            game_over = True


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
            if apple_box.rect.colliderect(banana.rect):
                b_move = False
                b_hit = True
            if cd >= 30:
                a_attack = False
                a_move = True
                b_move = True
                cd = 0
        if b_hit and not a_attack:
            b_hp -= 5
            display_bhp = hp_font.render("BANANA: " + str(b_hp), True, (0, 0, 0))
            b_hit = False

    # BANANA ATTACK
        if b_attack:
            banana.move_direction("attack")
            cd2 += 1
            b_move = False
            if banana_box.rect.colliderect(apple.rect):
                a_move = False
                a_hit = True
            if cd2 >= 30:
                b_attack = False
                b_move = True
                a_move = True
                cd2 = 0
        if a_hit and not b_attack:
            a_hp -= 5
            display_ahp = hp_font.render("APPLE: " + str(a_hp), True, (0, 0, 0))
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


    screen.blit(bg, (0, 0))
    if not game_over:
        if start:
            screen.blit(apple.image, apple.rect)
            screen.blit(banana.image, banana.rect)
            screen.blit(display_ahp, (0, 0))
            screen.blit(display_bhp, (700, 0))
        else:
            screen.blit(button.image, button.rect)
            screen.blit(display_start, (250, 125))
    if game_over:
        if a_win:
            screen.blit(display_a_win, (250, 150))
        if b_win:
            screen.blit(display_b_win, (250, 150))

    clock.tick(60)

    pygame.display.update()

    frame += 1

# Once we have exited the main program loop we can stop the game engine:
pygame.quit()

