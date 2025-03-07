package com.tahminator.leetcode.l0013_roman_to_integer;

class Solution {
    private final Map<Character, Integer> key = Map.of('I', 1, 'V', 5, 'X', 10, 'L', 50, 'C', 100, 'D', 500, 'M', 1000);

    public int romanToInt(String s) {
        int length = s.length();

        if (length == 1) {
          return key.get(s.charAt(0));
        }

        char p = s.charAt(length - 1);
        int res = key.get(p);
        for (int i = length - 2; i >= 0; i--) {
          char c = s.charAt(i);

          int cv = key.get(c);
          int pv = key.get(p);

          if (pv > cv) {
            res -= cv;
          } else {
            res += cv;
          }

          p = c;
        }

        return res;
    }
}
