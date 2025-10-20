from Scripts import Draw
from Scripts import Snake

import pygame
import os

pygame.init()

Draw.sizeCell = 20
Draw.sizeSnake = 18

Snake.widthMap = 30
Snake.hightMap = 30

screen = pygame.display.set_mode((Snake.widthMap * Draw.sizeCell, Snake.hightMap * Draw.sizeCell))

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


Snake.NewGame()

run = True
IsPause = False


while (run):
    for event in pygame.event.get():
        if (event.type == pygame.QUIT):
            run = False

        if (event.type == pygame.KEYDOWN):
            Snake.СhangeCourse(pygame.key.name(event.key))

            if (event.key == pygame.K_ESCAPE):
                IsPause = not IsPause
        
    if not IsPause:
        Snake.Move()
        maxScore = max(maxScore, Snake.Length)

    screen.fill((0, 0, 0))
    Draw.Apple(screen, Snake.Apple)
    Draw.Snake(screen, Snake.bodyPart)
    Draw.Score(screen, Snake.Length)
    if IsPause:
        Draw.MaxScore(screen, maxScore)
        Draw.Pause(screen)
    pygame.display.flip()

    pygame.time.delay(800)
    
    


#сохранение
if not os.path.exists("Save"):
    os.mkdir("Save")

if os.path.exists("Save/Score.txt"):
    SaveFile = open("Save/Score.txt", "w")
    SaveFile.write(str(maxScore))

SaveFile.close()
#====

pygame.quit()
