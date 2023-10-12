def readColumn(number):
    columnData = []
0    with open("iris.csv", "r") as iris:
        for line in iris.readlines()[1:]:
            data = line.strip().split(",")
            columnData.append(data[number])
    return columnData