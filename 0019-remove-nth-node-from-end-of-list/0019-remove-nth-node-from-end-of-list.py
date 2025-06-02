# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def removeNthFromEnd(self, head: Optional[ListNode], n: int) -> Optional[ListNode]:
        c=0
        node=head
        l={}
        while node!=None :
            l[c]=node
            c+=1
            node=node.next
        if n==c:
            return head.next
        l[c-n-1].next=l[c-n].next
        return head

        