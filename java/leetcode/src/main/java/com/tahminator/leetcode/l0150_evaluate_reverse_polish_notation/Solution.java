package com.tahminator.leetcode.l0150_evaluate_reverse_polish_notation;

class Solution {
  public int evalRPN(String[] tokens) {
    Stack<Integer> s = new Stack<>();

    for (String t : tokens) {
      if (t.equals("+")) {
        int v1 = s.pop(), v2 = s.pop();
        s.push(v1 + v2);
      } else if (t.equals("-")) {
        int v1 = s.pop(), v2 = s.pop();
        s.push(v2 - v1);
      } else if (t.equals("*")) {
        int v1 = s.pop(), v2 = s.pop();
        s.push(v1 * v2);
      } else if (t.equals("/")) {
        int v1 = s.pop(), v2 = s.pop();
        s.push(v2 / v1);
      } else {
        s.push(Integer.valueOf(t));
      }
    }

    return s.pop();
  }
}
