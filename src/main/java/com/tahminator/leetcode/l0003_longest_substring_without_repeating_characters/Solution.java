package com.tahminator.leetcode.l0003_longest_substring_without_repeating_characters;

class Solution {
  /**
   * "abcabcbb"
   *  
   */
  public int lengthOfLongestSubstring(String s) {
    int l = 0, maxlen = 0;
    Set<Character> chars = new HashSet<>();


    for (int r = 0; r < s.length(); r++) {
      while (chars.contains(s.charAt(r))) {
        chars.remove(s.charAt(l));
        l++;
      }

      chars.add(s.charAt(r));
      maxlen = Math.max(maxlen, chars.size());
    }

    return maxlen;
  }
}
