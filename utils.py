import numpy as np
import csv

from numpy import ndarray


def scaleTo(x: float, a: float, b: float) -> float:
    return 2 * (x-a) / (b-a) - 1


def scaleFrom(x: float, a: float, b: float) -> float:
    return (b-a) * (x+1) / 2 + a

def readData(filename: str, separator: str) -> ndarray:
    data = []
    with open(filename, 'r') as file:
        if filename.endswith('.csv'):
            csvReader = csv.reader(file, delimiter=separator)
            for line in csvReader:
                x = float(line[0].strip())
                y = float(line[1].strip())
                data.append([x, y])
        elif filename.endswith('.txt'):
            for line in file:
                splitted = line.strip().split(separator)
                x = float(splitted[0])
                y = float(splitted[1])
                data.append([x, y])
    return np.array(data)

def dataSubset(data : ndarray, subsetSize: int) -> ndarray:
    if subsetSize >= data.shape[0]:
        return data
    step = data.shape[0] // subsetSize
    return data[::step]
