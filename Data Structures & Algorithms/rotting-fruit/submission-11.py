class Solution:
    def orangesRotting(self, grid: List[List[int]]) -> int:
        directions = [[1, 0], [-1, 0], [0, 1], [0, -1]]
        ROWS, COLS = len(grid), len(grid[0])
        q, visited = deque(), set()
        result = 0

        def bfs(q, visited):
            count = 0
            while q:
                print(q)
                for _ in range(len(q)):
                    rx, cx, start = q.popleft()
                    for dr, dc in directions:
                        r, c = rx + dr, cx + dc
                        if (min(r, c) < 0 or r == ROWS or c == COLS or 
                            grid[r][c] == 0 or grid[r][c] == 2 or (r, c) in visited):
                            continue
                        q.append((r, c, 0))
                        visited.add((r, c))
                        grid[r][c] = 2
                if not start:
                    count += 1
            print(count)
            return count


        for r in range(ROWS):
            for c in range(COLS):
                if grid[r][c] == 2:
                    q.append((r, c, 1))
                    visited.add((r, c))
        result = bfs(q, visited)
        print(grid)
        for r in range(ROWS):
            for c in range(COLS):
                if grid[r][c] == 1:
                    return -1

        return result

