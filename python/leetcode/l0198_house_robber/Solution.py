class Solution:
    # def rob(self, nums: List[int]) -> int:
    #     def solver(i):
    #         if i >= len(nums):
    #             return 0
    #         # we either pick the current number and move on to it's next valueq
    #         # or skip the current one and see which one is larger.
    #         return max(nums[i] + solver(i + 2), solver(i + 1))
    #     return solver(0)
    #
    
    def rob(self, nums):
        if len(nums) == 1:
            return nums[0]

        dp = [0 for _ in range(len(nums))]
        dp[0], dp[1] = nums[0], max(nums[0], nums[1])

        for i in range(2, len(nums)):
            dp[i] = max(nums[i] + dp[i - 2], dp[i - 1])

        return dp[-1]

print(Solution().rob([1,2,3,1]))

