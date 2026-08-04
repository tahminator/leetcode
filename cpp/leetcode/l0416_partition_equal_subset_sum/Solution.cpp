class Solution {
public:
  bool canPartition(vector<int>& nums) {
    int total = 0;
    for (auto n : nums) {
      total += n;
    }

    if (total % 2 != 0) {
      return false;
    }

    int half = total / 2;

    std::vector<bool> dp(half + 1);
    dp[0] = true;

    for (auto n : nums) {
      for (int i = dp.size() - 1; i >= n; i--) {
        if (dp[i]) {
          continue;
        }

        if (dp[i-n]) {
          dp[i] = true;
        }

        if (dp.back()) {
          return true;
        }
      }
    }

    return false;
  }
};
