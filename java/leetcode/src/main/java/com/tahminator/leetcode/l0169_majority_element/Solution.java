package com.tahminator.leetcode.l169_majority_element;

/**
 * Boyer-Moore
 */
class Solution {
    public int majorityElement(int[] nums) {
      int c = 0, m = -1; 
      
      for (int num : nums) {
        if (c == 0) {
          m = num;
          c = 1;
        } else if (m == num) {
          c++;
        } else {
          c--;
        }
      }

      return m;
    }
}
