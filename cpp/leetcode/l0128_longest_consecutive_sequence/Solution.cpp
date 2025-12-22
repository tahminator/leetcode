class Solution {
public:
  int longestConsecutive(vector<int>& nums) {
    if (nums.empty()) return 0;
    int max = -1;
    for (auto n : nums) {
      max = std::max(n, max);
    }

    // ignore 0
    std::vector<int> arr(max + 1, 0);

    for (auto n : nums) {
      arr[n] = 1;
    }

    int res = 0;
    int curr = 0;
    for (auto n : arr) {
      if (n == 0) {
        res = std::max(curr, res);
        curr = 0;
        continue;
      }

      curr++;
    }

    res = std::max(curr, res);

    return res;
  }
};
