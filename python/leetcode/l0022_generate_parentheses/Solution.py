from typing import List

class Solution:
    def generateParenthesis(self, n: int) -> List[str]:
        res = []
        self.backtrack(res, "", n, 0, 0)
        return res

    def backtrack(self, res, ans, n, left, right):
        if len(ans) / 2 == n:
            res.append(ans)
            return

        if left < n:
            self.backtrack(res, ans + "(", n, left + 1, right)

        if right < left:
            self.backtrack(res, ans + ")", n, left, right + 1)


# print(Solution().generateParenthesis(3))
