import matplotlib.pyplot as plt

def plotOriginal(x: list[float], y: list[float], filename: str):
    plt.figure(figsize=(15, 10))
    plt.plot(x, y, color='blue')
    plt.title(f"Dane wejściowe dla {filename}", fontsize=25)
    plt.xlabel("Odległość[m]", fontsize=25)
    plt.ylabel("Wysokość[m]", fontsize=25)
    plt.tick_params(axis='both', which='major', labelsize=25)
    name = filename.rsplit('.', 1)[0]
    plt.savefig(f"charts/input_{name}.png")

def plotInterpolation(axes, xPoints: list[float], yPoints: list[float], yInterpolation: list[float],
                      xNodes: list[float], yNodes: list[float], method: str, nodesCount: int):
    axes.semilogy(xPoints, yPoints, color='blue')
    axes.semilogy(xPoints, yInterpolation, color='green')
    axes.scatter(xNodes, yNodes, marker='o', color='green')
    axes.set_title(f"Wykres metody {method} dla {nodesCount} węzłów")
    axes.set_xlabel("Odległość[m]")
    axes.set_ylabel("Wysokość[m]")
    axes.legend(["Funkcja wejściowa", "Funkcja interpolująca", "Węzły interpolacyjne"])
