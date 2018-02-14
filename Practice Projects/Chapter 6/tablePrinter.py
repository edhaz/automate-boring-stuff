tableData = [['apples', 'oranges', 'cherries', 'banana'],
             ['Alice', 'Bob', 'Carol', 'David'],
             ['dogs', 'cats', 'moose', 'goose']]

def printTable(userData):
    colWidths = [0] * len(userData)

    for line in range(len(tableData)):
        for word in range(len(tableData[line])):
            if colWidths[line] <= len(tableData[line][word]):
                colWidths[line] = len(tableData[line][word])
            else:
                colWidths[line] = colWidths[line]

    for numbs in range(len(tableData[0])):
        for i in range(len(tableData)):
            print(tableData[i][numbs].rjust(colWidths[i] + 1), end=" ")
        print()

printTable(tableData)
