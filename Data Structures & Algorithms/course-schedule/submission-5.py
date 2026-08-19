from collections import defaultdict, deque

class Solution:
    def canFinish(self, numCourses: int, prerequisites: List[List[int]]) -> bool:
        graph = defaultdict(list) # prereq > courses it can unlock
        indegree = [0] * numCourses
        for a, b in prerequisites: 
            graph[b].append(a)
            indegree[a] += 1 

        queue = deque()
        count = 0 

        for i in range(numCourses): 
            if indegree[i] == 0: 
                queue.append(i)

        
        while queue: 
            x = queue.popleft()
            count += 1 

            for new_course in graph[x]: 
                indegree[new_course] -= 1 
                if indegree[new_course] == 0: 
                    queue.append(new_course)



        return count == numCourses






        



       
