import pygame
import random
import time
from fox import Fox
from blue_fox import Blue_Fox
from coin import Coin
from red_coin import Red_Coin
from spiked_ball import Spiked_Ball

# set up pygame modules
pygame.init()
pygame.font.init()
my_font = pygame.font.SysFont('Arial', 15)
pygame.display.set_caption("Coin Collector!")

# highscores
f1 = open("highscore", "r")
data = f1.readline().strip()

f2 = open("highscore2", "r")
data2 = f2.readline().strip()

# set up variables for the display
SCREEN_HEIGHT = 370
SCREEN_WIDTH = 600
size = (SCREEN_WIDTH, SCREEN_HEIGHT)
screen = pygame.display.set_mode(size)

name = "Collect coins as fast as you can!"
r = 50
g = 0
b = 100
score = 0
score2 = 0
current_time = 10.00
game_start = False
game_over = False
start_time = 0
sb_cooldown = 0
r_c_chance = random.randint(1, 8)
display_r_c = False
touch_sb = True
new_highscore = False
new_highscore2 = False

# render the text for later
display_name = my_font.render(name, True, (255, 255, 255))

# Fox1
display_score = my_font.render("Score: " + str(score), True, (255, 255, 255))
# Fox2
display_score2 = my_font.render("Score: " + str(score2), True, (255, 255, 255))

display_time = my_font.render("Time remaining: " + str(current_time) + "s", True, (255, 255, 255))
display_start = my_font.render("Use WASD to move", True, (255, 255, 255))
display_start_2 = my_font.render("You have 10 seconds to collect 10 coins", True, (255, 255, 255))
display_start_3 = my_font.render("Click anywhere on the screen to begin!", True, (255, 255, 255))
display_end = my_font.render("Game Over!", True, (255, 255, 255))
# Highscores display
if int(data) > 0:
    display_highscore = my_font.render("Highscore: " + str(data), True, (255, 255, 255))
else:
    display_highscore = my_font.render("Highscore: N/A", True, (255, 255, 255))

if int(data2) > 0:
    display_highscore2 = my_font.render("Highscore: " + str(data2), True, (255, 255, 255))
else:
    display_highscore2 = my_font.render("Highscore: N/A", True, (255, 255, 255))

display_new_highscore = my_font.render("Player1 New highscore!: " + str(data), True, (255, 255, 255))
display_new_highscore2 = my_font.render("Player2 New highscore!: " + str(data2), True, (255, 255, 255))


f = Fox(40, 60)
c = Coin(200, 85)
r_c = Red_Coin(random.randint(45, 480), random.randint(45, 330))
s_b = Spiked_Ball(100, -100)
bf = Blue_Fox(450, 60)

# The loop will carry on until the user exits the game (e.g. clicks the close button).
run = True

# -------- Main Program Loop -----------
while run:
    if game_start:

        s_b.move_ball()
        current_time = round(10 - (time.time() - start_time), 2)
        display_time = my_font.render("Time remaining: " + str(current_time) + "s", True, (255, 255, 255))
        keys = pygame.key.get_pressed()  # checking pressed keys
        # Fox1
        if keys[pygame.K_d]:
            f.move_direction("right")
        if keys[pygame.K_a]:
            f.move_direction("left")
        if keys[pygame.K_w]:
            f.move_direction("up")
        if keys[pygame.K_s]:
            f.move_direction("down")

        # Fox2
        if keys[pygame.K_RIGHT]:
            bf.move_direction("right")
        if keys[pygame.K_LEFT]:
            bf.move_direction("left")
        if keys[pygame.K_UP]:
            bf.move_direction("up")
        if keys[pygame.K_DOWN]:
            bf.move_direction("down")

        # collision
        if f.rect.colliderect(c.rect):
            c.set_location(random.randint(45, 480), random.randint(45, 330))
            score += 10
            display_score = my_font.render("Score: " + str(score), True, (255, 255, 255))
        if bf.rect.colliderect(c.rect):
            c.set_location(random.randint(45, 480), random.randint(45, 330))
            score2 += 10
            display_score2 = my_font.render("Score: " + str(score2), True, (255, 255, 255))


        if f.rect.colliderect(r_c.rect) and display_r_c:
            score += 20
            display_score = my_font.render("Score: " + str(score), True, (255, 255, 255))
            display_r_c = False
        if bf.rect.colliderect(r_c.rect) and display_r_c:
            score2 += 20
            display_score2 = my_font.render("Score: " + str(score2), True, (255, 255, 255))
            display_r_c = False


        if f.rect.colliderect(s_b.rect):
            if touch_sb:
                score -= 10
                display_score = my_font.render("Score: " + str(score), True, (255, 255, 255))
                touch_sb = False
                sb_cooldown = current_time - 1
        if bf.rect.colliderect(s_b.rect):
            if touch_sb:
                score2 -= 10
                display_score2 = my_font.render("Score: " + str(score2), True, (255, 255, 255))
                touch_sb = False
                sb_cooldown = current_time - 1

        if current_time <= sb_cooldown:
            touch_sb = True

    if current_time == 0:
        game_over = True

    if game_over:
        if score > int(data):
            data = score
            f1 = open("highscore", "w")
            f1.write(str(data))
            display_highscore = my_font.render("Highscore: " + str(data), True, (255, 255, 255))
            new_highscore = True
            display_new_highscore = my_font.render("Player1 New highscore!: " + str(data), True, (255, 255, 255))
        if score2 > int(data2):
            data2 = score2
            f2 = open("highscore2", "w")
            f2.write(str(data2))
            display_highscore2 = my_font.render("Highscore: " + str(data2), True, (255, 255, 255))
            new_highscore2 = True
            display_new_highscore2 = my_font.render("Player2 New highscore!: " + str(data2), True, (255, 255, 255))

    # --- Main event loop
    for event in pygame.event.get():  # User did something
        if event.type == pygame.MOUSEBUTTONUP:
            game_start = True
            start_time = time.time()
            c = Coin(random.randint(45, 480), random.randint(45, 330))

        if event.type == pygame.QUIT:  # If user clicked close
            run = False
    current_time = round(10 - (time.time() - start_time), 2)
    display_time = my_font.render("Time remaining: " + str(current_time) + "s", True, (255, 255, 255))
    screen.fill((r, g, b))
    if game_start and not game_over:
        screen.blit(display_name, (0, 0))
        screen.blit(display_score, (0, 15))
        screen.blit(display_score2, (530, 15))
        screen.blit(display_highscore, (0, 30))
        screen.blit(display_highscore2, (500, 30))
        screen.blit(display_time, (0, 45))
        screen.blit(f.image, f.rect)
        screen.blit(bf.image, bf.rect)
        screen.blit(c.image, c.rect)
        screen.blit(s_b.image, s_b.rect)

        if current_time == r_c_chance:
            display_r_c = True
            
        if display_r_c:
            if current_time > r_c_chance - 2:
                screen.blit(r_c.image, r_c.rect)


    elif not game_start and not game_over:
        screen.blit(display_start, (140, 150))
        screen.blit(display_start_2, (140, 165))
        screen.blit(display_start_3, (140, 180))
        screen.blit(f.image, f.rect)
        screen.blit(c.image, c.rect)

    elif game_over:
        screen.blit(display_end, (200, 165))
        if new_highscore:
            screen.blit(display_new_highscore, (200, 180))
        if new_highscore2:
            screen.blit(display_new_highscore2, (200, 195))

    pygame.display.update()

# Once we have exited the main program loop we can stop the game engine:
pygame.quit()
