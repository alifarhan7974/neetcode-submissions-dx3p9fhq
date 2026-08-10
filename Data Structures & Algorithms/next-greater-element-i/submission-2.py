class Solution:
    def nextGreaterElement(self, nums1: List[int], nums2: List[int]) -> List[int]:
        next_greater = {}
        stack = [] 

        for x in nums2: 
            if not stack: 
                stack.append(x)

            while stack and x > stack[-1]: 
                next_greater[stack.pop()] = x 

            stack.append(x)
            print(next_greater, stack)
        
        answer = []

        for num in nums1: 
            if num not in next_greater: 
                answer.append(-1)
            else: 
                answer.append(next_greater[num])

        return answer 
                

            
            
                    


        


        
        