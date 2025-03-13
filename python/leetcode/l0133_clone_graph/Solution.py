"""
# Definition for a Node.
class Node:
    def __init__(self, val = 0, neighbors = None):
        self.val = val
        self.neighbors = neighbors if neighbors is not None else []
"""

"""
The question is a little misleading because it doesn't give you an edge list, but rather
the entry node itself.
"""
# This problem blows. The description is terrible.
from typing import Optional
class Solution:
    def cloneGraph(self, node: Optional['Node']) -> Optional['Node']:
        # Seen will hold the value of the node as the key, and the value will be the node itself.
        seen = {}

        return self.copy(seen, node)


    def copy(self, seen, node):
        if not node:
            return Node()

        if node.val in seen:
            return seen.get(node.val)

        new_node = Node(node.val)
        seen[node.val] = node
        for neighbor in node.neighbors:
            new_node.neighbors.append(self.copy(seen, neighbor))

        return new_node

