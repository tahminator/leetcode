from typing import List

class Solution:
    def longestNiceSubarray(self, nums: List[int]) -> int:
        """
        This is very similar to finding the longest k-length substring with unique characters.
        In this case, we need to keep a set of all the values that can be part of this subarray, and the 
        important part is that if we encounter a value that isn't valid, we keep moving our pointer left until 
        that is no longer the case. If we find a valid value, we keep moving right.
        """

        if len(nums) == 1:
            return 1

        l = 0
        bits = 0
        maxlen = 1 # minimum nice subarray

        for r in range(len(nums)):
            while bits & nums[r] != 0:
                bits ^= nums[l]
                l += 1

            bits |= nums[r]
            maxlen = max(maxlen, r - l + 1)

        return maxlen


print(Solution().longestNiceSubarray([1,3,8,48,10]))
