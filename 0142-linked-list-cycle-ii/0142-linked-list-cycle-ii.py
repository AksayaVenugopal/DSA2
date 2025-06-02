# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, x):
#         self.val = x
#         self.next = None

class Solution:
    def detectCycle(self, head: Optional[ListNode]) -> Optional[ListNode]:
        slow,fast,f=head,head,False
        
        while fast!=None and fast.next!=None:
            
            slow=slow.next
            fast=fast.next.next
            l=0
            if slow==fast:
                
                entry = head
                while entry != slow:
                    entry = entry.next
                    slow = slow.next
                return entry
        
        return None