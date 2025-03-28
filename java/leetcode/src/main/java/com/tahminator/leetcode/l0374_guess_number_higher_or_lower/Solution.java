package com.tahminator.leetcode.l0374_guess_number_higher_or_lower;

/**
 * Forward declaration of guess API.
 * 
 * @param num your guess
 * @return -1 if num is higher than the picked number
 *         1 if num is lower than the picked number
 *         otherwise return 0
 *         int guess(int num);
 */

public class Solution extends GuessGame {
  public int guessNumber(int n) {
    int l = 0, r = n;

    while (l <= r) {
      int m = l + (r - l) / 2;

      int g = guess(m);

      if (g  == 0) {
        return m;
      } else if (g == 1) {
        l = m + 1;
      } else {
        r = m - 1;
      }
    }

    // Should never happen if valid.
    return -1;
  }
}
