class Solution {
public:
  int countSubstrings(std::string s) {
    int n = s.length();

    std::vector<std::vector<int>>dp(
      n, std::vector<int>(n, false)
    );

    for (int i = 0; i < n; i++) {
      dp[i][i] = true;
    }

    int res = n;
    for (int len = 2; len < n + 1; len++) {
      for (int l = 0; l < n - len + 1; l++) {
        int r = l + len - 1;
        if (s[l] == s[r]) {
          if (len == 2 || dp[l + 1][r - 1] == true) {
            dp[l][r] = true;
            res++;
          }
        }
      }
    }

    return res;
  }
};
