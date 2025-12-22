#include <vector>

class Solution {
public:
  std::vector<std::vector<int>> generate(int numRows) {
    std::vector<std::vector<int>> res;
    res.push_back({1});
    if (numRows == 1) return res;
    res.push_back({1, 1});

    for (int i = 2; i < numRows; i++) {
      std::vector<int> row;
      int cells = i + 1;

      for (int c = 0; c < cells; c++) {
        if (c == 0 || c == cells - 1) {
          row.emplace_back(1);
          continue;
        }

        auto& prev_row = res[i - 1];
        int prev_l = prev_row[c - 1], prev_r = prev_row[c];

        row.emplace_back(prev_l + prev_r);
      }

      res.emplace_back(row);
    }

    return res;
  }
};

int main() {
  Solution s;

  s.generate(5);
}
