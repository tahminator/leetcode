from typing import List

class Solution:
    def subsetsWithDup(self, nums: List[int]) -> List[List[int]]:
        res = []
        nums.sort()
        self.backtrack(res, nums, [])
        return res

    def backtrack(self, res, nums, ans):
        if len(nums) < 0:
            return

        res.append(list(ans))

        prev = -10000
        for i in range(len(nums)):
            num = nums[i]

            if prev == num:
                continue

            ans.append(num)
            self.backtrack(res, nums[i + 1:], ans)
            ans.pop()
            prev = num

# print(Solution().subsetsWithDup([1,2,2]))
# print(Solution().subsetsWithDup([4,4,4,1,4]))
