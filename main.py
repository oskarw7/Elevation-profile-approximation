import utils
import charts
import lagrange

def main():
    paths = [("MountEverest.csv", ","), ("chelm.txt", " "), ("genoa_rapallo.txt", " "), ("WielkiKanionKolorado.csv", ",")]
    nodesCount = [5, 10, 15, 20]
    for path in paths:
        x, y = utils.readData(f"input/{path[0]}", path[1])
        xSubset, ySubset = utils.dataSubset(x, y, 512)
        xScaled, yScaled = utils.scaleTo(xSubset, xSubset[0], xSubset[-1]), ySubset
        xNodes, yNodes = lagrange.getInterpolationNodes(xScaled, yScaled,30, lagrange.linspace)
        yTest = lagrange.lagrangeInterpolation(xScaled, xNodes, yNodes)
        charts.plotOriginal(xSubset, ySubset, path[0])


if __name__ == '__main__':
    main()
