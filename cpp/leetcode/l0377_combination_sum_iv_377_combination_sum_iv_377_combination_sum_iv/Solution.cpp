class Solution {
public:
  int combinationSum4(std::vector<int>& nums, int target) {
    std::vector<unsigned long long>dp(target + 1);
    dp[0] = 1;

    for (unsigned long long t = 1; t <= target; t++) {
      for (auto n : nums) {
        if (t >= n) {
          dp[t] += dp[t - n];
        }
      }
    }

    return dp[target];
  }
};
