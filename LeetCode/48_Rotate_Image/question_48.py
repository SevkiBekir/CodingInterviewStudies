class Solution:
    def swap(self, a, b):
        return b, a

    def rotate(self, matrix: list[list[int]]) -> None:
        """
        Do not return anything, modify matrix in-place instead.
        """

        row_len = len(matrix)

        # first swap up to down
        swap_index = 0
        while swap_index < row_len / 2:
            down_index = row_len - swap_index - 1
            matrix[swap_index], matrix[down_index] = self.swap(matrix[swap_index], matrix[down_index])
            swap_index += 1

        # then swap wrt diagonal
        row_index = 0
        column_index = 0

        while row_index < row_len:
            column_index = row_index + 1
            while column_index < row_len:
                matrix[row_index][column_index], matrix[column_index][row_index] = self.swap(matrix[row_index][column_index], matrix[column_index][row_index])
                column_index += 1

            row_index += 1

        

if __name__ == "__main__":
    solution = Solution()
    matrix = [[1,2,3],[4,5,6],[7,8,9]]
    result = solution.rotate(matrix)
    print(f"matrix: {matrix}")
    matrix = [[5,1,9,11],[2,4,8,10],[13,3,6,7],[15,14,12,16]]
    result = solution.rotate(matrix)
    print(f"matrix: {matrix}")
