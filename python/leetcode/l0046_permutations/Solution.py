from typing import List
from collections import deque

class Solution:
    def permute(self, nums: List[int]) -> List[List[int]]:
        maxrecursion = 0
        for i in range(len(nums), -1, -1):
            maxrecursion += i

        res = []
        self.backtrack(res, [], nums, maxrecursion, len(nums))
        return res

    def backtrack(self, res, ans, nums, maxrecursion, maxlen):
        if maxrecursion == 0:
            res.append(list(ans))
            return

        for i in range(len(nums)):
            num = nums[i]
            ans.append(num)
            self.backtrack(res, ans, nums[i + 1:], maxrecursion - 1, maxlen)
            ans.pop()
            self.backtrack(res, ans, nums[i + 1:] + [nums[i]], maxrecursion - 1, maxlen)

print(Solution().permute([1,2,3]))
