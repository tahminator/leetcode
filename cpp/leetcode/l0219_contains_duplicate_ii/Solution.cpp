using Map = std::unordered_map<int, int>;

/**
  * [1,2,3,1,4,1]
  * <>
  * <  >
  * <    >
  * <      >
  *
  * if we saw that the number has been seen before,
  * since its fixed size sliding window , we should check
  * if we are larger than k and seen reports that nums[r] has been seen, get the 
  * value of the key from the map (which is index) and return.
  *
  * else add to map using key of r and value of nums[r]
  */
class Solution {
public:
  bool containsNearbyDuplicate(vector<int>& nums, int k) {
    Map seen;

    for (int r = 0; r < nums.size(); r++) {
      Map::iterator found = seen.find(nums[r]);
      if (found != seen.end() && r - found->second <= k) {
        return true;
      }

      seen[nums[r]] = r;
    }

    return false;
  }
};
