class Solution:
    def searchMatrix(self, matrix: List[List[int]], target: int) -> bool:
        R, C = len(matrix), len(matrix[0])
        l, r = 0, R * C - 1
        while l <= r:
            m = (l + r) // 2
            i, j = m // C, m % C
            if matrix[i][j] < target:
                l = m + 1
            elif matrix[i][j] > target:
                r = m - 1
            else:
                return True
        
        return False