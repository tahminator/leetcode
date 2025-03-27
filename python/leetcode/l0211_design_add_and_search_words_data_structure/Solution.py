class TrieNode:
    def __init__(self):
        self.children = {}
        self.word = False

class WordDictionary:

    def __init__(self):
        self.root = TrieNode()

    def addWord(self, word: str) -> None:
        cur = self.root
        for c in word:
            if c not in cur.children:
                cur.children[c] = TrieNode()
            cur = cur.children[c]
        cur.word = True

    def search(self, word: str) -> bool:
        return self.iterative_search(self.root, word)


    def iterative_search(self, root, word):
        cur = root
        for i, c in enumerate(word):
            if c == ".":
                for child in cur.children:
                    subword = word[i + 1::]
                    if self.iterative_search(cur.children[child], subword):
                        return True
                return False
            else:
                if c not in cur.children:
                    return False
                cur = cur.children[c]

        return cur.word

obj = WordDictionary()
obj.addWord("and")
print(obj.search("a"))

# Your WordDictionary object will be instantiated and called as such:
# obj = WordDictionary()
# obj.addWord(word)
# param_2 = obj.search(word)
