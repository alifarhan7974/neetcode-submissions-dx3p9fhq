# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next

class Solution:
    def mergeTwoLists(self, list1: Optional[ListNode], list2: Optional[ListNode]) -> Optional[ListNode]:
        dummy = ListNode()
        curr = dummy

        print(f"dummy.val, dummy.next {dummy.val}, {dummy.next}")
        while list1 and list2:
            if list1.val <= list2.val:
                #print(f"Adding list1: {list1.val}")
                curr.next = list1
                list1 = list1.next
            else:
                #print(f"Adding list2: {list2.val}")
                curr.next = list2
                list2 = list2.next
            curr = curr.next
            #print(f"inside loop dummy.val, dummy.next {dummy.val}, {dummy.next}")

        
        #print(f"prev.val, prev.next {prev.val}, {prev.next}")

        if list1: 
            curr.next = list1
        else: 
            curr.next = list2

        return dummy.next 
              


        
        

        
