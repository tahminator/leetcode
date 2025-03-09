package com.tahminator.leetcode.l0069_sqrt_x;

/**
 * Given 4, we can easily find this by just walking through
 * the space of sorted integers and finding the value that way.
 *
 * However, we need to support decimal floats being dropped to their floor.
 * The easiest way to likely do that would be to use floats to track
 * middle, left and right and then use a floor function on m^2 to check if 
 * it's a possible fit.
 *
 * [0,1,2,3,4,5,6,7,8]
 * 
 */
class Solution {
  public int mySqrt(int x) {
    int l = 0, r = x;

    while (l <= r) {
      int m = l + (r - l) / 2;
      long m2 = 1L * m * m;

      if (m2 == (long) x) {
        return m;
      } else if (m2 > (long) x) {
        r = m - 1;
      } else {
        l = m + 1;
      }
    }

    // We jump one too far at the very last iteration, so we subtract 1 to offset that and 
    // then we are left with the floor of x ** 1/2.
    return l - 1;
  }
}
