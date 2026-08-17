class Solution {
public:
  int maxTurbulenceSize(std::vector<int>& arr) {
    int n = arr.size();
    if (n == 0) return 0;
    if (n == 1) return 1;

    int max_len, cur_len;
    bool last_gt;

    for (int i = 1; i < n; i++) {
      int cur = arr[i], prev = arr[i - 1];
      if (i == 1) {
        last_gt = cur > prev;
        if (cur == prev) {
          cur_len = 1;
        } else {
          cur_len = 2;
        }
        max_len = cur_len;
        continue;
      }

      if (last_gt) {
        if (cur < prev) {
          // valid
          cur_len++;
          last_gt = !last_gt;
        } else {
          max_len = std::max(max_len, cur_len);
          if (cur == prev) {
            cur_len = 1;
          } else {
            cur_len = 2;
          }
        }
      } else {
        if (cur > prev) {
          // valid
          cur_len++;
          last_gt = !last_gt;
        } else {
          max_len = std::max(max_len, cur_len);
          if (cur == prev) {
            cur_len = 1;
          } else {
            cur_len = 2;
          }
        }
      }
    }

    return std::max(max_len, cur_len);
  }
};
