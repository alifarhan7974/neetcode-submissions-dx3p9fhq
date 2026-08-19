"""
# Definition for a Node.
class Node:
    def __init__(self, x: int, next: 'Node' = None, random: 'Node' = None):
        self.val = int(x)
        self.next = next
        self.random = random
"""

class Solution:
    def copyRandomList(self, head: 'Optional[Node]') -> 'Optional[Node]':
        copies = {}
        old = head

        while old: 
            copies[old] = Node(old.val)
            old = old.next

        old = head
        while old: 
            if old.next: 
                copies[old].next = copies[old.next]

            if old.random: 
                copies[old].random = copies[old.random]

            old = old.next 

        return copies[head] if head else None 

        


        



        
            
        


        
