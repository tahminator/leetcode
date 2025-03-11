from typing import List

"""
Given the robot, we can likely apply DFS and attempt to create unique paths to the end.
Every time we reach the end, we just increment our paths by 1. Return that value at the end.

DFS is too slow. Come back to this and do it with DP.
"""
class Solution:
    def uniquePathsWithObstacles(self, obstacleGrid: List[List[int]]) -> int:
        self.directions = [(0, 1), (1, 0)] # right, down
        
        paths = [0] # 0-index is the answer
        self.dfs(obstacleGrid, paths, (0, 0))

        return paths[0]


    def dfs(self, grid, paths, pos):
        r, c = pos

        if (r < 0 or r >= len(grid) or c < 0 or c >= len(grid[0])):
            return

        if grid[r][c] == 1:
            return

        if r == len(grid) - 1 and c == len(grid[0]) - 1:
            paths[0] += 1
            return

        for x, y in self.directions:
            nr, nc = r + x, c + y

            self.dfs(grid, paths, (nr, nc))

print(Solution().uniquePathsWithObstacles([[0,0],[0,1]]))
