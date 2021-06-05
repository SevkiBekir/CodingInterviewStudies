def printMatrix(matrix):
    print("PRINTING MATRIX")
    for row in matrix:
        print(row)

def getSwapedValues(value1, value2):
    temp = value1
    value1 = value2
    value2 = temp

    return [value1,value2]

def rotateMatrix(matrix):
    # diagonal is the same, then ignore it
    # a b
    # c d

    # After rotate
    # a c
    # b d

    matrixLength = len(matrix)

    #optimization
    # 1x1 matrix
    if matrixLength == 1:
        return matrix


    # NxN matrix
    for column in range(matrixLength):
        for row in range(column+1,matrixLength):
            swappedValues = getSwapedValues(matrix[column][row], matrix[row][column])
            matrix[column][row] = swappedValues[0]
            matrix[row][column] = swappedValues[1]

    return matrix


if __name__ == '__main__':
    matrix = [[0,1,2],[3,4,5],[6,7,8]]
    printMatrix(matrix)

    result = rotateMatrix(matrix)
    printMatrix(result)
