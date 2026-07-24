class Solution:
    def searchMatrix(self, matrix: List[List[int]], target: int) -> bool:
        left = 0
        right = len(matrix) * len(matrix[0]) - 1

        while left <= right:
            middle = (left + right) // 2
            middle_value = self.returnValue(middle, matrix)
            
            if middle_value < target:
                left = middle + 1
            elif middle_value > target:
                right = middle - 1
            else:
                return True
        return False

    def returnValue(self, idx: int, matrix: List[List[int]]) -> int:
        row = idx // len(matrix[0])
        col = idx - (row * len(matrix[0]))
        return matrix[row][col]

        