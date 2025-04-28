import matplotlib.pyplot as plt
import utils
import charts
import lagrange
import cubic_spline

def main():
    paths = [("MountEverest.csv", ","), ("chelm.txt", " "), ("genoa_rapallo.txt", " "), ("WielkiKanionKolorado.csv", ",")]
    nodesCount = [5, 10, 20, 50]
    for path in paths:
        x, y = utils.readData(f"input/{path[0]}", path[1])
        xSubset, ySubset = utils.dataSubset(x, y, 512)
        xScaled, yScaled = utils.scaleTo(xSubset, xSubset[0], xSubset[-1]), ySubset
        xScaled, yScaled = utils.scaleTo(xSubset, xSubset[0], xSubset[-1]), ySubset
        # charts.plotOriginal(xSubset, ySubset, path[0])
        fig, axes = plt.subplots(len(nodesCount), 3, figsize=(20, 25))
        fig.suptitle(f"Wyniki metod interpolacji dla input/{path[0]}", fontsize=25)
        for i in range(len(nodesCount)):
            xNodes, yNodes = utils.getInterpolationNodes(xScaled, yScaled, nodesCount[i], utils.linspace)
            yTest = lagrange.lagrangeInterpolation(xScaled, xNodes, yNodes)
            xNodesReverseScaled = utils.scaleFrom(xNodes, xSubset[0], xSubset[-1])
            charts.plotInterpolation(axes[i,0], xSubset, ySubset, yTest, xNodesReverseScaled, yNodes, "Lagrange", nodesCount[i])

            xNodes, yNodes = utils.getInterpolationNodes(xScaled, yScaled, nodesCount[i], utils.chebyshev)
            yTest = lagrange.lagrangeInterpolation(xScaled, xNodes, yNodes)
            xNodesReverseScaled = utils.scaleFrom(xNodes, xSubset[0], xSubset[-1])
            charts.plotInterpolation(axes[i,1], xSubset, ySubset, yTest, xNodesReverseScaled, yNodes, "Lagrange + Czebyszew", nodesCount[i])

            xNodes, yNodes = utils.getInterpolationNodes(xSubset, ySubset, nodesCount[i], utils.linspace)
            yTest = cubic_spline.cubicSplineIntepolation(xSubset, xNodes, yNodes)
            charts.plotInterpolation(axes[i,2], xSubset, ySubset, yTest, xNodes, yNodes, "funkcji sklejanych", nodesCount[i])
        plt.show()
        plt.close(fig)


if __name__ == '__main__':
    main()
