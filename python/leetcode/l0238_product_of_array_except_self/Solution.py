from typing import List

class Solution:
    """
    example:
        nums = [1,2,3,4]
        res = [24,12,8,6]

        nums = [2,2,3,4]
        res = [24,24,16,12]
        prefix = [2,4,12,48]
        postfix = [48,24,12,4]
    """
    def productExceptSelf(self, nums: List[int]) -> List[int]:
        n = len(nums)
        prefix = self.calculatePrefixArray(nums)
        postfix = self.calculatePostfixArray(nums)

        res = []

        for i in range(n):
            prefixValue = prefix[i - 1] if i != 0 else 1
            postfixValue = postfix[i + 1] if i != n - 1 else 1

            ans = prefixValue * postfixValue

            res.append(ans)

        return res

        
    def calculatePrefixArray(self, nums: List[int]) -> List[int]:
        n = len(nums)
        res = [nums[0]]

        for i in range(1, n):
            num = nums[i]
            res.append(res[i - 1] * num)

        return res

    def calculatePostfixArray(self, nums: List[int]) -> List[int]:
        n = len(nums)
        res = [0] * n
        res[n - 1] = nums[n - 1]

        for i in range(n - 2, -1, -1):
            num = nums[i]
            res[i] = res[i + 1] * num

        return res

print(Solution().productExceptSelf([2,2,3,4]))
