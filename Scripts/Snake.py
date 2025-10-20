import random
import pygame




bodyPart = [[0, 0], [0, -1], [0, -2]]
Course = [0, -1]
LastPosition = list(bodyPart[-1])

Length = 0

widthMap = 0
hightMap = 0


Apple = [0, 0]


def NewApple():
    global Apple 
    Apple = [random.randint(0, widthMap-1), random.randint(0, hightMap-1)]


def NewGame():
    global bodyPart, Length, Course
    bodyPart = [[15, 15], [15, 16], [15, 17]]
    Length = 3
    Course = [0, -1]

    NewApple()


def СhangeCourse(course):
    global Course
    if (course == "w"):
        Course = [0, -1]
    if (course == "s"):
        Course = [0, 1]
    if (course == "a"):
        Course = [-1, 0]
    if (course == "d"):
        Course = [1, 0]


def Move():
    global bodyPart, Length
    LastPosition = list(bodyPart[-1])
    for i in range(len(bodyPart) - 1, -1, -1):
        if i != 0:
            bodyPart[i] = list(bodyPart[i-1])
        else:
            bodyPart[0][0] += Course[0]
            bodyPart[0][1] += Course[1]
    
    if bodyPart[0] == Apple:
        bodyPart += [list(LastPosition)]
        Length += 1
        NewApple()

    if IsDeath():
        NewGame()

def IsDeath():
    for i in range(1, len(bodyPart)):
        if bodyPart[0] == bodyPart[i]:
            return True
    if bodyPart[0][0] < 0 or bodyPart[0][0] >= widthMap or bodyPart[0][1] < 0 or bodyPart[0][1] >= hightMap:
        return True
    return False    
