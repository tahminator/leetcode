package com.tahminator.leetcode.l0739_daily_temperatures;

class Solution {
  public int[] dailyTemperatures(int[] temps) {
    int[] res = new int[temps.length];
    Stack<Integer> s = new Stack<>();

    for (int i = 0; i < temps.length; i++) {
      int t = temps[i];
      while (!s.isEmpty() && t > temps[s.peek()]) {
        int j = s.pop();
        int d = i - j;
        res[j] = d;
      }

      s.push(i);
    }

    while (!s.isEmpty()) {
      int j = s.pop();
      res[j] = 0;
    }

    return res;
  }
}
