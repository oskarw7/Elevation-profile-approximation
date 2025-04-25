import utils


def main():
    data = utils.readData("input/ostrowa.txt", ",")
    data = utils.dataSubset(data, 512)


if __name__ == '__main__':
    main()
