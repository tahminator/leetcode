package com.tahminator.leetcode.l0079_word_search;

/*
 * This problem will use a form of DFS to try to build the string out. We won't be starting until
 * we run into the very first character. Once we do that, we can start DFS on the graph where we look in every
 * adjacent cell and see whether or not it's the next valid character. Once we can append a value to the StringBuilder,
 * we can mark that cell as visited so we don't come back there by accident.
 */
class Solution {
  private final int[][] directions = { {0, 1}, {0, -1}, {1, 0}, {-1, 0} };

  public boolean exist(char[][] board, String word) {
    int rows = board.length;
    int cols = board[0].length;
    boolean[][] visited = new boolean[rows][cols];

    StringBuilder sb = new StringBuilder();
    
    char firstCharacter = word.charAt(0);
    for (int r = 0; r < rows; r++) {
      for (int c = 0; c < cols; c++) {
        if (!visited[r][c] && board[r][c] == firstCharacter) {
          dfs(visited, board, Map.entry(r, c), word, sb);
          String res = sb.toString();
          return res.equals(word);
        }
      }
    }
    
    return false;
  }

  private void dfs(boolean[][] visited, int[][] board, Map.Entry<Integer, Integer> coords, String word, StringBuilder sb, int i) {

  }
}
