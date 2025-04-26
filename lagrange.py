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

def getInterpolationNodes(points: list[tuple[float, float]], nodesCount: int,
                          method: Callable[[float, float, int], list[float]]) -> list[tuple[float, float]]:
    realNodes = method(points[0][0], points[-1][0], nodesCount)
    discreteNodes = []
    for node in realNodes:
        def key_func(n: tuple[float, float]):
            return abs(n[0] - node)
        discrete = min(points, key=key_func)
        if discrete not in discreteNodes:
            discreteNodes.append(discrete)
    return discreteNodes