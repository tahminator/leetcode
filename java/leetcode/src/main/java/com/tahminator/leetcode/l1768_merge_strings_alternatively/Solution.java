package com.tahminator.leetcode.l1768_merge_strings_alternatively;

class Solution {
  /**
   * You are given two strings word1 and word2. Merge the strings by adding letters in alternating order, starting with word1. If a string is longer
   * than the other, append the additional letters onto the end of the merged string.
   * 
   * Return the merged string.
   * 
   * 
   * Example 1:
   * 
   * Input: word1 = "abc", word2 = "pqr" Output: "apbqcr" Explanation: The merged string will be merged as so: word1: a b c word2: p q r merged: a p b q
   * c r Example 2:
   * 
   * Input: word1 = "ab", word2 = "pqrs" Output: "apbqrs" Explanation: Notice that as word2 is longer, "rs" is appended to the end. word1: a b word2: p
   * q r s merged: a p b q r s Example 3:
   * 
   * Input: word1 = "abcd", word2 = "pq" Output: "apbqcd" Explanation: Notice that as word1 is longer, "cd" is appended to the end. word1: a b c d
   * word2: p q merged: a p b q c d
   */
  public String mergeAlternately(String word1, String word2) {
    StringBuilder sb = new StringBuilder();

    int p1 = 0, p2 = 0;

    boolean f = true;
    while (p1 < word1.length() && p2 < word2.length()) {
      if (f) {
        sb.append(word1.charAt(p1++));
      } else {
        sb.append(word2.charAt(p2++));
      }
      f = !f;
    }

    while (p1 < word1.length()) {
      sb.append(word1.charAt(p1++));
    }

    while (p2 < word2.length()) {
      sb.append(word2.charAt(p2++));
    }

    return sb.toString();
  }
}
