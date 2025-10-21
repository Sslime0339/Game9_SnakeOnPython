from turtle import position
from Scripts.Vector2D import Vector2D


class Apple:

    Position = Vector2D()

    def __init__(self, position):
        if isinstance(position, Vector2D):
            self.Position = position


