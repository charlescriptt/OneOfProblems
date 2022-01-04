# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def removeNthFromEnd(self, head: Optional[ListNode], n: int) -> Optional[ListNode]:
        #creation of dummy node for output for if head of list is deleted
        out = ListNode(0, head)
        current = lead = out
        #increment lead pointer to act as indicator of when to delete node
        while n > 0 :
            lead = lead.next
            n -= 1
        
        #increment through the list
        while lead.next != None:
            lead = lead.next
            current = current.next
        
        #after end of list is hit the current node(to be deleted must) is skipped as we are now in correct placement          
        current.next = current.next.next        
        
        return out.next
            