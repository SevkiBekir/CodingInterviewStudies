class Solution:

    def setZeroes(self, matrix: list[list[int]]) -> None:
        """
        Do not return anything, modify matrix in-place instead.
        """
        row_len = len(matrix)
        column_len = len(matrix[0])

        allZeroList = self.findAllZeros(matrix)

        for zero_row,zero_column in allZeroList:
            self.doZeroColumn(matrix, zero_column)
            self.doZeroRow(matrix,zero_row)

    
    def findAllZeros(self, matrix: list[list[int]]) -> list[list[int]]:
        row_len = len(matrix)
        allZeroList = []
        for row_index in range(row_len):
            column_len = len(matrix[row_index])
            for column_index in range(column_len):
                if matrix[row_index][column_index] == 0:
                    allZeroList.append([row_index,column_index])

        return allZeroList


    def doZeroColumn(self, matrix, columnIndex):
        for rowIndex in range(len(matrix)):
            matrix[rowIndex][columnIndex] = 0

    def doAllZeroColumns(self, matrix, columnList):
        for columnIndex in columnList:
            self.doZeroColumn(matrix,columnIndex)


    def doZeroRow(self, matrix,rowIndex):
        columnCount = len(matrix[rowIndex])
        zeroRow = [0] * columnCount
        matrix[rowIndex] = zeroRow
   

    def doAllZeroRows(self, matrix, rowList):
        for rowIndex in rowList:
            self.doZeroRow(matrix,rowIndex)
        

        

if __name__ == "__main__":
    solution = Solution()
    matrix = [[1,1,1],[1,0,1],[1,1,1]]
    result = solution.setZeroes(matrix)
    print(f"matrix: {matrix}")
    matrix = [[0,1,2,0],[3,4,5,2],[1,3,1,5]]
    result = solution.setZeroes(matrix)
    print(f"matrix: {matrix}")
