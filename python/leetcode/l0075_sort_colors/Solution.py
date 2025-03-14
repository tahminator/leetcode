from typing import List

"""
The question is easier because we know that there is only 0, 1, or 2.
So keeping that in mind, we can sort based off of that logic.

Dutch flag problem
"""

class Solution:
    def sortColors(self, nums: List[int]) -> None:
        zero, one, two = 0, 0, len(nums) - 1

        while one <= two:
            if nums[one] == 0:
                nums[one], nums[zero] = nums[zero], nums[one]
                zero += 1
                one += 1
            elif nums[one] == 1:
                one += 1
            else:
                nums[one], nums[two] = nums[two], nums[one]
                two -= 1


Solution().sortColors([2,0,2,1,1,0])
Solution().sortColors([2,0,1])
Solution().sortColors([1,0,1])
