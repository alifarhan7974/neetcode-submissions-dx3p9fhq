# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next

class Solution:
    def reverseList(self, head: Optional[ListNode]) -> Optional[ListNode]:
        if head is None:
            return head
        
        prev_node = head
        current_node = prev_node.next

        prev_node.next = None

        while True: 
            if current_node is None: 
                break

            temp = current_node.next
            current_node.next = prev_node

            prev_node = current_node 
            current_node = temp 

            
        head = prev_node 
        print(head.val)
        return head 

        

        