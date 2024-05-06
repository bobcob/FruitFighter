import pygame
from Test import Test

pygame.init()
pygame.font.init()
my_font = pygame.font.SysFont('Arial', 15)
pygame.display.set_caption("")
size = (1000, 600)
screen = pygame.display.set_mode(size)

test = Test(50,50)


run = True

while run:

    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            run = False

    screen.fill((0, 0, 0))

    screen.blit(test.image, test.rect)
    pygame.display.update()

# Once we have exited the main program loop we can stop the game engine:
pygame.quit()

