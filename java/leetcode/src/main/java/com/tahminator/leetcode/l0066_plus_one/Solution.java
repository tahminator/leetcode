package com.tahminator.leetcode.l0066_plus_one;

import java.util.ArrayList;
import java.util.Collections;
import java.util.List;

class Solution {
  /**
   * You are given a large integer represented as an integer array digits, where each digits[i] is the ith digit of the integer. The digits are ordered
   * from most significant to least significant in left-to-right order. The large integer does not contain any leading 0's.
   * 
   * Increment the large integer by one and return the resulting array of digits.
   * 
   * 
   * 
   * Example 1:
   * 
   * Input: digits = [1,2,3] Output: [1,2,4] Explanation: The array represents the integer 123. Incrementing by one gives 123 + 1 = 124. Thus, the
   * result should be [1,2,4]. Example 2:
   * 
   * Input: digits = [4,3,2,1] Output: [4,3,2,2] Explanation: The array represents the integer 4321. Incrementing by one gives 4321 + 1 = 4322. Thus,
   * the result should be [4,3,2,2]. Example 3:
   * 
   * Input: digits = [9] Output: [1,0] Explanation: The array represents the integer 9. Incrementing by one gives 9 + 1 = 10. Thus, the result should be
   * [1,0].
   * 
   */

  // [9], []
  // [9], [0]
  // [9], [0, 1]
  // [1, 0]

  // [1, 2, 3], []
  // [1, 2, 3], [4]
  // [1, 2, 3], [4, 2]
  // [1, 2, 3], [4, 2, 1]
  // [1, 2, 4]
  public int[] plusOne(int[] digits) {
    List<Integer> res = new ArrayList<>();

    int carry = 1;
    for (int i = digits.length - 1; i >= 0; i--) {
      int n = carry + digits[i];
      if (n >= 10) {
        carry = n / 10;
        n %= 10;
      } else {
        carry = 0;
      }
      res.add(n);
    }

    if (carry != 0) {
      res.add(carry);
    }

    Collections.reverse(res);

    return res.stream().mapToInt(i -> i).toArray();
  }
}
