from Scripts.GameObject import GameObject


class SnakeBodyPart(GameObject):
    

    def __init__(self, gameMap, position):
        super().__init__(gameMap, position)

    def __str__(self):
        return "Sn: " + super().__str__()