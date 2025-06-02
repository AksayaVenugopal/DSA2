# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def deleteMiddle(self, head: Optional[ListNode]) -> Optional[ListNode]:
        c=0
        l={}
        node=head
        while node!=None:
            l[c]=node
            c+=1
            node=node.next
        m=(c//2)
        if c==1:
            return None
        l[m-1].next=l[m].next
        return head

        