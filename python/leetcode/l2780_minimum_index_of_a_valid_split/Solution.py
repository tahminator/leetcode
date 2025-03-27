from typing import List

class Solution:
    def minimumIndex(self, nums: List[int]) -> int:
        "boyer-moore, sliding window-like"
        majority = 0
        count = 0

        for num in nums:
            if count == 0:
                majority = num
                count += 1
            elif num == majority:
                count += 1
            else:
                count -= 1

        left, right = 0, 0

        for num in nums:
            if num == majority:
                right += 1

        for i in range(len(nums)):
            # sliding window part, where we keep moving it down and then see if it its the case that we need.
            if nums[i] == majority:
                left += 1
                right -= 1

            if left > (i + 1) // 2 and right > (len(nums) - i - 1) // 2:
                return i

        return -1

        

print(Solution().minimumIndex([9,5,5,1,1,1,1,8,1]))
