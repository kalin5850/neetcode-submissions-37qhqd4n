class Solution:
    def uniquePathsWithObstacles(self, obstacleGrid: List[List[int]]) -> int:
        ROWS, COLS = len(obstacleGrid), len(obstacleGrid[0])
        if obstacleGrid[0][0] or obstacleGrid[ROWS - 1][COLS - 1]:
            return 0

        new_grid = [[0 for _ in range(COLS + 1)] for _ in range(ROWS + 1)]
        for r in range(ROWS - 1, -1, -1):
            for c in range(COLS - 1, -1, -1):
                if r == ROWS - 1 and c == COLS - 1:
                    new_grid[r][c] = 1
                elif obstacleGrid[r][c] == 1:
                    new_grid[r][c] = 0
                else:
                    new_grid[r][c] = new_grid[r + 1][c] + new_grid[r][c + 1]
        
        return new_grid[0][0]
