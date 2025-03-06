package com.tahminator.leetcode.l2965_find_missing_and_repeated_values;

class Solution {
    /**
     * Naive solution, O(n^2) memory
     */
    public int[] findMissingAndRepeatedValues(int[][] grid) {
      int n = grid.length;
      int[] res = new int[(n * n) + 1];
  
      int rows = n, cols = n;

      for (int r = 0; r < rows; r++) {
        for (int c = 0; c < cols; c++) {
          int v = grid[r][c];

          res[v]++;
        }
      }
  
      int[] ans = new int[2];
      for (int i = 1; i < res.length; i++) {
        if (res[i] > 1) {
          ans[0] = i;
        }

        if (res[i] == 0) {
          ans[1] = i;
        }
      }

      return ans;
    }
}

