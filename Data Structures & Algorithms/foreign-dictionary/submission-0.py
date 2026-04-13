from collections import defaultdict, deque

class Solution:
    def foreignDictionary(self, words: List[str]) -> str:
        graph = defaultdict(list)
        indegree = {} 
        
        # set up indegree
        for word in words: 
            for c in word: 
                indegree[c] = 0

        # build graph 
        for i in range(len(words) - 1): 
            word1 = words[i]
            word2 = words[i + 1]

            j = 0 
            while j < len(word1) and j < len(word2) and word1[j] == word2[j]:
                j += 1  

            # Edge case shorter word comes first if share a prefix 
            # If shorter word is second return ''
            if j == len(word2) and len(word1) > len(word2): 
                return ""

            # Make sure both words in bounds 
            if j < len(word1) and j < len(word2): 
                if word2[j] not in graph[word1[j]]:
                    graph[word1[j]].append(word2[j])
                    indegree[word2[j]] += 1 

        queue = deque([c for c in indegree if indegree[c] == 0])
        order = []
        
        # BFS
        while queue: 
            char = queue.popleft()
            order.append(char)

            for neighbor in graph[char]: 
                indegree[neighbor] -= 1
                if indegree[neighbor] == 0:
                    queue.append(neighbor)


        return "".join(order) if len(order) == len(indegree) else ""











        