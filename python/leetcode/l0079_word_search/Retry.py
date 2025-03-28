from typing import List

class Solution:
    """
    wanted to retry this problem after having learned backtracking properly.
    """
    def exist(self, board: List[List[str]], word: str) -> bool:
        self.rows = len(board)
        self.cols = len(board[0])
        self.directions = [(0, -1), (0, 1), (-1, 0), (1, 0)]

        rows, cols = self.rows, self.cols

        for r in range(rows):
            for c in range(cols):
                if self.dfs(board, word, "", (r, c)):
                    return True

        return False


    def dfs(self, board, word, ans, coord):
        rows, cols = self.rows, self.cols
        directions = self.directions

        if word == "":
            return True

        r, c = coord

        if r < 0 or r >= rows:
            return False

        if c < 0 or c >= cols:
            return False

        if board[r][c] != word[0]:
            return False

        orig = board[r][c]
        board[r][c] = "#"
        for dr, dc in directions:
            nr, nc = r + dr, c + dc

            if self.dfs(board, word[1:], ans + orig, (nr, nc)):
                return True

        board[r][c] = orig
        return False

# print(Solution().exist([["A","B","C","E"],["S","F","C","S"],["A","D","E","E"]], "ABCCED"))
# print(Solution().exist([["A","B","C","E"],["S","F","C","S"],["A","D","E","E"]], "ABCB"))
# print(Solution().exist([["a","a","a","a"],["a","a","a","a"],["a","a","a","a"]], "aaaaaaaaaaaaa"))
