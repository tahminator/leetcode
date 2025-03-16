from typing import Optional

# Definition for singly-linked list.
class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next

class Solution:
    def oddEvenList(self, head: Optional[ListNode]) -> Optional[ListNode]:
        if head is None:
            return

        if head.next is None:
            return head

        l, r = head, head.next
        original_r = r

        while (l is not None and l.next is not None) or (r is not None and r.next is not None):
            # print(l.val, r.val)
            l.next = l.next.next if l.next else None
            r.next = r.next.next if r.next else None
            l = l.next
            r = r.next

        cur = head
        while cur.next is not None:
            cur = cur.next

        cur.next = original_r

        return head

linked_list = ListNode(1, 
                ListNode(2, 
                    ListNode(3, 
                        ListNode(4, 
                            ListNode(5, 
                                ListNode(6, 
                                    ListNode(7, 
                                        ListNode(8, None))))))))

ans = Solution().oddEvenList(linked_list)

while ans is not None:
    print(ans.val)
    ans = ans.next

# linked_list = ListNode(1, 
#                 ListNode(2, 
#                     ListNode(3, 
#                         ListNode(4, 
#                             ListNode(5, None)))))
# ans = Solution().oddEvenList(linked_list)
#
# while ans is not None:
#     print(ans.val)
#     ans = ans.next
