from matplotlib import pyplot



def createChart(x, y):
    pyplot.scatter(x, y, alpha=0.5)
    pyplot.savefig("graph.png")


