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