# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def removeNthFromEnd(self, head: Optional[ListNode], n: int) -> Optional[ListNode]:
        slow = head
        fast = head
        
        for i in range(n):
            if not fast.next:
                if n - 1 == i:
                    head = head.next
                    return head
            fast = fast.next
            
        while fast.next:
            fast = fast.next
            slow = slow.next

        slow.next = slow.next.next
        return head
        