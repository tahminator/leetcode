from typing import List

class Solution:
    def trap(self, height: List[int]) -> int:
        l, r = 0, len(height) - 1
        maxl, maxr = height[l], height[r]
        water = 0

        while l < r:
            if height[l] < height[r]:
                if height[l] < maxl:
                    water += min(maxl, maxr) - height[l]
                l += 1
                maxl = max(maxl, height[l])
            else:
                if height[r] < maxr:
                    water += min(maxl, maxr) - height[r]
                r -= 1
                maxr = max(maxr, height[r])

        return water

print(Solution().trap([0,1,0,2,1,0,1,3,2,1,2,1]))
