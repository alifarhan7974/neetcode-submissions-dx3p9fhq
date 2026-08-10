from collections import defaultdict 
class Solution:
    def dailyTemperatures(self, temperatures: List[int]) -> List[int]:
        temp_map = {i : 0 for i in range(len(temperatures))}
        stack = [] 

        for i in range(len(temperatures)):
            while stack and temperatures[i] > temperatures[stack[-1]]: 
                j = stack.pop()
                temp_map[j] = i - j 

            stack.append(i) 

        return [temp_map[i] for i in range(len(temperatures))]
                
