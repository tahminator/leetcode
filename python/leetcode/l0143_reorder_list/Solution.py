from typing import Optional

def printList(head, name = None):
    cur = head
    print(name, end=": ") if name else None
    while cur:
        print(cur.val, end=" -> ")
        cur = cur.next
    print("End")

# Definition for singly-linked list.
class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next


class Solution:
    def reorderList(self, head: Optional[ListNode]) -> None:
        """

        notes:
            at first glance, easiest way might be to keep track of all references in a list. then, we can 
            both calculate total length of linked list + figure out how to re-interlace the list based on the parity 
            of len(linked_list).

            the easiest way to find that middle and split can also just be to use tortoise and hare method / slow fast pointer 
            to find the middle. then we can reverse the latter list, and then interleave each node until we are done.
        """

        if not head.next:
            return

        slow, fast = head, head

        # [1,2,3,4,5]
        #      
        # [1,2,3,4]
        #    
        while fast.next and fast.next.next:
            slow = slow.next
            fast = fast.next.next

        # set the head of second list, and sever the link at the end of first list
        secondHead = slow.next
        slow.next = None

        # reverse second list
        prev = None
        cur = secondHead
        
        while cur:
            nextNode = cur.next
            cur.next = prev
            prev = cur
            cur = nextNode
        
        newSecondHead = prev

        isFirst = True
        firstCur = head
        secondCur = newSecondHead

        while firstCur or secondCur:
            printList(firstCur, "firstCur")
            printList(secondCur, "secondCur")
            if isFirst:
                nextCurValue = firstCur.next
                firstCur.next = secondCur
                firstCur = nextCurValue
            else:
                nextCurValue = secondCur.next
                secondCur.next = firstCur
                secondCur = nextCurValue
            printList(head, "head")
            isFirst = not isFirst


# print(Solution().reorderList(ListNode(1, ListNode(2, ListNode(3, ListNode(4))))))
# print(Solution().reorderList(ListNode(1, ListNode(2))))
print(Solution().reorderList(ListNode(1, ListNode(2, ListNode(3, ListNode(4, ListNode(5, ListNode(6, ListNode(7)))))))))






