package com.tahminator.leetcode.l215_kth_largest_element_in_an_array;

class Solution {

  private void add(int num, Queue<Integer> q, int k) {
    if (q.size() < k) {
      q.offer(num);
      return;
    } else if (q.peek() < num) {
      q.poll();
      q.offer(num);
    }
      
  }

  /**
   * Given [3,2,1,5,6,4], k = 2.
   * 3 and 2 go in with no problem because it's less than k.
   * Our queue is in the order of {2, 3}
   * Then we get to 1, of which if 1 is smaller than the current smallest (head)
   * then we pop that and insert our new lowest which will bubble up to the top
   * because of the PriorityQueue.
   */
  public int findKthLargest(int[] nums, int k) {
    Queue<Integer> q = new PriorityQueue<>();

    for (int num: nums) {
      add(num, q, k);
    }

    return q.peek();
  }
}
