from collections import defaultdict, deque
class Solution:
    def findOrder(self, numCourses: int, prerequisites: List[List[int]]) -> List[int]:
        # Implementing Khan's algorithim 
        graph = defaultdict(list)
        indegree = [0] * numCourses

        for a, b in prerequisites: 
            graph[b].append(a)
            indegree[a] += 1 

        queue = deque()
        for i in range(numCourses): 
            if indegree[i] == 0:
                queue.append(i)

        order = [] 

        # queue = courses ready to take 
        # indegree = how many prereqs left 
        while queue: 
            course = queue.popleft()
            order.append(course)

            for neighbor in graph[course]: 
                indegree[neighbor] -= 1 
                if indegree[neighbor] == 0:
                    queue.append(neighbor)

        return order if len(order) == numCourses else [] 


