class Solution:
    def canFinish(self, numCourses: int, prerequisites: List[List[int]]) -> bool:
        graph = {i : [] for i in range(numCourses)}

        # must take b before a 
        for a, b in prerequisites: 
            graph[b].append(a) 

        # 0 unvisted
        # 1 visiting
        # 2 visited 
        state = [0] * numCourses 

        def dfs(course): 
            # cycle detected 
            if state[course] == 1:
                return False

            # already processed  
            if state[course] == 2: 
                return True  

            state[course] = 1 

            for neighbor in graph[course]: 
                if not dfs(neighbor):
                    return False 

            state[course] = 2 
            return True 

        for i in range(numCourses):
            if not dfs(i):
                return False 

        return True 
