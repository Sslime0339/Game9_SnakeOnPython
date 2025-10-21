from Scripts import Draw
from Scripts.Snake import Snake
from Scripts.Apple import Apple
from Scripts.Vector2D import Vector2D

import pygame
import os

pygame.init()

Draw.sizeCell = 20
Draw.sizeSnake = 18

snake = Snake()

snake.widthMap = 30
snake.hightMap = 30

screen = pygame.display.set_mode((snake.widthMap * Draw.sizeCell, snake.hightMap * Draw.sizeCell))

#загрузка
if not os.path.exists("Save"):
    os.mkdir("Save")

maxScore = 0
if os.path.exists("Save/Score.txt"):
    SaveFile = open("Save/Score.txt", "r")
    line = SaveFile.readline()
    if line != "":
        maxScore = int(line)

    SaveFile.close()
#====


snake.NewGame()

run = True
IsPause = False


while (run):
    for event in pygame.event.get():
        if (event.type == pygame.QUIT):
            run = False

        if (event.type == pygame.KEYDOWN):
            snake.СhangeCourse(pygame.key.name(event.key))

            if (event.key == pygame.K_ESCAPE):
                IsPause = not IsPause
        
    if not IsPause:
        snake.Move()
        maxScore = max(maxScore, snake.Length)

    screen.fill((0, 0, 0))
    Draw.Apple(screen, snake.Apple)
    Draw.Snake(screen, snake.bodyPart)
    Draw.Score(screen, snake.Length)
    if IsPause:
        Draw.MaxScore(screen, maxScore)
        Draw.Pause(screen)
    pygame.display.flip()

    pygame.time.delay(800)
    
    


#сохранение
if not os.path.exists("Save"):
    os.mkdir("Save")


SaveFile = open("Save/Score.txt", "w")
SaveFile.write(str(maxScore))

SaveFile.close()
#====

pygame.quit()
