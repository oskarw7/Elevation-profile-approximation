import numpy as np

def cubicSplineIntepolation(xCompute: list[float], xNodes: list[float], yNodes: list[float]) -> list[float]:
    xNodes, yNodes = np.array(xNodes), np.array(yNodes)
    intervalsCount = len(xNodes)-1
    coefficientsCount = intervalsCount*4
    A = np.zeros((coefficientsCount, coefficientsCount))
    b = np.zeros(coefficientsCount)
    row = 0
    for i in range(intervalsCount):
        col = i*4
        # S_j(x_j) = f(x_j) => a_i = f(x_i)
        A[row, col] = 1
        b[row] = yNodes[i]
        row += 1

        # S_j(x_{j+1}) = f(x_{j+1}) => a_i + b_i*h + c_i*h^2 + d_i*h^3 = f(x_{i+1})
        h = xNodes[i+1] - xNodes[i]
        A[row, col:col+4] = [1, h, h**2, h**3]
        b[row] = yNodes[i+1]
        row += 1

        if i < intervalsCount-1:
            # S'_i(x_{i+1}) = S'_{i+1}(x_{i+1}) => b_i + 2*c_i*h + 3*d_i*h^2 = b_{i+1}
            A[row, col+1:col+4] = [1, 2*h, 3*h**2]
            A[row, col+5] = -1
            row += 1

            # S''_i(x_{i+1}) = S''_{i+1}(x_{i+1}) => 2*c_i + 6*d_i*h = 2*c_{i+1}
            A[row, col+2:col+4] = [2, 6*h]
            A[row, col+6] = -2
            row += 1
    # S_0''(x_0) = 0 => c0 = 0
    A[row, 2] = 1
    row += 1

    # S_{n-1}''(x_n) = 0 => 2*c_n + 6*d_n * h = 0
    h = xNodes[-1] - xNodes[-2]
    A[row, coefficientsCount-2] = 2
    A[row, coefficientsCount-1] = 6*h
    row += 1

    coefficients = np.linalg.solve(A, b)
    def getValue(i: int, h: float):
        return coefficients[i*4] + coefficients[i*4 + 1]*h + coefficients[i*4 + 2]*h**2 + coefficients[i*4 + 3]*h**3
    yCompute = []
    for x in xCompute:
        for i in range(intervalsCount):
            if xNodes[i] <= x <= xNodes[i+1]:
                h = float(x - xNodes[i])
                yCompute.append(getValue(i, h))
                break
        else:
            yCompute.append(yCompute[-1])
    return yCompute

