from typing import List
from collections import deque

class Solution:
    def permute(self, nums: List[int]) -> List[List[int]]:
        res = []
        self.backtrack(res, [], nums)
        return res

    def backtrack(self, res, ans, nums):
        if len(nums) == 0:
            res.append(list(ans))
            return

        for i in range(len(nums)):
            ans.append(nums[i])
            self.backtrack(res, ans, nums[:i] + nums[i + 1:])
            ans.pop()

print(Solution().permute([1,2,3]))
