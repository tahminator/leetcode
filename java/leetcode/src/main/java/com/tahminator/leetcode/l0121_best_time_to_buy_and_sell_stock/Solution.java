package com.tahminator.leetcode.l0121_best_time_to_buy_and_sell_stock;

class Solution {
  public int maxProfit(int[] prices) {
    int res = 0;
    int buy = Integer.MAX_VALUE;
    for (int i = 0; i < prices.length; i++) {
      int pb = prices[i];
      if (pb < buy) {
        // we are always looking for the cheapest buy.
        buy = pb;
      }

      res = Math.max(res, prices[i] - buy);
    }

    return res;
  }
}
