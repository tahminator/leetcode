package com.tahminator.leetcode.l0973_k_closest_points_to_origin;

class Solution {
    private static final int[] origin = {0, 0};
    
    public int[][] kClosest(int[][] points, int k) {
        Queue<int[]> q = new PriorityQueue<>((a, b) -> a[2] - b[2]);
        int[][] res = new int[k][2];

        for (int[] p : points) {
          q.offer(new int[]{p[0], p[1], distance});
        }
        
        int i = 1; 
        
        while (i <= k) {
          int v = q.poll();
          int x = v[0];
          int y = v[1];
          res[i - 1] = new int[]{x, y};
        }

        return res;
    }

   private int distance(int x1, int x2, int y1, int y2) {
        int xdiff = x1 - x2;
        int ydiff = y1 - y2;
      
        int xsq = xdiff * xdiff;
        int ysq = ydiff * ydiff;

        return Math.sqrt(xsq + ysq);
   }
}
