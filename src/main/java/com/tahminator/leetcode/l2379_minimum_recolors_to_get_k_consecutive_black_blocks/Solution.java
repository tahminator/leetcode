package com.tahminator.leetcode.l2379_minimum_recolors_to_get_k_consecutive_black_blocks;

/**
 * This could be similar to another problem, where if we can just calculate the moves required 
 * for each k-len window to be valid and take the minimum amount from each of them.
 */
class Solution {
  /**
   * [0, 1, 2, 3, 4], k = 3
   *        <     >
   */
  public int minimumRecolors(String blocks, int k) {
    int res = Integer.MAX_VALUE;
    for (int i = 0; i <= blocks.length() - k; i++) {
      int moves = 0;
      for (int j = 0; j < k; j++) {
        char c = blocks.charAt(i + j);
        if (c != 'B') {
          moves++;
        }
      }
      res = Math.min(res, moves);
    }

    return res;
  }
}
