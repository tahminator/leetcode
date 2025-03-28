from typing import List
from collections import deque

class TrieNode:
    def __init__(self):
        self.children = {}
        self.word = False

class Trie:
    def __init__(self):
        self.root = TrieNode()

    def addWord(self, word: str):
        cur = self.root
        for c in word:
            if c not in cur.children:
                cur.children[c] = TrieNode()
            cur = cur.children[c]
        cur.word = True


class Solution:
    def findWords(self, board: List[List[str]], words: List[str]) -> List[str]:
        self.rows = len(board)
        self.cols = len(board[0])
        self.directions = [(0, -1), (0, 1), (-1, 0), (1, 0)]

        rows, cols = self.rows, self.cols

        trie = Trie()
        for word in words:
            trie.addWord(word)


        res = []
        for r in range(rows):
            for c in range(cols):
                    self.dfs(trie.root, board, (r, c), "", res)

        return res

    def dfs(self, node, board, coord, word, res):
        directions = self.directions
        rows, cols = self.rows, self.cols

        r, c = coord

        if node.word:
            node.word = False
            res.append(word)

        if r < 0 or r >= rows:
            return

        if c < 0 or c >= cols:
            return

        node = node.children.get(board[r][c])
        if not node:
            return

        current_val = board[r][c]
        board[r][c] = "-1"
        for dr, dc in directions:
            nr, nc = r + dr, c + dc

            self.dfs(node, board, (nr, nc), word + current_val, res)
        board[r][c] = current_val

# print("solution 1:")
# print(Solution().findWords([["a"]], ["a"]))
# print()
# print("solution 2:")
# print(Solution().findWords([["o","a","a","n"],["e","t","a","e"],["i","h","k","r"],["i","f","l","v"]], ["oath", "oei", "pea","eat","rain"]))
