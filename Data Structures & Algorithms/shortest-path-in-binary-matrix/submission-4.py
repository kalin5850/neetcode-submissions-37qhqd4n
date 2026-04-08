class Solution:
    def shortestPathBinaryMatrix(self, grid: List[List[int]]) -> int:
        directions = [[1, 0], [-1, 0], [0, 1], [0, -1],
                      [1, 1], [-1, -1], [1, -1], [-1, 1]]
        ROWS, COLS = len(grid), len(grid[0])
        q, visited = deque(), set((0, 0))
        q.append((0, 0))
        path = 1

        if grid[0][0] or grid[ROWS - 1][COLS - 1]:
            return -1

        while q:
            for _ in range(len(q)):
                r, c = q.popleft()
                if r == ROWS - 1 and c == COLS - 1:
                    return path
                for dr, dc in directions:
                    r, c = r + dr, c + dc
                    if (0 <= r < ROWS and 0 <= c < COLS and 
                        grid[r][c] != 1 and (r, c) not in visited):
                        q.append((r, c))
                        visited.add((r, c))
            path += 1

        return -1

