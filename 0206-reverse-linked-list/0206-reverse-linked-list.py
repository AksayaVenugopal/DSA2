# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def reverseList(self, head: Optional[ListNode]) -> Optional[ListNode]:
        if head==None:
            return head
        node=head
        s=[]
        while node!=None:
            s.append(node.val)
            node=node.next
        s=s[::-1]
        head2=ListNode(s[0])
        node=head2
        for i in range(1,len(s)):
            node.next=ListNode(s[i])
            node=node.next
        return head2
        