from collections import defaultdict
class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        counter = defaultdict(int)

        highest_freq = 0
        for num in nums:
            counter[num] += 1
        
        sorted_counter = dict(sorted(counter.items(), key=lambda pair : pair[1]))
        return [ list(sorted_counter)[-i] for i in range(1, k+1)]
