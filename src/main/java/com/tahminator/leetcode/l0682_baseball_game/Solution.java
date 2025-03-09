package com.tahminator.leetcode.l0682_baseball_game;

class Solution {
  public int calPoints(String[] operations) {
    Stack<Integer> s = new Stack<>();

    for (String o : operations) {
      if (o.equals("C")) {
        s.pop();
      } else if (o.equals("D")) {
        int pv = s.peek();
        s.push(pv * 2);
      } else if (o.equals("+")) {
        int v1 = s.pop(), v2 = s.pop();
        s.push(v2);
        s.push(v1);
        s.push(v1 + v2);
      } else {
        s.push(Integer.valueOf(o));
      }
    }

    int res = 0;
    while (!s.isEmpty()) {
      res += s.pop();
    }

    return res;
  }
}
