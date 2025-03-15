from typing import Optional


class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right

# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def flatten(self, root: Optional[TreeNode]) -> None:
        """
        Do not return anything, modify root in-place instead.

        There seems to be a way to solve this problem without O(n) extra memory.
        """
        
        if root is None:
            return

        stack = []
        node = root

        self.preorder(node, stack)
        stack.reverse()

        root.val = stack.pop()
        node = root
        while stack:
            curr = stack.pop()
            node.left = None
            node.right = TreeNode(curr)
            node = node.right



    def preorder(self, node, stack):
        stack.append(node.val)
        if node.left:
            self.preorder(node.left, stack)
        if node.right:
            self.preorder(node.right, stack)

root = TreeNode(
    1,
    TreeNode(2, TreeNode(3), TreeNode(4)),
    TreeNode(5, None, TreeNode(6))
)
print(Solution().flatten(root))

print(root.right.val)

