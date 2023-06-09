class Solution:
    def setZeroes(self, matrix: List[List[int]]) -> None:
        """
        Do not return anything, modify matrix in-place instead.
        """
        to_modify = []
        for i in range(len(matrix)):
            for j in range(len(matrix[0])):
                if matrix[i][j] == 0:
                    to_modify.append((i,j))
        for k in to_modify:
            x = k[0]
            y = k[1]
            for i in range(len(matrix)):
                matrix[i][y] = 0
            for j in range(len(matrix[0])):
                matrix[x][j] = 0
