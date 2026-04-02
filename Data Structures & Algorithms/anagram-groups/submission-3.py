from collections import defaultdict

class Solution:
    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:
        groups = defaultdict(list) 

        for word in strs: 
            count = [0] * 26 

            for c in word: 
                if 'a' <= c <= 'z': 
                    count[ord(c) - ord('a')] += 1    

            hashable_count = tuple(count) 
            groups[hashable_count].append(word)
            #print(groups.values())

        return list(groups.values()) 
        










