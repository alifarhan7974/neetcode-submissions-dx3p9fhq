from collections import defaultdict

class Solution:
    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:
        groups = defaultdict(list) 

        for word in strs: 
            count = [0] * 26 

            for c in word: 
                if 'a' <= c <= 'z': 
                    count[ord(c) - ord('a')] += 1    

            groups[tuple(count)].append(word)

        return list(groups.values()) 
        










