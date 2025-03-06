package com.tahminator.leetcode.l1046_last_stone_weight;

import java.util.*;

class Solution {
    public int lastStoneWeight(int[] stones) {
        Queue<Integer> q = new PriorityQueue<>(Collections.reverseOrder());

        for (int stone : stones) {
          q.offer(stone);
        }
        
        while (q.size() >= 2) {
          int y = q.poll();
          int x = q.poll();

          if (x != y) {
            y -= x;
            q.offer(y);
          }
        } 
     
        
        return q.size() == 1 ? q.poll() : 0;
    }
}
