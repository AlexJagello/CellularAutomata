import numpy
import pygame
from pygame import gfxdraw





def createNewCellularArray(cellularArray, columnSize_, rowSize_):
    newCellularArray = numpy.zeros((columnSize_, rowSize_))
    for i in range(columnSize_):
        for j in range(rowSize_):
            newCellularArray[i][j] = checkRules_DayAndNight(cellularArray, i, j)
    return newCellularArray


def calculateLifeCellularNear(cellularArray, x, y):
    i = 0
    if cellularArray[x + 1][y + 1]:
        i += 1
    if cellularArray[x + 1][y]:
        i += 1
    if cellularArray[x][y + 1]:
        i += 1
    if cellularArray[x - 1][y - 1]:
        i += 1
    if cellularArray[x - 1][y]:
        i += 1
    if cellularArray[x][y - 1]:
        i += 1
    if cellularArray[x - 1][y + 1]:
        i += 1
    if cellularArray[x + 1][y - 1]:
        i += 1
    return i


def checkRules_Life(cellularArray, x, y):
    if x == 0 or y == 0 or x >= len(cellularArray) - 2 or y >= len(cellularArray) - 2:
        return False

    i = calculateLifeCellularNear(cellularArray, x, y)
    if i > 3 or i < 2:
        return False
    elif i == 3:
        return True
    elif i == 2 and cellularArray[x][y]:
        return True
    else:
        return False


def checkRules_HighLife(cellularArray, x, y):
    if x == 0 or y == 0 or x >= len(cellularArray) - 2 or y >= len(cellularArray) - 2:
        return False

    i = calculateLifeCellularNear(cellularArray, x, y)

    if i == 3 or i == 6:
        return True
    elif i == 2 and cellularArray[x][y]:
        return True
    else:
        return False


def checkRules_DayAndNight(cellularArray, x, y):
    if x == 0 or y == 0 or x >= len(cellularArray) - 2 or y >= len(cellularArray) - 2:
        return False

    i = calculateLifeCellularNear(cellularArray, x, y)
    if i == 3 or i == 6 or i == 7 or i == 8:
        return True
    elif i == 4 and cellularArray[x][y]:
        return True
    else:
        return False


def checkRules_Seeds(cellularArray, x, y):
    if x == 0 or y == 0 or x >= len(cellularArray) - 2 or y >= len(cellularArray) - 2:
        return False

    i = calculateLifeCellularNear(cellularArray, x, y)

    if i == 2 and cellularArray[x][y] == False:
        return True
    else:
        return False


