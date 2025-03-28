from typing import List

class Solution:
    def subsets(self, nums: List[int]) -> List[List[int]]:
        res = []
        self.dfs(nums, [], res, -1)
        return res

    def dfs(self, nums, subsets, res, i):
        if i == len(nums) - 1:
            res.append(list(subsets))
            return

        i += 1
        subsets.append(nums[i])
        self.dfs(nums, subsets, res, i)

        subsets.pop()
        self.dfs(nums, subsets, res, i)

print(Solution().subsets([1,2,3]))
