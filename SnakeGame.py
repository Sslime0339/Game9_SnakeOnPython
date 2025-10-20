from Scripts import Draw
from Scripts import Snake

import pygame

pygame.init()

Draw.sizeCell = 20
Draw.sizeSnake = 18

Snake.widthMap = 30
Snake.hightMap = 30

screen = pygame.display.set_mode((Snake.widthMap * Draw.sizeCell, Snake.hightMap * Draw.sizeCell))

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

    screen.fill((0, 0, 0))
    Draw.Apple(screen, Snake.Apple)
    Draw.Snake(screen, Snake.bodyPart)
    Draw.Score(screen, 600)
    if IsPause:
        Draw.Pause(screen)
    pygame.display.flip()

    pygame.time.delay(800)
    
    



pygame.quit()
