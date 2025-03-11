from typing import List
from collections import deque

class Solution:
    def maxAreaOfIsland(self, grid: List[List[int]]) -> int:
        self.directions = [(0, -1), (0, 1), (1, 0), (-1, 0)]
        rows = len(grid)
        cols = len(grid[0])
        seen = [[0 for _ in range(cols)] for _ in range(rows)]

        res = 0
        for r in range(rows):
            for c in range(cols):
                if not seen[r][c] and grid[r][c] == 1:
                    seen[r][c] = True
                    res = max(self.bfs(grid, seen, (r, c)), res)

        return res

    def bfs(self, grid, seen, coords):
        rows = len(grid)
        cols = len(grid[0])

        r, c = coords

        q = deque([(r, c)])

        size = 1
        while q:
            row, col = q.popleft()

            for x, y in self.directions:
                nr, nc = row + x, col + y

                if nr < 0 or nr >= rows or nc < 0 or nc >= cols:
                    continue

                if seen[nr][nc]:
                    continue

                if grid[nr][nc] == 0:
                    continue
                
                q.append((nr, nc))
                size += 1
                seen[nr][nc] = True

        return size
