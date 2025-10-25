import pygame

from Scripts.Vector2D import Vector2D
from Scripts.Snake import Snake


sizeCell = 0
sizeSnake = 0

eyeSize = 0
distanceBetweenEyes = 0


def Snake(screen, snake : Snake):
    for i in range(len(snake.bodyPart)):
        if i > 0:
            course = snake.bodyPart[i - 1].Position - snake.bodyPart[i].Position
            SnakeBodyPart(screen, snake.bodyPart[i].Position, course)
        else:
            course = snake.Position - snake.bodyPart[i].Position
            SnakeBodyPart(screen, snake.bodyPart[i].Position, course)
    SnakeBodyPart(screen, snake.Position)
    SnakeFace(screen, snake.Position, snake.Course)


# ыыыыыы
def SnakeFace(screen, Position, Course):
    my_surface = pygame.Surface((sizeSnake, sizeSnake), pygame.SRCALPHA)

    indentationX = 0 if Course.x > 0 else Course.x * eyeSize * 0.5
    indentationY = 0 if Course.y > 0 else Course.y * eyeSize * 0.5

    indentationX += sizeSnake / 2
    indentationY += sizeSnake / 2

    x = int(Course.x * sizeSnake / 4 + Course.y * distanceBetweenEyes + indentationX)
    y = int(Course.y * sizeSnake / 4 + Course.x * distanceBetweenEyes + indentationY)
    r = pygame.Rect((x, y), (eyeSize, eyeSize))
    pygame.draw.rect(my_surface, (0, 0, 0), r, 0)

    x = int(Course.x * sizeSnake / 4 - Course.y * distanceBetweenEyes + indentationX)
    y = int(Course.y * sizeSnake / 4 - Course.x * distanceBetweenEyes + indentationY)
    r = pygame.Rect((x, y), (eyeSize, eyeSize))
    pygame.draw.rect(my_surface, (0, 0, 0), r, 0)
    
    indentation = 0.5*(sizeCell - sizeSnake)
    screen.blit(my_surface, (Position.x*sizeCell + indentation, Position.y*sizeCell + indentation))
    pass


def SnakeBodyPart(screen, Position, Course = Vector2D(0, 0)):
    indentation = 0.5*(sizeCell - sizeSnake)
    indentationX = 0 if Course.x > 0 else Course.x*2*(sizeCell - sizeSnake)
    indentationY = 0 if Course.y > 0 else Course.y*2*(sizeCell - sizeSnake)

    # вычисляем размер блока змейки с учётом направления
    size = (sizeSnake + abs(Course.x)*2*(sizeCell - sizeSnake) , sizeSnake + abs(Course.y)*2*(sizeCell - sizeSnake))
    # также с позицией
    rectPosition = (Position[0]*sizeCell + indentation + indentationX, 
                    Position[1]*sizeCell + indentation + indentationY)
    r = pygame.Rect(rectPosition, size)
    pygame.draw.rect(screen, (0, 255, 0), r, 0)


def Apple(screen, Position):
    indentation = 0.5*(sizeCell - sizeSnake)
    r = pygame.Rect((Position[0]*sizeCell + indentation, Position[1]*sizeCell + indentation), (sizeSnake, sizeSnake))
    pygame.draw.rect(screen, (255, 0, 0), r, 0)

def DrawEmptyPosition(screen, Position):
    r = pygame.Rect((Position[0]*sizeCell, Position[1]*sizeCell), (5, 5))
    pygame.draw.rect(screen, (150, 150, 150), r, 0)
    pass




def Pause(screen):
    my_surface = pygame.Surface((50, 50), pygame.SRCALPHA)

    r = pygame.Rect((0, 0), (20, 50))
    pygame.draw.rect(my_surface, (255, 255, 255), r, 0)
    r = pygame.Rect((30, 0), (20, 50))
    pygame.draw.rect(my_surface, (255, 255, 255), r, 0)

    # Устанавливаем прозрачность 50%
    my_surface.set_alpha(128)

    # Отображаем поверхность на экране
    screen.blit(my_surface, (275, 275))


def FPS(screen, fps):
    Text(screen, fps, (400, 400))


def Score(screen, score):
    Text(screen, score, (400, 15))

def MaxScore(screen, score):
    #костыль для отрисовки слова длина
    Text(screen, "длина:", (50, 15))

    Text(screen, "максимальная", (50, 65))
    Text(screen, "длина:", (50, 115))
    Text(screen, score, (400, 115))


def Text(screen, text, position, sizeText=50, color=(255, 255, 255)):
    font = pygame.font.SysFont('couriernew', sizeText)
    renderText = font.render(str(text), True, color)
    screen.blit(renderText, position)
