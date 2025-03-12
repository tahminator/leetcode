"""
You can find this problem on Neetcode.com.
"""

"""
You are given an m x n 2D grid initialized with these three possible values:

-1  -> A water cell that cannot be traversed.
 0  -> A treasure chest.
 INF -> A land cell that can be traversed. We use the integer 2^31 - 1 = 2147483647 to represent INF.

Fill each land cell with the distance to its nearest treasure chest. 
If a land cell cannot reach a treasure chest, the value should remain INF.

The grid can only be traversed up, down, left, or right.

Modify the grid in-place.

Example 1:
Input:
[
  [2147483647, -1, 0, 2147483647],
  [2147483647, 2147483647, 2147483647, -1],
  [2147483647, -1, 2147483647, -1],
  [0, -1, 2147483647, 2147483647]
]

Output:
[
  [3, -1, 0, 1],
  [2, 2, 1, -1],
  [1, -1, 2, -1],
  [0, -1, 3, 4]
]

Example 2:
Input:
[
  [0, -1],
  [2147483647, 2147483647]
]

Output:
[
  [0, -1],
  [1, 2]
]

Constraints:
- m == grid.length
- n == grid[i].length
- 1 <= m, n <= 100
- grid[i][j] is one of {-1, 0, 2147483647}
"""

class Solution:
    def islandsAndTreasure(self, grid: List[List[int]]) -> None:
        self.int_max = (2 ** 31) - 1
        self.directions = [(0, 1), (0, -1), (1, 0), (-1, 0)]

        rows = len(grid)
        cols = len(grid[0])

        for r in range(rows):
            for c in range(cols):
                if grid[r][c] == 0:
                    seen = [[False for _ in range(cols)] for _ in range(rows)]
                    seen[r][c] = True
                    self.bfs(grid, seen, (r, c))

    def bfs(self, grid, seen, coords):
        rows = len(grid)
        cols = len(grid[0])

        q = deque([coords])

        d = 0

        while q:
            r, c = q.popleft()
            current = grid[r][c]
            grid[r][c] = min(current, d)

            d += 1

            for x, y in self.directions:
                nr, nc = r + x, c + y

                if nr < 0 or nr >= rows or nc < 0 or nc >= cols:
                    continue

                if seen[nr][nc]:
                    continue

                if grid[nr][nc] == -1:
                    continue

                if grid[nr][nc] == 0:
                    continue

                seen[nr][nc] = True
                q.append((nr, nc))







