# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next

class Solution:
    def removeNthFromEnd(self, head: Optional[ListNode], n: int) -> Optional[ListNode]:
        dummy = ListNode()
        dummy.next = head
        curr = head 
        fast = head

        for _ in range(n): 
            fast = fast.next

        prev = dummy 
        while fast: 
            prev = curr
            curr = curr.next
            fast = fast.next

        if prev and curr: 
            prev.next = curr.next

        return dummy.next


        