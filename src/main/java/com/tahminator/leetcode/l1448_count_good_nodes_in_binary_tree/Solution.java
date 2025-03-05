package com.tahminator.leetcode.l1448_count_good_nodes_in_binary_tree;

/**
 * Definition for a binary tree node.
 * public class TreeNode {
 *     int val;
 *     TreeNode left;
 *     TreeNode right;
 *     TreeNode() {}
 *     TreeNode(int val) { this.val = val; }
 *     TreeNode(int val, TreeNode left, TreeNode right) {
 *         this.val = val;
 *         this.left = left;
 *         this.right = right;
 *     }
 * }
 */
class Solution {
    /**
     * This is likely going to be DFS as we care more about the way that we trace back to the root.
     * We need to keep track of the current maximum for the path in each node. If the node is larger than the maximum sum,
     * increase the total and update to the new maximum. If not larger, just recursively call the left and right children
     * to check if exists.
     */ 
    public int goodNodes(TreeNode root) {
      if (root == null) {
        return 0;
      }

      int[] res = {1};
      int max = root.val;
      
      helper(root.left, max, res);
      helper(root.right, max, res);

      return res[0];
    }

    private void helper(TreeNode node, int max, int[] sum) {
      if (node == null) {
        return;
      }

      if (node.val >= max) {
        sum[0]++;
        max = node.val;
      }
        
      helper(node.left, max, sum);
      helper(node.right, max, sum);
    }
}
