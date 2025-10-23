
from Scripts import Draw
from Scripts.Vector2D import Vector2D
from Scripts.Apple import Apple, NewApple
from Scripts.GameObject import GameObject
from Scripts.Snake import Snake
from Scripts.SnakeBodyPart import SnakeBodyPart


class GameMap:
    

    widthMap = 30
    hightMap = 30

    EmptyPosition = []

    GameObjects = []
    snake = 0

    


    def __init__(self, widthMap, hightMap):
        self.widthMap = widthMap
        self.hightMap = hightMap


    def NewGame(self):
        self.GameObjects.clear()
        self.EmptyPosition = [Vector2D(x, y) for x in range(self.widthMap) for y in range(self.hightMap)]
        self.snake = Snake(self)
        NewApple(self)
        for i in range(10):
            # if i % 10 == 0:
            #     print(i)
            NewApple(self)


    # def CreatGameObject(self, object : GameObject):
    #     object.GameMap = self
    #     AddGameObject

    #     return object


    def AddGameObject(self, obj):
        self.GameObjects += [obj]


    def DestroyObject(self, object : GameObject):
        self.GameObjects.remove(object)
        # Object.Destroy()

    def VacatePosition(self, position):
        # позиция освободилась => в масив свобоных мест добавилась позиция
        if (self.CheckCollision(position) == None and
            position.x >= 0 and position.x < self.widthMap and
            position.y >= 0 and position.y < self.hightMap):
            self.EmptyPosition.append(position)
    
    def TakeAPosition(self, position):
        # забирает позицию
        # Возможны баги !!!!
        if position in self.EmptyPosition:
            self.EmptyPosition.remove(position)
        else:
            # print('эта позиция занята или не существует')
            pass

    def CheckCollision(self, position : Vector2D):
        for obj in self.GameObjects:
            if obj.Position == position and obj != object:
                return obj
        return None
    
    def DrawObjects(self, screen):
        for obj in self.GameObjects:
            if isinstance(obj, SnakeBodyPart) or isinstance(obj, Snake):
                Draw.SnakeBodyPart(screen, obj.Position)
            elif isinstance(obj, Apple):
                Draw.Apple(screen, obj.Position)
    
    def DrawEmptyPosition(self, screen):
        for pos in self.EmptyPosition:
            Draw.DrawEmptyPosition(screen, pos)