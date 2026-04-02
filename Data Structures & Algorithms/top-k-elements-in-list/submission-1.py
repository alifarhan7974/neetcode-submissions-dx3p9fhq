from collections import defaultdict
class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        counter = defaultdict(int)

        for num in nums:
            counter[num] += 1
        
        sorted_counter = sorted(counter.items(), key=lambda pair : pair[1])
        return [list(sorted_counter)[-i][0] for i in range(1, k+1)]
