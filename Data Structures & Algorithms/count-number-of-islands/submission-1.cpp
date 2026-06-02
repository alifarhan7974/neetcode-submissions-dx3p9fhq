class Solution {
public:
    int numIslands(vector<vector<char>>& grid) {
        int rows = size(grid);
        int cols = size(grid[0]); 

        int count = 0; 

        for (int r = 0; r < rows; r++) { 
            for (int c = 0; c < cols; c++) { 
                if (grid[r][c] == '1') { 
                    count++; 
                    dfs(r, c, grid); 
                }
            }
        }

        return count;
    }

    void dfs(int r, int c, vector<vector<char>>& grid) { 
        int rows = size(grid); 
        int cols = size(grid[0]); 
        if (r >= 0 && r < rows && c >= 0 && c < cols && grid[r][c] == '1' && grid[r][c] == '1') { 
                grid[r][c] = '0'; 
                dfs(r + 1, c, grid); 
                dfs(r - 1, c, grid); 
                dfs(r, c + 1, grid); 
                dfs(r, c - 1, grid);
            } 
    
    }
};
