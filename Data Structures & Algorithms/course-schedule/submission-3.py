from collections import defaultdict
class Solution:
    def canFinish(self, numCourses: int, prerequisites: List[List[int]]) -> bool:
        indegree = [0] * numCourses
        graph = defaultdict(list)

        for post, pre in prerequisites: 
            graph[post].append(pre)
            indegree[post] += 1 

        state = [0 for i in range(numCourses)]
        # 0 = not visited havent done any prereqs 
        # 1 = visiting currently doing prereqas 
        # 2 = finished all prereqs 

        def dfs(i): 
            # Done all prereqs 
            if state[i] == 2: 
                return True 
            
            # Not done w prereqs 
            if state[i] == 1: 
                return False  
            
            # currently visiting 
            state[i] = 1 

            for pre_req in graph[i]: 
                if not dfs(pre_req): 
                    return False  


            state[i] = 2 # explored all preqs can take now 
            return True 

        for i in range(numCourses): 
            if not dfs(i): 
                return False 


        return True 


       
