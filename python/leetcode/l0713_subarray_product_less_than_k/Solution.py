from typing import List

class Solution:
    def numSubarrayProductLessThanK(self, nums: List[int], k: int) -> int:
        if k == 0 or k == 1:
            return 0

        l = 0
        res = 0
        product = 1

        for r in range(len(nums)):
            product *= nums[r]

            while product >= k:
                # integer div wouldn't hurt, but to remove 
                # some integer from a integer that was initially 
                # multiplied with some other integer(s) will inherently 
                # equal to an integer number
                product /= nums[l]
                l += 1

            res += (r - l + 1)
            r += 1

        return res

print(Solution().numSubarrayProductLessThanK([10,5,2,6], 100))

