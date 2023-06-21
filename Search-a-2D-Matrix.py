class Solution:
    def searchMatrix(self, matrix: List[List[int]], target: int) -> bool:
        start = 0
        end = (len(matrix)*len(matrix[0]))-1
        while start<=end:
            mid = (start+(end-start)//2)
            if matrix[mid//len(matrix[0])][mid%len(matrix[0])] == target:
                return True
            elif matrix[mid//len(matrix[0])][mid%len(matrix[0])] < target:
                start = mid + 1
            elif matrix[mid//len(matrix[0])][mid%len(matrix[0])] > target:
                end = mid - 1
        return False
