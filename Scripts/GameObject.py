from Scripts.Vector2D import Vector2D
# from Scripts.GameMap import GameMap

class GameObject:
    __Position = Vector2D()
    gameMap = 0

    #свойства

    #получить переменную
    @property
    def Position(self):
        return self.__Position
    
    #присвоить значение переменной
    @Position.setter
    def Position(self, position):
        lastPosition = self.__Position.new()
        self.__Position = position
        self.gameMap.TakeAPosition(position)
        self.gameMap.VacatePosition(lastPosition)



    def __init__(self, gameMap, position):
        # важно сначала добавить карту
        self.gameMap = gameMap
        self.Position = position
        self.gameMap.AddGameObject(self)
    
    def __str__(self):
        return f"Position: {self.Position}"