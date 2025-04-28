import csv
import math
from typing import Callable


def readData(filename: str, separator: str) -> tuple[list[float], list[float]]:
    x = []
    y = []
    with open(filename, 'r') as file:
        if filename.endswith('.csv'):
            csvReader = csv.reader(file, delimiter=separator)
            for line in csvReader:
                x.append(float(line[0].strip()))
                y.append(float(line[1].strip()))
        elif filename.endswith('.txt'):
            for line in file:
                splitted = line.strip().split(separator)
                x.append(float(splitted[0]))
                y.append(float(splitted[1]))
    return x, y

def dataSubset(x: list[float], y: list[float], subsetSize: int) -> tuple[list[float], list[float]]:
    if subsetSize >= len(x):
        return x, y
    step = len(x) // subsetSize
    return x[::step], y[::step]

def scaleTo(x: list[float], a: float, b: float) -> list[float]:
    return [2 * (xi-a) / (b-a) - 1 for xi in x]

def scaleFrom(x: list[float], a: float, b: float) -> list[float]:
    return [(b-a) * (xi+1) / 2 + a for xi in x]

def linspace(a: float, b: float, N: int) -> list[float]:
    arr = []
    for i in range(N):
        arr.append(a + (b-a)*i / (N-1))
    return arr

def chebyshev(a: float, b: float, N: int) -> list[float]:
    arr = []
    for i in range(N):
        arr.append((a+b)/2 + (b-a)/2 * math.cos(math.pi*i / (N-1)))
    return arr[::-1]

def getInterpolationNodes(xPoints: list[float], yPoints: list[float], nodesCount: int,
                          method: Callable[[float, float, int], list[float]]) -> tuple[list[float], list[float]]:
    realNodes = method(xPoints[0], xPoints[-1], nodesCount)
    xDiscrete = []
    yDiscrete = []
    for node in realNodes:
        index = 0
        min_distance = abs(xPoints[0] - node)
        for i in range(1, len(xPoints)):
            distance = abs(xPoints[i] - node)
            if distance < min_distance:
                min_distance = distance
                index = i
        if xPoints[index] not in xDiscrete:
            xDiscrete.append(xPoints[index])
            yDiscrete.append(yPoints[index])
    return xDiscrete, yDiscrete
