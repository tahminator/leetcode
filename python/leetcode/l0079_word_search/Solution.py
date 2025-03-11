from typing import List

class Solution:

    """
    This problem will use a form of DFS to try to build the string out. We won't be starting until
    we run into the very first character. Once we do that, we can start DFS on the graph where we look in every
    adjacent cell and see whether or not it's the next valid character. Once we can append a value to the StringBuilder,
    we can mark that cell as visited so we don't come back there by accident.
    """
    def exist(self, board: List[List[str]], word: str) -> bool:
        self.directions = [(0, 1), (0, -1), (1, 0), (-1, 0)]
        rows = len(board)
        cols = len(board[0])
        visited = [[False for c in range(cols)] for r in range(rows)]

        for r in range(rows):
            for c in range(cols):
                if not visited[r][c] and board[r][c] == word[0]:
                    # enter bfs
                    if self.bfs(board, word, visited, (r, c), 0):
                        return True

        return False

    def bfs(self, board, word, visited, coords, index):
        rows = len(board)
        cols = len(board[0])
        r, c = coords

        # match found
        if index == len(word):
            return True

        # out of bounds
        if r < 0 or r >= rows or c < 0 or c >= cols:
            return False

        # already visited
        if visited[r][c]:
            return False

        # if character is not equal
        if board[r][c] != word[index]:
            return False

        visited[r][c] = True
        index += 1

        for x, y in self.directions:
            nr, nc = r + x, c + y

            # yay, bfs done
            if self.bfs(board, word, visited, (nr, nc), index):
                return True

        # If we got to this point, we failed to find a valid word. So, we reset it back so we can use it from a different starting point. 
        visited[r][c] = False

        return False

solution = Solution()
print(solution.exist([["A","B","C","E"],["S","F","C","S"],["A","D","E","E"]], "ABCB"))
