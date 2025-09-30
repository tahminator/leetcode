class Solution:
    # match on words if we use the vowels as a "crutch"
    def vowelHelper(self, word: str) -> str:
        vowels = ("a", "e", "i", "o", "u")
        res = []
        for c in word:
            cl = c.lower()
            if cl in vowels:
                res.append("*")
            else:
                res.append(cl)
        return "".join(res)

    def spellchecker(self, wordlist: List[str], queries: List[str]) -> List[str]:
        """
        worst problem description i have ever seen. in short, they are asking the following for each query:

        1. if the query has a perfect match, return the exact query.
        2. if the query matches with case insensitivity, return first match (so go in order).
        3. if the query has a match with failures being replaced with any of the 5 vowels, return first match (go in order).
        """
        perfectWords = set(wordlist)
        caseInsensitiveWords = {}
        vowelWords = {}
        res = []

        for word in wordlist:
            lw = word.lower()
            if lw not in caseInsensitiveWords:
                caseInsensitiveWords[lw] = word

        for word in wordlist:
            output = self.vowelHelper(word)
            if output not in vowelWords:
                vowelWords[output] = word

        for query in queries:
            if query in perfectWords:
                res.append(query)
                continue

            lq = query.lower()
            if lq in caseInsensitiveWords:
                res.append(caseInsensitiveWords[lq])
                continue

            output = self.vowelHelper(query)
            if output in vowelWords:
                res.append(vowelWords[output])
                continue

            res.append("")

        return res
