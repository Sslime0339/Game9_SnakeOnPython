from Scripts import Draw
from Scripts import Snake

import pygame

pygame.init()

screen = pygame.display.set_mode((600, 600))

run = True


while (run):
    for event in pygame.event.get():
        if (event.type == pygame.QUIT):
            run = False

        if (event.type == pygame.KEYDOWN):
            Snake.Move(pygame.key.name(event.key))
            
        
        if event.type == pygame.MOUSEBUTTONDOWN:
            my_pos = event.pos
            my_button = event.button
            print(f"Позиция мыши: {my_pos}")
            print(f"Идентификатор кнопки мыши: {my_button}")
    

    screen.fill((0, 0, 0))
    Draw.Snake(screen, Snake.bodyPart)
    pygame.display.flip()

    pygame.time.delay(60)
    
    



pygame.quit()
