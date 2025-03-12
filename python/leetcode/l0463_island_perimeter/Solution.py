from typing import List
from collections import deque

class Solution:
    def islandPerimeter(self, grid: List[List[int]]) -> int:
        self.directions = [(0, 1), (0, -1), (1, 0), (-1, 0)]

        rows, cols = len(grid), len(grid[0])
        seen = [[False for _ in range(cols)] for _ in range(rows)]
        perimeter = [0] # 0-index is the answer

        for r in range(rows):
            for c in range(cols):
                if not seen[r][c] and grid[r][c] == 1:
                    seen[r][c] = True
                    self.bfs(grid, seen, perimeter, (r, c))

        return perimeter[0]

    def bfs(self, grid, seen, perimeter, coords):
        rows, cols = len(grid), len(grid[0])
        q = deque([coords])

        while q:
            # we don't actually care about the current value whatsoever. We
            # can calculate the perimeter by looking for: out of bounds or water for each direction.
            # Either case will increase the perimeter by 1.

            r, c = q.popleft()

            for x, y in self.directions:
                nr, nc = r + x, c + y

                if nr < 0 or nr >= rows or nc < 0 or nc >= cols:
                    perimeter[0] += 1
                    continue

                if seen[nr][nc]:
                    continue

                if grid[nr][nc] == 0:
                    perimeter[0] += 1
                    continue

                seen[nr][nc] = True
                q.append((nr, nc))

print(Solution().islandPerimeter([[0,1,0,0],[1,1,1,0],[0,1,0,0],[1,1,0,0]]))
