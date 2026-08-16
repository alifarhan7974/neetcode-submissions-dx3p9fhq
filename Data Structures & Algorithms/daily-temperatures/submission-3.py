from collections import defaultdict 
class Solution:
    def dailyTemperatures(self, temperatures: List[int]) -> List[int]:
        stack = []
        answer = [0] * len(temperatures) # Each index corresponds to temp index 

        for i in range(len(temperatures)): 
            # Monotonic stack holdes index that are less
            while stack and temperatures[i] > temperatures[stack[-1]]: 
                x = stack.pop()
                answer[x] = i - x 

            stack.append(i)



        return answer
