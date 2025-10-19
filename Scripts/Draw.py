import pygame


sizeCell = 0
sizeSnake = 0



def Snake(screen, snake):
    for Position in snake:
        indentation = 0.5*(sizeCell - sizeSnake)
        r = pygame.Rect((Position[0]*sizeCell + indentation, Position[1]*sizeCell + indentation), (sizeSnake, sizeSnake))
        pygame.draw.rect(screen, (0, 255, 0), r, 0)


def Apple(screen, Position):
    indentation = 0.5*(sizeCell - sizeSnake)
    r = pygame.Rect((Position[0]*sizeCell + indentation, Position[1]*sizeCell + indentation), (sizeSnake, sizeSnake))
    pygame.draw.rect(screen, (255, 0, 0), r, 0)


def Pause(screen):
    my_surface = pygame.Surface((50, 50), pygame.SRCALPHA)

    r = pygame.Rect((0, 0), (20, 50))
    pygame.draw.rect(my_surface, (255, 255, 255), r, 0)
    r = pygame.Rect((30, 0), (20, 50))
    pygame.draw.rect(my_surface, (255, 255, 255), r, 0)

    # Устанавливаем прозрачность 50%
    my_surface.set_alpha(128)

    # Отображаем поверхность на экране
    screen.blit(my_surface, (50, 50))
    
