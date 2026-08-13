class Solution:
    def countPaths(self, grid: List[List[int]]) -> int:
        ROWS, COLS = len(grid), len(grid[0])
        directions = [[0, 1], [0, -1], [1, 0], [-1, 0]]
        if grid[0][0] or grid[ROWS - 1][COLS - 1]:
            return 0
        
        def dfs(r: int, c: int, visited: set[int, int]) -> int:
            if (r < 0 or c < 0 or r == ROWS or c == COLS or 
               grid[r][c] == 1 or (r, c) in visited):
               return 0
            if r == ROWS - 1 and c == COLS - 1:
                return 1
            visited.add((r, c))
            count = 0
            for dr, dc in directions:
                count += dfs(r + dr, c + dc, visited)
            visited.remove((r, c))

            return count
        
        return dfs(0, 0, set())