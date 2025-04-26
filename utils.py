import csv


def readData(filename: str, separator: str) -> list[tuple[float, float]]:
    data = []
    with open(filename, 'r') as file:
        if filename.endswith('.csv'):
            csvReader = csv.reader(file, delimiter=separator)
            for line in csvReader:
                x = float(line[0].strip())
                y = float(line[1].strip())
                data.append((x, y))
        elif filename.endswith('.txt'):
            for line in file:
                splitted = line.strip().split(separator)
                x = float(splitted[0])
                y = float(splitted[1])
                data.append((x, y))
    return data

def dataSubset(data : list[tuple[float, float]], subsetSize: int) -> list[tuple[float, float]]:
    if subsetSize >= len(data):
        return data
    step = len(data) // subsetSize
    return data[::step]

def scaleTo(x: list[tuple[float, float]], a: float, b: float) -> list[tuple[float, float]]:
    return [(2 * (xi-a) / (b-a) - 1, yi) for xi, yi in x]

def scaleFrom(x: list[tuple[float, float]], a: float, b: float) -> list[tuple[float, float]]:
    return [((b-a) * (xi+1) / 2 + a, yi) for xi, yi in x]
