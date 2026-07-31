class Solution {
public:
    int numSquares(int n) {
        std::vector<int> perf;

        int i = 1;
        while (true) {
            int sq = i * i;
            if (sq > n) {
                break;
            }
            perf.push_back(sq);
            i++;
        }

        std::vector<int> dp(n + 1, INT_MAX);

        dp[0] = 0;

        for (int i = 1; i < dp.size(); i++) {
            for (int j = perf.size() - 1; j > -1; j--) {
                int ps = perf[j];
                if (ps > i) {
                    continue;
                }

                dp[i] = std::min(dp[i], dp[i - ps] + 1);
            }
        }
        
        return dp.back();
    }
};
