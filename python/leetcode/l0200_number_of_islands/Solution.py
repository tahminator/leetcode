from typing import List
from collections import deque

class Solution:
    def numIslands(self, grid: List[List[str]]) -> int:
        self.directions = [(0, 1), (0, -1), (1, 0), (-1, 0)]
        islands = 0
        rows = len(grid)
        cols = len(grid[0])
        seen = [[False for _ in range(cols)] for _ in range(rows)]

        for row in range(rows):
            for col in range(cols):
                if not seen[row][col] and grid[row][col] == "1":
                    islands += 1
                    seen[row][col] = True
                    self.bfs(grid, seen, (row, col))

        return islands

    def bfs(self, grid, seen, coords):
        rows = len(grid)
        cols = len(grid[0])

        q = deque([coords])

        while q:
            r, c = q.popleft()

            for x, y in self.directions:
                nr, nc = r + x, c + y

                if nr < 0 or nr >= rows or nc < 0 or nc >= cols:
                    continue

                if seen[nr][nc]:
                    continue
                
                if grid[nr][nc] == "0":
                    continue

                seen[nr][nc] = True
                q.append((nr, nc))

