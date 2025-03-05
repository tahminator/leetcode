package com.tahminator.leetcode.l0703_kth_largest_element_in_a_stream;

import java.util.Collections;

class KthLargest {
    Queue<Integer> q;
    int k;

    public KthLargest(int k, int[] nums) {
      q = new PriorityQueue<>();
      this.k = k;
      
      for (int n : nums) {
        add(n);
      }
    }
    
    public int add(int val) {
      if (q.size() < k) {
        q.offer(val);
      } else if (q.peek() < val) {
        q.poll();
        q.offer(val);
      }
      
      return q.peek();
    }
}

/**
 * Your KthLargest object will be instantiated and called as such:
 * KthLargest obj = new KthLargest(k, nums);
 * int param_1 = obj.add(val);
 */
