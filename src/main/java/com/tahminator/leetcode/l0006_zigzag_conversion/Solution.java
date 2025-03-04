package com.tahminator.leetcode.l0006_zigzag_conversion;

class Solution {
  public String convert(String s, int numRows) {
    if (numRows == 1 || numRows >= s.length()) {
      return s;
    }

    StringBuilder[] sba = new StringBuilder[numRows];
    for (int i = 0; i < sba.length; i++) {
      sba[i] = new StringBuilder();
    }

    int row = 1;
    boolean increasing = false;
    for (char c : s.toCharArray()) {
      sba[row - 1].append(c);
      if (row == numRows || row == 1) {
        increasing = !increasing;
      }
      if (increasing) {
        row++;
      } else {
        row--;
      };
    }

    StringBuilder res = new StringBuilder();
  
    for (StringBuilder sb : sba) {
      res.append(sb);
    }

    return res.toString();
  }
}
