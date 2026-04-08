class Solution:
    def numIslands(self, grid: List[List[str]]) -> int:
        ROWS, COLS = len(grid), len(grid[0])
        count = 0

        def dfs(r, c, visit):
            if (r < 0 or c < 0 or r >= ROWS or c >= COLS or grid[r][c] == "0" or (r, c) in visit):
                return

            grid[r][c] = "0"
            visit.add((r, c))
            dfs(r + 1, c, visit)
            dfs(r - 1, c, visit)
            dfs(r, c + 1, visit)
            dfs(r, c - 1, visit)

            return
        
        for r in range(ROWS):
            for c in range(COLS):
                if grid[r][c] == "1":
                    dfs(r, c, set())
                    count += 1
        print(grid)
        return count
