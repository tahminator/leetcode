class Solution:
    def maxArea(self, height: List[int]) -> int:
        l, r = 0, len(height) - 1
        maxArea = 0

        while l <= r:
            calculatedArea = (r - l) * min(height[l], height[r])
            maxArea = max(maxArea, calculatedArea)

            if height[r] > height[l]:
                l += 1
            else:
                r -= 1

        return maxArea
