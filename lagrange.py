import math
from typing import Callable


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
        def key_func(i):
            return abs(xPoints[i]-node)
        index = min(range(len(xPoints)), key=key_func)
        if xPoints[index] not in xDiscrete:
            xDiscrete.append(xPoints[index])
            yDiscrete.append(yPoints[index])
    return xDiscrete, yDiscrete

def lagrangeInterpolation(xCompute: list[float], xNodes: list[float], yNodes: list[float]) -> list[float]:
    yCompute = []
    for x in xCompute:
        yCurrent = 0
        for i in range(len(xNodes)):
            xi, yi = xNodes[i], yNodes[i]
            phi = 1
            for j in range(len(xNodes)):
                if i != j:
                    xj = xNodes[j]
                    phi *= (x-xj) / (xi-xj)
            yCurrent += yi*phi
        yCompute.append(yCurrent)
    return yCompute