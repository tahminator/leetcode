package com.tahminator.leetcode.l0219_contains_duplicate_ii;

/**
 * [1,2,3,1], k = 3
 * <>
 *  < >
 *  <   >
 *    <   >
 */
class Solution {
  public boolean containsNearbyDuplicate(int[] nums, int k) {
    Set<Integer> seen = new HashSet<>();
    int l = 0;

    for (int r = 0; r < nums.length; r++) {
      if (r - l > k) {
        if (seen.contains(nums[l])) {
          seen.remove(nums[l]);
        }
        l++;
      }
      if (seen.contains(nums[r])) {
        return true;
      }
      seen.add(nums[r]);
    }

    return false;
  }
}
