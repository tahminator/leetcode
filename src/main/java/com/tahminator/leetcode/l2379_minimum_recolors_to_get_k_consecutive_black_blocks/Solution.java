package com.tahminator.leetcode.l2379_minimum_recolors_to_get_k_consecutive_black_blocks;

/**
 * This could be similar to another problem, where if we can just calculate the moves required 
 * for each k-len window to be valid and take the minimum amount from each of them.
 */
class Solution {
  /**
   * [0, 1, 2, 3, 4], k = 3
   *        <     >
   *
   * "WBBWWBBWBW", k = 7
   *  <     >       c = 3, res = 3
   *   <     >      c = 3+1-1, res = 3
   *    <     >     c = 3, res = 3
   *     <     >
   */
  public int minimumRecolors(String blocks, int k) {
    int count = 0, res = Integer.MAX_VALUE;
    int l = 0, r = 0;

    while (r < blocks.length()) {
      if (blocks.charAt(r) == 'W') count++;
      if (r - l + 1 == k) {
        res = Math.min(res, count);
        if (blocks.charAt(l) == 'W') count--;
        l++;
      }
      r++;
    }

    return res;
  }
}
