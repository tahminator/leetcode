package com.tahminator.leetcode.l3208_alternating_groups_ii;

/**
 * Sliding window with a fixed length of k.
 * The criteria for counting differences is anything that isn't the 
 * left and right are different or not. 
 *
 */
class Solution {
  public int numberOfAlternatingGroups(int[] colors, int k) {
    int pc = colors[0];
    int res = 0;
    int s = 1;
    for (int i = 1; i < colors.length + k - 1; i++) {
      int cc = colors[i % colors.length]; 
      // This is not a valid sequence, so just restart and move to the start of the next possible valid sequence.
      if (cc == pc) {
        s = 1;
        pc = cc;
        continue;
      }

      s++;

      // Found a valid k-len sequence. We can keep going even after it surprasses k because
      // in our head, if we just increment the L pointer by one, we will have a brand new valid sequence. 
      if (s >= k) {
        res++;
      }

      pc = cc;
    }

    return res;
  }
}
