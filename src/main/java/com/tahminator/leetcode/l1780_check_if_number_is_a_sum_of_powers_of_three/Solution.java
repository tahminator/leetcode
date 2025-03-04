package com.tahminator.leetcode.l1780_check_if_number_is_a_sum_of_powers_of_three;

class Solution {
  public boolean checkPowersOfThree(int n) {
    while (n > 0) {
      if (n % 3 == 2) {
        return false;
      }
      n /= 3;
    }

    return true;
  }
}
