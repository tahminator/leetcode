class Solution {
  std::vector<std::string> dig_to_letters = {
    "",
    "",
    "abc",
    "def",
    "ghi",
    "jkl",
    "mno",
    "pqrs",
    "tuv",
    "wxyz",
  };

public:
  // we can solve this problem relatively trivially - for each character attached to a letter, we will 
  // recurse deeper with that character appended to the current string. if i has hit end of digits, then 
  // we know we are done recursing on this path.
  std::vector<string> letterCombinations(std::string digits) {
    if (digits.length() == 0) {
      return {};
    }

    std::vector<string> res;

    dfs(digits, 0, res, "");

    return res;
  }

  void dfs(std::string& digits, int i, std::vector<string>& res, std::string curr) {
    if (i == digits.length()) {
      res.emplace_back(curr);
      return;
    }

    int dig = digits[i] - '0';
    auto& s = dig_to_letters[dig];
    for (auto c : s) {
      curr.push_back(c);
      dfs(digits, i + 1, res, curr);
      curr.pop_back();
    }
  }
};
