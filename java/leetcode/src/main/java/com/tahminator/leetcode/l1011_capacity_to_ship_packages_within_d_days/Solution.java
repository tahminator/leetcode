package com.tahminator.leetcode.l1011_capacity_to_ship_packages_within_d_days;

class Solution {
  public int shipWithinDays(int[] weights, int days) {
    int max = -1;
    for (int w : weights) {
      max = Math.max(max, w);
    }
    int l = 1, r = max * days;

    while (l <= r) {
      int m = l + (r - l) / 2;

      int pd = 0;
      for (int w : weights) {
        pd += Math.ceil(1.0 * w / m);
      }

      if (pd <= days) {
        r = m - 1;
      } else {
        l = m + 1;
      }
    }

    return l;
  }
}
