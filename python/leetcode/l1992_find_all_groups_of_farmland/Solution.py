from typing import List
from collections import deque

class Solution:
    def findFarmland(self, land: List[List[int]]) -> List[List[int]]:
        """
        the key difference is that we just want to always track the smallest x,y and the largest x,y for the current island.
        """

        self.directions = [(0, 1), (0, -1), (1, 0), (-1, 0)]
        self.rows = len(land)
        self.cols = len(land[0])
        seen = [[False for _ in range(self.cols)] for _ in range(self.rows)]

        res = []
        for r in range(self.rows):
            for c in range(self.cols):
                if land[r][c] == 1 and seen[r][c] is False:
                    res.append(self.dfs(land, seen, (r, c)))

        return res


    def dfs(self, land, seen, start):
        r, c = start
        seen[r][c] = True
        min_x, max_x = c, c
        min_y, max_y = r, r

        q = deque([start])
        while q:
            r, c = q.popleft()
            min_x = min(min_x, c)
            max_x = max(max_x, c)
            min_y = min(min_y, r)
            max_y = max(max_y, r)

            for x, y in self.directions:
                nr, nc = r + y, c + x

                if nr < 0 or nr >= self.rows:
                    continue

                if nc < 0 or nc >= self.cols:
                    continue

                if land[nr][nc] != 1:
                    continue

                if seen[nr][nc]:
                    continue

                seen[nr][nc] = True
                q.append((nr, nc))

        return [min_y, min_x, max_y, max_x]

print(Solution().findFarmland([[1,0,0],[0,1,1],[0,1,1]]))
