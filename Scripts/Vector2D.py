


class Vector2D:

    x = 0
    y = 0


    def new(self):
        return Vector2D(self.x, self.y)

    
    def __init__(self, x=0, y=0):
        '''создание вектора'''
        self.x = x
        self.y = y


    # присвоение self[k] = v
    def __setitem__(self, k, v):
        if k == 0:
            self.x = v
        elif k == 1:
            self.y = v
        else: 
            print('Ошибка --------------------------------------')

    # получить self[k]
    def __getitem__(self, k):
        if k == 0:
            return self.x
        elif k == 1:
            return self.y
        else: 
            print('Ошибка --------------------------------------')

    # Сложение с присваиванием a += b
    def __iadd__(a, b):
        a.x += b.x
        a.y += b.y
        return a
    
    # Сложение a + b
    def __add__(self, other):
        return Vector2D(self.x + other.x, self.y + other.y)
    
    def __eq__(a, b):
        print(((a.x == b.x) and (a.y == b.y)))
        return ((a.x == b.x) and (a.y == b.y))
    
    def __ne__(a, b):
        return not a == b
    
    # преобразовать в строку
    def __str__(self):
        return f"x: {self.x}, y: {self.y}"