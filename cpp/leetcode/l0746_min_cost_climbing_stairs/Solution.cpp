class Solution {
public:
  int minCostClimbingStairs(std::vector<int>& cost) {
    int n = cost.size();
    int dp[n + 1];

    dp[n] = 0;

    for (int i = n - 1; i >= 0; i--) {
      int min_cost;
      if (i == n - 1) {
          min_cost = dp[i + 1];
      } else {
          min_cost = min(dp[i + 1], dp[i + 2]);
      }
      dp[i] = cost[i] + min_cost;
    }

    return std::min(dp[0], dp[1]);
  }
};
