package com.tahminator.leetcode.l0344_reverse_string;

class Solution {
  /**
   * Write a function that reverses a string. The input string is given as an array of characters s.
   * 
   * You must do this by modifying the input array in-place with O(1) extra memory.
   */
  public void reverseString(char[] s) {
    int l = 0, r = s.length - 1;

    while (l <= r) {
      char temp = s[l];
      s[l] = s[r];
      s[r] = temp;
      l++;
      r--;
    }
  }
}
