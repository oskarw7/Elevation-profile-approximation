import csv


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
