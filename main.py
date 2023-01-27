import numpy
import pygame
import random
import CellularAutomaton_2D
from pygame import gfxdraw


def drawPixel(x, y, surface, isSelect):
    if isSelect:
        gfxdraw.pixel(surface, x, y, (255, 0, 0))
    else:
        gfxdraw.pixel(surface, x, y, (0, 0, 0))


def launchGame2D(generation, columnSize, rowSize):
    pygame.init()
    pygame.display.set_caption('Cellular')
    window = pygame.display.set_mode((columnSize, rowSize))
    running = True
    while running:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                running = False
        generation = CellularAutomaton_2D.createNewCellularArray(generation, columnSize, rowSize)
        for i in range(columnSize):
            for j in range(rowSize):
                drawPixel(i, j, window, generation[i][j])
        pygame.display.update()


if __name__ == '__main__':
    rowSize = 300
    columnSize = 300

    firstGeneration = numpy.zeros((columnSize, rowSize))
    for column in range(len(firstGeneration)):
        for row in range(len(firstGeneration[column])):
            firstGeneration[column][row] = bool(random.choice([True, False]))

    launchGame2D(firstGeneration, columnSize, rowSize)
