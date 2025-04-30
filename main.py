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
        charts.plotOriginal(xSubset, ySubset, path[0])

        fig, axes = plt.subplots(len(nodesCount)//2, len(nodesCount)//2, figsize=(15, 12))
        fig.suptitle(f"Wyniki interpolacji Lagrange'a dla {path[0]}", fontsize=20)
        for i in range(len(nodesCount)):
            xNodes, yNodes = utils.getInterpolationNodes(xScaled, yScaled, nodesCount[i], utils.linspace)
            yTest = lagrange.lagrangeInterpolation(xScaled, xNodes, yNodes)
            xNodesReverseScaled = utils.scaleFrom(xNodes, xSubset[0], xSubset[-1])
            row = i // 2
            col = i % 2
            charts.plotInterpolation(axes[row, col], xSubset, ySubset, yTest, xNodesReverseScaled, yNodes,
                                     "Lagrange", nodesCount[i])
        name = path[0].rsplit('.', 1)[0]
        plt.savefig(f"charts/lagrange_{name}.png")
        plt.close(fig)

        fig, axes = plt.subplots(len(nodesCount) // 2, len(nodesCount) // 2, figsize=(15, 12))
        fig.suptitle(f"Wyniki interpolacji Lagrange'a + Czebyszew dla {path[0]}", fontsize=20)
        for i in range(len(nodesCount)):
            xNodes, yNodes = utils.getInterpolationNodes(xScaled, yScaled, nodesCount[i], utils.chebyshev)
            yTest = lagrange.lagrangeInterpolation(xScaled, xNodes, yNodes)
            xNodesReverseScaled = utils.scaleFrom(xNodes, xSubset[0], xSubset[-1])
            row = i // 2
            col = i % 2
            charts.plotInterpolation(axes[row, col], xSubset, ySubset, yTest, xNodesReverseScaled, yNodes,
                                     "Lagrange+Czebyszew", nodesCount[i])
        name = path[0].rsplit('.', 1)[0]
        plt.savefig(f"charts/chebyszev_{name}.png")
        plt.close(fig)

        fig, axes = plt.subplots(len(nodesCount) // 2, len(nodesCount) // 2, figsize=(15, 12))
        fig.suptitle(f"Wyniki interpolacji funkcjami sklejanymi dla {path[0]}", fontsize=20)
        for i in range(len(nodesCount)):
            xNodes, yNodes = utils.getInterpolationNodes(xSubset, ySubset, nodesCount[i], utils.linspace)
            yTest = cubic_spline.cubicSplineIntepolation(xSubset, xNodes, yNodes)
            row = i // 2
            col = i % 2
            charts.plotInterpolation(axes[row, col], xSubset, ySubset, yTest, xNodes, yNodes,
                                     "funkcji sklejanych", nodesCount[i])
        name = path[0].rsplit('.', 1)[0]
        plt.savefig(f"charts/cubic_spline_{name}.png")
        plt.close(fig)

        fig, axes = plt.subplots(len(nodesCount), 3, figsize=(20, 25))
        fig.suptitle(f"Wyniki metod interpolacji dla {path[0]}", fontsize=20)
        for i in range(len(nodesCount)):
            xNodes, yNodes = utils.getInterpolationNodes(xScaled, yScaled, nodesCount[i], utils.linspace)
            yTest = lagrange.lagrangeInterpolation(xScaled, xNodes, yNodes)
            xNodesReverseScaled = utils.scaleFrom(xNodes, xSubset[0], xSubset[-1])
            charts.plotInterpolation(axes[i,0], xSubset, ySubset, yTest, xNodesReverseScaled, yNodes,
                                     "Lagrange", nodesCount[i])

            xNodes, yNodes = utils.getInterpolationNodes(xScaled, yScaled, nodesCount[i], utils.chebyshev)
            yTest = lagrange.lagrangeInterpolation(xScaled, xNodes, yNodes)
            xNodesReverseScaled = utils.scaleFrom(xNodes, xSubset[0], xSubset[-1])
            charts.plotInterpolation(axes[i,1], xSubset, ySubset, yTest, xNodesReverseScaled, yNodes,
                                     "Lagrange + Czebyszew", nodesCount[i])

            xNodes, yNodes = utils.getInterpolationNodes(xSubset, ySubset, nodesCount[i], utils.linspace)
            yTest = cubic_spline.cubicSplineIntepolation(xSubset, xNodes, yNodes)
            charts.plotInterpolation(axes[i,2], xSubset, ySubset, yTest, xNodes, yNodes,
                                     "funkcji sklejanych", nodesCount[i])
        name = path[0].rsplit('.', 1)[0]
        plt.savefig(f"charts/comparison_{name}.png")
        plt.close(fig)


if __name__ == '__main__':
    main()
