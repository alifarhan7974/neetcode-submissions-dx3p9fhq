class Solution {
public:
    vector<int> findOrder(int numCourses, vector<vector<int>>& prerequisites) {
        // Adjaceny graph with index are preq 
        // Building graph 
        vector<vector<int>> graph(numCourses); 
        vector<int> indegree(numCourses, 0); 

        for (auto& p : prerequisites) { 
            int a = p[0]; int b = p[1]; 
            graph[b].push_back(a);
            indegree[a]++; 
        }

        // Push nodes with in degree 0 
        queue<int> q; 
        for (int i = 0; i < numCourses; i++) { 
            if (indegree[i] == 0) { 
                q.push(i); 
            }
        }

        // BFS 
        vector<int> order; 
        while (!q.empty()) {
            int course = q.front(); 
            q.pop(); 
            order.push_back(course); 

            for (int neighbor : graph[course]) { 
                indegree[neighbor]--; 
                if (indegree[neighbor] == 0) { 
                    q.push(neighbor); 
                }
            }
        }

        // Check if order is valid 
        if (size(order) == numCourses) { 
            return order; 
        }

        return {}; 

        
    }
};
