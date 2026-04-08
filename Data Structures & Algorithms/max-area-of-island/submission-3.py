class Solution:
    def maxAreaOfIsland(self, grid: List[List[int]]) -> int:
        ROWS, COLS = len(grid), len(grid[0])
        directions = [[1, 0], [-1, 0], [0, 1], [0, -1]]
        max_area = 0

        def dfs(r: int, c: int, visited: set[int, int]) -> int:
            if (r < 0 or c < 0 or r == ROWS or c == COLS or
                grid[r][c] == 0 or (r, c) in visited):
                return 0
            grid[r][c] = 0
            visited.add((r, c))
            area = 0
            for dr, dc in directions:
                area += dfs(r + dr, c + dc, visited)
            
            return area + 1

        for r in range(ROWS):
            for c in range(COLS):
                if grid[r][c] == 1:
                    max_area = max(max_area, dfs(r, c, set()))
        return max_area