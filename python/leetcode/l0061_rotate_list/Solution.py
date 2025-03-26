# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def rotateRight(self, head: Optional[ListNode], k: int) -> Optional[ListNode]:
        if head is None or head.next is None:
            return head

        if k is 0:
            return head

        len = 0

        cur = head
        while cur is not None:
            len += 1
            cur = cur.next

        n = len - (k % len)

        # just wraps fully around.
        if n % len == 0:
            return head

        i = 0
        cur = head
        while cur.next is not None:
            i += 1

            if i == n:
                break

            cur = cur.next

        new_head = cur.next
        cur.next = None

        cur = new_head

        while cur.next is not None:
            cur = cur.next

        cur.next = head

        return new_head



