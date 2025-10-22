from Scripts.GameObject import GameObject
from Scripts.Vector2D import Vector2D

import random


def NewApple(gameMap):
    Apple(gameMap, Vector2D(random.randint(0, gameMap.widthMap-1), random.randint(0, gameMap.hightMap-1)))

class Apple(GameObject):


    def Eat(self):
        NewApple(self.gameMap)
        self.gameMap.DestroyObject(self)


    def __init__(self, gameMap, position : Vector2D):
        super().__init__(gameMap, position)
        # if isinstance(position, Vector2D):
        # else:
        #     print('ошибка: яблоко получило не тот тип данных')

    def __str__(self):
        return f"position: {self.Position}"
