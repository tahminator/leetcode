class Solution {
public:
  int numDecodings(string s) {
    std::unordered_map<int, int> c;

    c[s.length()] = 1;

    return dfs(0, c, s);
  }

  int dfs(int i, std::unordered_map<int, int>& c, string& s) {
    if (c.count(i)) {
      return c[i];
    }

    if (s[i] == '0') {
      return 0;
    }

    int res = dfs(i + 1, c, s);
    if (i + 1 < s.length() && 
        (s[i] == '1' ||
          (s[i] == '2' && s[i + 1] >= '0' && s[i + 1] <= '6'))
    ) {
      res += dfs(i + 2, c, s);
    }

    c[i] = res;
    return res;
  }
};
