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
            # fast의 다음칸이 없는데 i가 n-1과 같다는 것은
            # 노드가 두 개 있는데 첫번째 노드를 지우라는 뜻
            # head가 next 가리키게 한 다음 head 반환
            if not fast.next:
                if i == n - 1:
                    head = head.next
                return head
            fast = fast.next
        
        while fast.next:
            fast = fast.next
            slow = slow.next
            
        slow.next = slow.next.next
        return head