def findZeroValues(matrix):
    result = []
    for rowIndex in range(len(matrix)):
        for columnIndex in range(len(matrix[rowIndex])):
            if not matrix[rowIndex][columnIndex]:
                result.append([rowIndex, columnIndex])

    return result


def unifyAllZeroValueIndex(zeroValueIndexList):
    row = []
    column = []
    for indexList in zeroValueIndexList:
        if not indexList[0] in row:
            row.append(indexList[0])
        if not indexList[1] in column:
            column.append(indexList[1])

    result = [row, column]

    return result


def doZeroColumn(matrix, columnIndex):
    for rowIndex in range(len(matrix)):
        matrix[rowIndex][columnIndex] = 0

    return matrix

def doAllZeroColumns(matrix, columnList):
    for columnIndex in columnList:
        matrix = doZeroColumn(matrix,columnIndex)

    return matrix

def doZeroRow(matrix,rowIndex):
    columnCount = len(matrix[rowIndex])
    zeroRow = [0] * columnCount
    matrix[rowIndex] = zeroRow
    return matrix

def doAllZeroRows(matrix, rowList):
    for rowIndex in rowList:
        matrix = doZeroRow(matrix,rowIndex)

    return matrix

def doZeroMatrix(matrix, zeroValueRowColumnList):
    matrix = doAllZeroRows(matrix,zeroValueRowColumnList[0])
    matrix = doAllZeroColumns(matrix,zeroValueRowColumnList[1])

    return matrix

def printMatrix(matrix):
    print("PRINTING MATRIX")
    for row in matrix:
        print(row)


if __name__ == '__main__':
    matrix = [[0, 1], [1, 0]];
    printMatrix(matrix)
    zeroValueIndexList = findZeroValues(matrix)
    print(zeroValueIndexList)
    unifiedZeroValueRowColumnList = unifyAllZeroValueIndex(zeroValueIndexList)
    print(unifiedZeroValueRowColumnList)

    zeroMatrix = doZeroMatrix(matrix,unifiedZeroValueRowColumnList)
    printMatrix(zeroMatrix)
