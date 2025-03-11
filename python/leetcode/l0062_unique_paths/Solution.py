class Solution:
    def uniquePaths(self, m: int, n: int) -> int:
        self.directions = [(0, 1), (1, 0)]
        paths = [0]

        self.dfs(paths, m, n, (0, 0))

        return paths[0]

    def dfs(self, paths, m, n, coord):
        r, c = coord

        if (r < 0 or r >= m or c < 0 or c >= n):
            return

        if (r == m - 1 and c == n - 1):
            paths[0] += 1
            return

        for x, y in self.directions:
            nr, nc = r + x, c + y
            
            self.dfs(paths, m, n, (nr, nc))

