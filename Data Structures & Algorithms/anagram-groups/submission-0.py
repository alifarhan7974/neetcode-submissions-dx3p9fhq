from collections import Counter 
from collections import defaultdict
class Solution:
    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:
        lookup = defaultdict(list)
        counter_list = []

        for word in strs:
            frequency = Counter(word)
            if frequency in counter_list:
                # Let index of freq be key
                key = counter_list.index(frequency)
                lookup[key].append(word)
            else: 
                counter_list.append(frequency)
                lookup[len(counter_list) - 1].append(word)

        print(lookup)
        return [word_list for word_list in lookup.values()]        



