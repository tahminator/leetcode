package com.tahminator.leetcode.l0015_3sum;

import java.util.ArrayList;
import java.util.Arrays;
import java.util.List;

class Solution {
  /**
   * Given an integer array nums, return all the triplets [nums[i], nums[j], nums[k]] such that i != j, i != k, and j != k, and nums[i] + nums[j] +
   * nums[k] == 0.
   * 
   * Notice that the solution set must not contain duplicate triplets.
   * 
   * 
   * 
   * Example 1:
   * 
   * Input: nums = [-1,0,1,2,-1,-4] Output: [[-1,-1,2],[-1,0,1]] Explanation: nums[0] + nums[1] + nums[2] = (-1) + 0 + 1 = 0. nums[1] + nums[2] +
   * nums[4] = 0 + 1 + (-1) = 0. nums[0] + nums[3] + nums[4] = (-1) + 2 + (-1) = 0. The distinct triplets are [-1,0,1] and [-1,-1,2]. Notice that the
   * order of the output and the order of the triplets does not matter. Example 2:
   * 
   * Input: nums = [0,1,1] Output: [] Explanation: The only possible triplet does not sum up to 0. Example 3:
   * 
   * Input: nums = [0,0,0] Output: [[0,0,0]] Explanation: The only possible triplet sums up to 0.
   */

  public List<List<Integer>> threeSum(int[] nums) {
    Arrays.sort(nums);
    List<List<Integer>> res = new ArrayList<>();

    for (int k = 0; k < nums.length; k++) {
      if (k > 0 && nums[k] == nums[k - 1]) {
        continue;
      }

      int i = k + 1, j = nums.length - 1;
      int nk = nums[k] * -1;

      while (i < j) {
        int sum = nums[i] + nums[j];
        if (sum == nk) {
          res.add(Arrays.asList(nums[i], nums[j], nums[k]));
          i++;
          while (i < j && nums[i] == nums[i - 1]) {
            i++;
          }
        } else if (sum > nk) {
          j--;
        } else {
          i++;
        }
      }
    }

    return res;
  }
}
