# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next

class Solution:
    def reorderList(self, head: Optional[ListNode]) -> None:
        # Split two halves 
        # Reverse second half 
        # Merge 
        if not head or not head.next: 
            return

        # Find middle 
        fast, slow = head, head 
        while fast and fast.next: 
            slow = slow.next
            fast = fast.next.next 

        # Split into 2 lists 
        second = slow.next
        slow.next = None 


        # Reverse second
        curr = second
        prev = None 

        while curr: 
            temp = curr.next
            curr.next = prev
            prev = curr
            curr = temp 
            
        second = prev  # head of rev list 
        first = head   # head of first half 
        #self.print_list(first)
        #self.print_list(second)

        while second: 
            temp1 = first.next
            temp2 = second.next 

            first.next = second
            second.next = temp1

            first = temp1
            second = temp2 


    def print_list(self, node): 
        while node: 
            print(node.val, end = " ")
            node = node.next
        print("")

