# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def getDecimalValue(self, head: Optional[ListNode]) -> int:
        w=[]
        decimal=0
        q=head.val
        decimal=decimal*2+q
        w.append(q)
        node=head.next
        while node!=None:
            cn=node.val
            decimal=decimal*2+cn
            w.append(cn)
            node=node.next
        return decimal
        