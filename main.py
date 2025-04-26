import utils
import lagrange

def main():
    data = utils.readData("input/ostrowa.txt", ",")
    dataSubset = utils.dataSubset(data, 512)
    dataScaled = utils.scaleTo(dataSubset, dataSubset[0][0], dataSubset[-1][0])
    nodes = lagrange.getInterpolationNodes(dataScaled,30, lagrange.linspace)
    print(nodes)

if __name__ == '__main__':
    main()
