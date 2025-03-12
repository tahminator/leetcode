"""
# Definition for a Node.
class Node:
    def __init__(self, val = 0, neighbors = None):
        self.val = val
        self.neighbors = neighbors if neighbors is not None else []
"""


# This problem blows. The description is terrible.
from typing import Optional
class Solution:
    def cloneGraph(self, node: Optional['Node']) -> Optional['Node']:
        int n = max(node)
        nodeToParent = {}
        nodeToChild = {}

        if not node:
            return None

        cur = node
        while cur:
            neighbors = cur.neighbors

            for neighbor in neighbors:
                c = nodeToParent.get(neighbor.val, 0)
                c += 1
                nodeToParent[neighbor.val] = c

                children = nodeToChild.get(cur.val, [])
                children.append(neighbor)
                nodeToChild[cur.val] = neighbor


        res = dummy = Node()

        q = deque([(node, res)])

        while q:
            cur, pointer = q.popleft()

            pointer.neighbors = pointer.neighbors + [Node(cur.val)]

            children = cur.neighbors

            for child in children:
                nodeToParent.get(child.val, 1)
                c -= 1
                nodeToParent[child.val] = c

                if c == 0:
                    pointer.neighbors.append(Node(child.val))
                    i = pointer.neighbors.find(child.val)
                    q.append(child, pointer.neighbors[i])

        return dummy.next

