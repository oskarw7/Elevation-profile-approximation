import matplotlib.pyplot as plt

def plotOriginal(x: list[float], y: list[float], filename: str):
    plt.figure(figsize=(25, 10))
    plt.plot(x, y, marker='o', markersize=3)
    plt.title(f"Dane wejściowe dla {filename}")
    plt.xlabel("Dystans[m]")
    plt.ylabel("Wysokość[m]")
    plt.show()