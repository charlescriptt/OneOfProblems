# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def mergeKLists(self, lists: List[Optional[ListNode]]) -> Optional[ListNode]:
        arr = []
        for l in lists:            
            while l:
                arr.append(l.val)
                l = l.next
                
        arr.sort()
        
        self.head = ListNode()
        self.current = self.head
        
        for i in arr:
            self.current.next = ListNode(i)
            self.current = self.current.next
        
        return self.head.next
        