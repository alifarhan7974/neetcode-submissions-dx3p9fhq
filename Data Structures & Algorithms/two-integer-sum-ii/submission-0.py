class Solution:
    def twoSum(self, numbers: List[int], target: int) -> List[int]:
        lookup = {} 

        for i, v in enumerate(numbers):
            difference = target - numbers[i]
            if difference in lookup:
                return [lookup[difference]+1, i+1]
            else:
                lookup[v] = i 
        return []

            