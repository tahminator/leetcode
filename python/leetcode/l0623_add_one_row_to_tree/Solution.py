# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def addOneRow(self, root: Optional[TreeNode], val: int, depth: int) -> Optional[TreeNode]:
        if depth == 1:
            newNode = TreeNode(val)
            newNode.left = root
            root = newNode
            return root

        self.helper(root, 1, val, depth)
        return root

    def helper(self, node, currDepth, val, depth):
        if currDepth >= depth:
            return

        # Found parent node
        if currDepth == depth - 1:
            leftNode, rightNode = node.left, node.right

            newLeft, newRight = TreeNode(val), TreeNode(val)

            newLeft.left = leftNode
            newRight.right = rightNode

            node.left = newLeft
            node.right = newRight

            return

        currDepth += 1
        if node.left:
            self.helper(node.left, currDepth, val, depth)

        if node.right:
            self.helper(node.right, currDepth, val, depth)

