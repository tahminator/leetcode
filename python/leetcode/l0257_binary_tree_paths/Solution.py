from typing import Optional, List

# Definition for a binary tree node.
class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right

class Solution:
    def binaryTreePaths(self, root: Optional[TreeNode]) -> List[str]:
        res = []
        if not root:
            return res
        self.search(root, res, str(root.val))

        return res

    def search(self, node, res, path):
        if not node.left and not node.right:
            res.append(path)
            return

        if node.left:
            self.search(node.left, res, f"{path}->{node.left.val}")

        if node.right:
            self.search(node.right, res, f"{path}->{node.right.val}")

root = TreeNode(1)
root.left = TreeNode(2)
root.right = TreeNode(3)
root.left.right = TreeNode(5)

print(Solution().binaryTreePaths(root))
