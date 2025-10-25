from Scripts import Draw
from Scripts.Snake import Snake
from Scripts.Apple import Apple, NewApple
from Scripts.Vector2D import Vector2D
from Scripts.GameMap import GameMap

import pygame
import os

pygame.init()

Draw.sizeCell = 20
Draw.sizeSnake = 18
Draw.eyeSize = 4
Draw.distanceBetweenEyes = 4

fps = 60
snakeSpeed = 4 # клеток в секунду
lastGameTime = 0

showFPS = pygame.time.Clock()


gameMap = GameMap(30, 30)
gameMap.NewGame()


screen = pygame.display.set_mode((gameMap.widthMap * Draw.sizeCell, gameMap.hightMap * Draw.sizeCell))
pygame.display.set_caption("Змейка")


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


# snake.NewGame()

run = True
IsPause = False


while (run):
    for event in pygame.event.get():
        if (event.type == pygame.QUIT):
            run = False

        if (event.type == pygame.KEYDOWN):
            gameMap.snake.СhangeCourse(pygame.key.name(event.key))

            if (event.key == pygame.K_ESCAPE):
                IsPause = not IsPause
    
    if not IsPause:
        time = pygame.time.get_ticks()
        if time > (lastGameTime + 1000/snakeSpeed):
            lastGameTime = time
            #print(pygame.time.get_ticks())
            gameMap.snake.Move()
            maxScore = max(maxScore, gameMap.snake.Length)

    screen.fill((0, 0, 0))
    
    gameMap.DrawObjects(screen)
    # gameMap.DrawEmptyPosition(screen) # для отрисовки пустых клеток

    Draw.Score(screen, gameMap.snake.Length)

    # showFPS.tick()
    # Draw.FPS(screen, showFPS.get_fps())
    if IsPause:
        Draw.MaxScore(screen, maxScore)
        Draw.Pause(screen)
    pygame.display.flip()


    pygame.time.delay(int(1000/fps))
    
    


#сохранение
if not os.path.exists("Save"):
    os.mkdir("Save")


SaveFile = open("Save/Score.txt", "w")
SaveFile.write(str(maxScore))

SaveFile.close()
#====

pygame.quit()
