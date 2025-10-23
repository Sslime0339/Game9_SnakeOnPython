from Scripts.GameObject import GameObject
from Scripts.Vector2D import Vector2D
# from Scripts.GameMap import GameMap

import random


def NewApple(gameMap):

    if len(gameMap.EmptyPosition) > 0:
        newPosition = gameMap.EmptyPosition[random.randint(0, len(gameMap.EmptyPosition)) - 1].new()
        Apple(gameMap, newPosition)

    # newPosition = Vector2D(random.randint(0, gameMap.widthMap-1), random.randint(0, gameMap.hightMap-1))
    
    # не оптимизированно
    # cells = [Vector2D(x, y) for x in range(gameMap.widthMap) for y in range(gameMap.hightMap)]

    # for obj in gameMap.GameObjects:
    #     if obj.Position in cells:
    #         cells.remove(obj.Position)

    # if len(cells) >= 1:
    #     newPosition = cells[random.randint(0, len(cells) - 1)]


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
