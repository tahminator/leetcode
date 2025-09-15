from typing import List

class Solution:
    """
    rules:
        1. array doesn't have to be unique 
        2. subarray does have to be unique 
        3. score equals to sum(subarray)

    solution:
        my best course of action would be to use a type of sliding window.
        i can keep track of my current seen, and every time i can add a number, compare with my current maximum
        and when im doing sliding the window all the way to the end, just return the max score

    example:
        [5,2,1,2,5,2,1,2,5]
         lr
         l r                  count = 7, max = 7
         l   r                count = 8, max = 8
         l     r
           l   r
             l r              count = 3, max = 8
             l   r            count = 8, max = 8
             l     r
               l   r
                 l r          count = 7
    """
    def maximumUniqueSubarray(self, nums: List[int]) -> int:
        l, r = 0, 0
        seen = set()
        count, res = 0, 0

        while r < len(nums):
            if nums[r] in seen:
                seen.remove(nums[l])
                count -= nums[l]
                l += 1
                continue

            seen.add(nums[r])
            count += nums[r]
            res = max(res, count)
            r += 1

        return res
