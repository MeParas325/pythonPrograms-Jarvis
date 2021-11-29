import pygame

# x = pygame.init()
# print(x)

# Colours
white = (255, 255, 255)
red = (255, 0, 0)
black = (0, 0, 0)

gameWindow = pygame.display.set_mode((1200, 500))
pygame.display.set_caption("My Second Game")

#Creating game variables
exit_game = False
game_over = False

while not exit_game:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            exit_game = True


    gameWindow.fill(white)
    pygame.display.update()


pygame.quit()
quit()