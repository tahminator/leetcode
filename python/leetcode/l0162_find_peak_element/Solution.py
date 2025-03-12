from typing import List

"""
We are expected to solve this in O(log(n)) so binary search is the clear winner.
The important part is determining what array to use based off of the neighbors of mid.

This was key to my understanding: if we have m, and m is not a valid local minimum.
This means one of them is larger than m, and one of them is smaller (they cannot be equal because of the constraints of this problem).
Let's say m - 1 is smaller and m + 1 is larger.
If we use the right subarray, we have the exact same odds of finding one as before. This is because the left-most and right-most out of bounds 
part of the original arrays are -inf. Well, we know m is smaller than m + 1, and the right is the exact same situation due to it being at the end of the subarray. So, we have 
the better odd compared to the left of finding any local minima.
"""

class Solution:
    def findPeakElement(self, nums: List[int]) -> int:
        negative_inf = float("-inf")
        l, r = 0, len(nums) - 1

        while l <= r:
            m = (l + r) // 2

            print(l, m, r)

            li, ri = m - 1, m + 1

            if li < 0:
                ln = negative_inf
            else:
                ln = nums[li]

            if ri >= len(nums):
                rn = negative_inf
            else:
                rn = nums[ri]

            if nums[m] > ln and nums[m] > rn:
                return m

            if rn > nums[m]:
                l = m + 1
            else:
                r = m - 1

        return 0

print(Solution().findPeakElement([-2147483648,-2147483647]))
