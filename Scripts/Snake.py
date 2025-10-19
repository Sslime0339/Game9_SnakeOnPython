import pygame




bodyPart = [[0, 0]]


def Move(course):
    if (course == "w"):
        bodyPart[0][1] -= 1
    if (course == "s"):
        bodyPart[0][1] += 1
    if (course == "a"):
        bodyPart[0][0] -= 1
    if (course == "d"):
        bodyPart[0][0] += 1