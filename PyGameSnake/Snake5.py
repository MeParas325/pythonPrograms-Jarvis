import pygame

# x = pygame.init()
# print(x)

gameWindow = pygame.display.set_mode((1200, 500))
pygame.display.set_caption("My Second Game")
#Creating game variables
exit_game = False
game_over = False

while not exit_game:
    for event in pygame.event.get():
        print(event)

pygame.quit()
quit()