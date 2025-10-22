from turtle import position
from Scripts.Vector2D import Vector2D


class Apple:

    Position = Vector2D()

    def __init__(self, position : Vector2D):
        self.Position = position
        # if isinstance(position, Vector2D):
        # else:
        #     print('ошибка: яблоко получило не тот тип данных')

    def __str__(self):
        return f"position: {self.Position}"
