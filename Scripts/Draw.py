import pygame


sizeCell = 20
sizeSnake = 18



def Snake(screen, snake):
    for Position in snake:
        indentation = 0.5*(sizeCell - sizeSnake)
        r = pygame.Rect((Position[0]*sizeCell + indentation, Position[1]*sizeCell + indentation), (sizeSnake, sizeSnake))
        print(Position[0], Position[1])
        pygame.draw.rect(screen, (0, 255, 0), r, 0)
