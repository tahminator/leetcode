from typing import List
from collections import deque

"""
We are going to need to first calculate all the oranges that are on the board.
Then, when we find a rotten orange, we can continue with traditional multi-source BFS.
For every time we check the neighbors of the given cell, we can increment the time by 1.
We can use a list[int] with a length of 2 to update the minutes & the rotted oranges. Once we finish scanning the 
matrix, we can return the time if the number of rotted oranges equal to our initial count of all oranges, else -1.
"""

class Solution:
    def orangesRotting(self, grid: List[List[int]]) -> int:
        directions = [(0, 1), (0, -1), (1, 0), (-1, 0)]
        rows, cols = len(grid), len(grid[0])
        seen = [[False for _ in range(cols)] for _ in range (rows)]
        freshOranges = 0
        minutes = 0

        q = deque()

        for r in range(rows):
            for c in range(cols):
                if grid[r][c] == 2:
                    seen[r][c] = True
                    q.append((r, c))

                if grid[r][c] == 1:
                    freshOranges += 1

        if freshOranges == 0:
            return 0

        while q:
            size = len(q)

            for i in range(size):
                row, col = q.popleft()

                for x, y in directions:
                    nr, nc = row + x, col + y

                    if nr < 0 or nr >= rows or nc < 0 or nc >= cols:
                        continue

                    if seen[nr][nc]:
                        continue

                    if grid[nr][nc] == 0:
                        continue
                    
                    grid[nr][nc] = 2
                    seen[nr][nc] = True
                    freshOranges -= 1
                    q.append((nr, nc))

            minutes += 1

        # Adds minutes one more than it should before it exits out of the loop.
        return minutes - 1 if freshOranges == 0 else -1

print(Solution().orangesRotting([[0]]))


