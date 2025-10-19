from Scripts import Draw
from Scripts import Snake

import pygame

pygame.init()

Draw.sizeCell = 20
Draw.sizeSnake = 18

Snake.widthMap = 30
Snake.hightMap = 30

screen = pygame.display.set_mode((Snake.widthMap * Draw.sizeCell, Snake.hightMap * Draw.sizeCell))


Snake.bodyPart = [[15, 15], [15, 16], [15, 17]]


run = True


while (run):
    for event in pygame.event.get():
        if (event.type == pygame.QUIT):
            run = False

        if (event.type == pygame.KEYDOWN):
            Snake.СhangeCourse(pygame.key.name(event.key))
            
        
    
    Snake.Move()

    screen.fill((0, 0, 0))
    Draw.Snake(screen, Snake.bodyPart)
    pygame.display.flip()

    pygame.time.delay(1000)
    
    



pygame.quit()
