from Scripts.GameObject import GameObject
from Scripts.Vector2D import Vector2D
from Scripts.SnakeBodyPart import SnakeBodyPart
from Scripts.Apple import Apple

import random
import pygame



class Snake(GameObject):
    

    bodyPart = 0
    Course = 0

    Length = 0

    OnDied = lambda: print('Умер')

    # widthMap = 0
    # hightMap = 0


    # Apple = [0, 0]

    def __init__(self, gameMap):
        mapCenter = Vector2D(int(gameMap.widthMap/2), int(gameMap.hightMap/2))
        super().__init__(gameMap, mapCenter)
        self.gameMap.EmptyPosition.remove(mapCenter) # удалить свободную клетку там где появляется змейка
        
        self.Length = 3
        self.Course = Vector2D(0, -1)
        if (gameMap.hightMap > 5):
            self.bodyPart = [SnakeBodyPart(gameMap, mapCenter+Vector2D(0, 1)), 
                             SnakeBodyPart(gameMap, mapCenter+Vector2D(0, 2))]
            self.gameMap.EmptyPosition.remove(mapCenter+Vector2D(0, 1)) # удалить свободную клетку там где появляется змейка
            self.gameMap.EmptyPosition.remove(mapCenter+Vector2D(0, 2)) # удалить свободную клетку там где появляется змейка
        else:
            self.Length = 1
            self.bodyPart = []
            print("слишком маленькая карта")


    # def NewApple(self):
    #     self.Apple = [random.randint(0, self.widthMap-1), random.randint(0, self.hightMap-1)]


    # def NewGame(self):
    #     self.bodyPart = [[15, 15], [15, 16], [15, 17]]
    #     self.Length = 3
    #     self.Course = [0, -1]
    #     self.NewApple()


    def СhangeCourse(self, course):
        if (course == "w"):
            self.Course = Vector2D(0, -1)
        if (course == "s"):
            self.Course = Vector2D(0, 1)
        if (course == "a"):
            self.Course = Vector2D(-1, 0)
        if (course == "d"):
            self.Course = Vector2D(1, 0)


    def Move(self):
        lastPosition = self.bodyPart[-1].Position
        for i in range(len(self.bodyPart) - 1, -1, -1):
            if i != 0:
                self.bodyPart[i].Position = self.bodyPart[i-1].Position
            else:
                self.bodyPart[0].Position = self.Position

        newPosition = self.Position + self.Course

        objectOfTouch = self.gameMap.CheckCollision(newPosition)
        
        self.Position = newPosition



        if self.IsDeath():
            self.gameMap.NewGame()
            return

        
        if isinstance(objectOfTouch, Apple):
            self.bodyPart += [SnakeBodyPart(self.gameMap, lastPosition)]
            self.Length += 1
            objectOfTouch.Eat()
        else:
            self.gameMap.EmptyPosition.remove(newPosition)
            self.gameMap.EmptyPosition.append(lastPosition)


    def IsDeath(self):
        for i in range(len(self.bodyPart)):
            if self.Position == self.bodyPart[i].Position:
                return True
        if self.Position.x < 0 or self.Position.x >= self.gameMap.widthMap \
        or self.Position.y < 0 or self.Position.y >= self.gameMap.hightMap:
            return True
        return False
