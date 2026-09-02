from collections import defaultdict 
class Solution:
    def dailyTemperatures(self, temperatures: List[int]) -> List[int]:
        stack = []
        answer = [0] * len(temperatures)

        for i, temp in enumerate(temperatures): 

            while stack and temp > temperatures[stack[-1]]: 
                x = stack.pop()
                answer[x] = i - x 

            stack.append(i)

        return answer 

            



    
