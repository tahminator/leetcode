class Solution {
  void print_dp(std::vector<std::vector<int>>& dp) {
    for (auto& r : dp) {
      for (auto& c : r) {
        std::print("{} ", c);
      }
      std::println();
    }
  }

public:
  std::string longestPalindrome(std::string s) {
    int n = s.length();
    std::vector<std::vector<int>> dp(
      n, std::vector<int>(n, false)
    );

    // represents the single char words (all single words are palindromes :) )
    for (int i = 0; i < n; i++) {
      dp[i][i] = true;
    }
    int max_len = 1;
    int coords[2] = { 0, 0 };

    for (int len = 2; len < n + 1; len++) {
      for (int l = 0; l < n - len + 1; l++) {
        int r = l + len - 1;
        if (s[l] == s[r]) {
          if (len == 2 || dp[l + 1][r - 1]) {
            dp[l][r] = true;

            if (len > max_len) {
              max_len = len;
              coords[0] = l;
              coords[1] = r;
            }
          }
        }
      }
    }

    // print_dp(dp);
    return s.substr(coords[0], coords[1] - coords[0] + 1);
  }
};
