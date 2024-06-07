import pygame
import random
from bird import Bird
from balloon import Balloon

# set up pygame modules
pygame.init()
pygame.font.init()
my_font = pygame.font.SysFont('Arial', 20)
red_font = pygame.font.SysFont('Arial', 50)
pygame.display.set_caption("Balloon Flight!")


# set up variables for the display
size = (800, 600)
screen = pygame.display.set_mode(size)
BIRD_START_X = 950

bg = pygame.image.load("background.png")
house = pygame.image.load("house.png")
tree = pygame.image.load("tree.png")


bird = Bird(BIRD_START_X, 250)
b = Balloon(300, 200)


INITIAL_HOUSE_X = random.randint(0,600)
INITIAL_TREE_X = random.randint(0,600)
house_x = INITIAL_HOUSE_X
tree_x = INITIAL_TREE_X

game_start = False
game_over = False
direction = "down"
score = 0

# render the text for later
display_intro = red_font.render("Welcome to Balloon Flight", True, (255, 0, 0))
display_intro2 = my_font.render("Hold Space bar to go up", True, (0, 0, 0))
display_intro3 = my_font.render("Dodge the flying bird", True, (0, 0, 0))
display_intro4 = my_font.render("Click anywhere to start", True, (0, 0, 0))

display_score = my_font.render("Score: " + str(score), True, (0, 0, 0))

display_game_over = red_font.render("GAME OVER", True, (255, 0, 0))
display_game_over2 = my_font.render("Final Score: " + str(score), True, (0, 0, 0))

# The loop will carry on until the user exits the game (e.g. clicks the close button).
run = True
# -------- Main Program Loop -----------
clock = pygame.time.Clock()
frame = 0
while run:
    # --- Main event loop
    clock.tick(60)

    if game_start and not game_over:
        bird.move_bird()
        b.move_balloon(direction)
        house_x -= 2
        tree_x -= 3
        if house_x < -200:
            house_x = 1000
        if tree_x < -200:
            tree_x = 1000

        if frame % 30 == 0:
            bird.switch_image()

        if b.rect.colliderect(bird.rect):
            game_over = True

        if bird.x == 198:
            score += 1
            display_score = my_font.render("Score: " + str(score), True, (0, 0, 0))
            display_game_over2 = my_font.render("Final Score: " + str(score), True, (0, 0, 0))


    for event in pygame.event.get():  # User did something
        if event.type == pygame.QUIT:  # If user clicked close
                run = False
        if event.type == pygame.MOUSEBUTTONDOWN:
            game_start = True
        if game_start:
            if event.type == pygame.KEYDOWN:
                if event.key == pygame.K_SPACE:
                    direction = "up"
            if event.type == pygame.KEYUP:
                direction = "down"


    screen.blit(bg, (0, 0))

    if not game_start:
        screen.blit(display_intro, (200, 170))
        screen.blit(display_intro2, (200, 225))
        screen.blit(display_intro3, (200, 250))
        screen.blit(display_intro4, (200, 275))

    elif game_start and not game_over:
        screen.blit(house, (house_x, 360))
        screen.blit(tree, (tree_x, 360))
        screen.blit(b.image, b.rect)
        screen.blit(bird.image, bird.rect)
        screen.blit(display_score, (0, 0))

    elif game_over:
        screen.blit(display_game_over, (200, 170))
        screen.blit(display_game_over2, (200, 225))

    pygame.display.update()

    frame += 1

# Once we have exited the main program loop we can stop the game engine:
pygame.quit()

