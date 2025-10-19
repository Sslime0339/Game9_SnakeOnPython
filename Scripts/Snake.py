from turtle import width
import pygame




bodyPart = [[0, 0], [0, -1], [0, -2]]
Course = [0, -1]

widthMap = 0
hightMap = 0




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
    for i in range(len(bodyPart) - 1, -1, -1):
        if i != 0:
            bodyPart[i] = list(bodyPart[i-1])
        else:
            bodyPart[0][0] += Course[0]
            bodyPart[0][1] += Course[1]
    
    
