from typing import List
from collections import deque

class Solution:
    """
    the main quirk about this problem is that you have to first mark all the chests and then you can start the multi-source dfs.
    """
    def islandsAndTreasure(self, grid: List[List[int]]) -> None:
        self.inf = 2 ** 31 - 1
        self.directions = [(0, -1), (0, 1), (-1, 0), (1, 0)] 
        self.rows, self.cols = len(grid), len(grid[0])

        rows, cols, directions = self.rows, self.cols, self.directions
        seen = [[False for _ in range(cols)] for _ in range(rows)]

        q = deque()

        for r in range(rows):
            for c in range(cols):
                if grid[r][c] == 0 and not seen[r][c]:
                    seen[r][c] = True
                    q.append((r, c, 0))

        while q:
            r, c, distance = q.popleft()

            grid[r][c] = distance

            distance += 1

            for dr, dc in directions:
                nr, nc = r + dr, c + dc

                if nr < 0 or nr >= rows:
                    continue

                if nc < 0 or nc >= cols:
                    continue

                if grid[nr][nc] == -1:
                    continue

                if grid[nr][nc] == 0:
                    continue

                if seen[nr][nc]:
                    continue

                seen[nr][nc] = True

                q.append((nr, nc, distance))

print(Solution().islandsAndTreasure([[2147483647,-1,0,2147483647],[2147483647,2147483647,2147483647,-1],[2147483647,-1,2147483647,-1],[0,-1,2147483647,2147483647]]))
