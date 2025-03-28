# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def mergeNodes(self, head: Optional[ListNode]) -> Optional[ListNode]:
        ans = temp = ListNode()
        cur = head

        while cur.next is not None:
            if cur.next.val == 0:
                if cur.next.next is None:
                    break
                ans.next = ListNode()
                ans = ans.next
            else:
                ans.val += cur.next.val
            cur = cur.next

        return temp
