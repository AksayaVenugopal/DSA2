# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def oddEvenList(self, head: Optional[ListNode]) -> Optional[ListNode]:
        oddh=head
        odd=oddh

        if odd==None or odd.next==None:
            return odd
        evenh=head.next
        even=evenh
        
        while even and even.next:
            odd.next=even.next
            odd=odd.next
            even.next=odd.next
            even=even.next
        odd.next=evenh
        return oddh