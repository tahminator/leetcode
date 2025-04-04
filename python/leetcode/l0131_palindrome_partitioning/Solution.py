class Solution:
    def isPalindrome(self, s):
        if len(s) == 1:
            return True

        l, r = 0, len(s) - 1

        while l <= r:
            if s[l] != s[r]:
                return False
            l += 1
            r -= 1

        return True

    def partition(self, s: str) -> List[List[str]]:
        res = []
        self.backtrack(s, [], res)
        return res

    def backtrack(self, s, ans, res):
