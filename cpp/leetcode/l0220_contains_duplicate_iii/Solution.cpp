typedef std::vector<int>::iterator vIter;
typedef std::set<int>::iterator sIter;

class Solution {
public:
  bool containsNearbyAlmostDuplicate(std::vector<int> &nums, int indexDiff,
                                     int valueDiff) {
    if (indexDiff <= 0 || valueDiff < 0 || nums.empty()) {
      return false;
    }
    std::set<int> window;

    for (vIter i = nums.begin(); i != nums.end(); i++) {
      int x = *i;
      sIter lower = window.lower_bound(x - valueDiff);
      if (lower != window.end() && *lower <= x + valueDiff) {
        return true;
      }

      window.insert(x);
      size_t idx = i - nums.begin();
      if (idx >= indexDiff) {
        window.erase(nums[idx - indexDiff]);
      }
    }

    return false;
  }
};
