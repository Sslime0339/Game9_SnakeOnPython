
from Scripts import Draw
from Scripts.Apple import Apple
from Scripts.Apple import NewApple
from Scripts.GameObject import GameObject
from Scripts.Snake import Snake
from Scripts.SnakeBodyPart import SnakeBodyPart


class GameMap:
    

    widthMap = 30
    hightMap = 30


    GameObjects = []
    snake = 0


    def __init__(self, widthMap, hightMap):
        self.widthMap = widthMap
        self.hightMap = hightMap


    def NewGame(self):
        self.GameObjects.clear()
        self.snake = Snake(self)
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

    def CheckCollision(self, object : GameObject):
        for obj in self.GameObjects:
            if obj.Position == object.Position and obj != object:
                return obj
    
    def DrawObjects(self, screen):
        for obj in self.GameObjects:
            print(obj)
            if isinstance(obj, SnakeBodyPart):
                Draw.SnakeBodyPart(screen, obj.Position)
            elif isinstance(obj, Apple):
                Draw.Apple(screen, obj.Position)