


class Vector2D:

    x = 0
    y = 0


    def __init__(self, x=0, y=0):
        self.x = x
        self.y = y


    def __setitem__(self, k, v):
        if k == 0:
            self.x = v
        elif k == 1:
            self.y = v
        else: 
            print('Ошибка --------------------------------------')

    def __getitem__(self, k):
        if k == 0:
            return self.x
        elif k == 1:
            return self.y
        else: 
            print('Ошибка --------------------------------------')

