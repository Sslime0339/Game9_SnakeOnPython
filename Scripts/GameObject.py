from Scripts.Vector2D import Vector2D
# from Scripts.GameMap import GameMap

class GameObject:
    Position = Vector2D()
    gameMap = 0

    def __init__(self, gameMap, position):
        self.Position = position
        self.gameMap = gameMap
        self.gameMap.AddGameObject(self)
    
    def __str__(self):
        return f"Position: {self.Position}"