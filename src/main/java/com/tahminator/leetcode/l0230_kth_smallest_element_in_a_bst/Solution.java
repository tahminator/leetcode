package com.tahminator.leetcode.l0230_kth_smallest_element_in_a_bst;

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
     * Inorder traversal naturally returns a BST in order from smallest to greatest.
     * We can utilize this condition to solve this problem in-place.
     */
    public int kthSmallest(TreeNode root, int k) {
      // Should never happen.
      if (root == null) {
        return -1;
      }

      int[] res = {-1};
      int[] i = {0};
      helper(root, res, i, k);
      return res[0];
    }

    private void helper(TreeNode node, int[] res, int[] i, int k) {
      if (node == null) {
        return;
      }

      helper(node.left, res, i, k);
      i[0]++;

      if (i[0] == k) {
        res[0] = node.val;
        return;
      }
      
      helper(node.right, res, i, k);
    }
}
