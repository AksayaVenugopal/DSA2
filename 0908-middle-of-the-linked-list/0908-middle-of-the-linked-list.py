# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def insert(self,val,next=None):
        self.val=val
        self.next=None
    def middleNode(self, head: Optional[ListNode]) -> Optional[ListNode]:
        l=0
        node=head
        while node!=None:
            l+=1
            node=node.next
        e=(l//2)+1
        node=head
        c=0
        while c+1<e:
            c+=1
            node=node.next
        return node 