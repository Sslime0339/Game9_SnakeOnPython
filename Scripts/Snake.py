import random
import pygame


class Snake:
    
    def __init__(self):
        self.Length = 3

    bodyPart = [[0, 0], [0, -1], [0, -2]]
    Course = [0, -1]
    LastPosition = list(bodyPart[-1])

    Length = 0

    widthMap = 0
    hightMap = 0


    Apple = [0, 0]


    def NewApple(self):
        self.Apple = [random.randint(0, self.widthMap-1), random.randint(0, self.hightMap-1)]


    def NewGame(self):
        self.bodyPart = [[15, 15], [15, 16], [15, 17]]
        self.Length = 3
        self.Course = [0, -1]
        self.NewApple()


    def СhangeCourse(self, course):
        if (course == "w"):
            self.Course = [0, -1]
        if (course == "s"):
            self.Course = [0, 1]
        if (course == "a"):
            self.Course = [-1, 0]
        if (course == "d"):
            self.Course = [1, 0]


    def Move(self):
        LastPosition = list(self.bodyPart[-1])
        for i in range(len(self.bodyPart) - 1, -1, -1):
            if i != 0:
                self.bodyPart[i] = list(self.bodyPart[i-1])
            else:
                self.bodyPart[0][0] += self.Course[0]
                self.bodyPart[0][1] += self.Course[1]
        
        if self.bodyPart[0] == self.Apple:
            self.bodyPart += [list(LastPosition)]
            self.Length += 1
            self.NewApple()

        if self.IsDeath():
            self.NewGame()

    def IsDeath(self):
        for i in range(1, len(self.bodyPart)):
            if self.bodyPart[0] == self.bodyPart[i]:
                return True
        if self.bodyPart[0][0] < 0 or self.bodyPart[0][0] >= self.widthMap or self.bodyPart[0][1] < 0 or self.bodyPart[0][1] >= self.hightMap:
            return True
        return False    
