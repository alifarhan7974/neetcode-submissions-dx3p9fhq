class Solution {
public:
    int rows, cols;
    vector<vector<char>> board; 
    string word; 

    bool exist(vector<vector<char>>& b, string w) {
        board = b; 
        word = w; 
        
        rows = board.size(); 
        cols = board[0].size(); 

        for (int r = 0; r < rows; r++) {
            for (int c = 0; c < cols; c++) {
                if (dfs(r, c, 0)) { 
                    return true;  
                }
            }
        }

        return false; 
    }

    bool dfs(int r, int c, int i) { 
        // base case 
        if (i == word.size()) { 
            return true; 
        } 

        // out of bounds 
        if (r < 0 || r >= rows || c < 0 || c >= cols) { 
            return false; 
        }

        if (board[r][c] != word[i]) { 
            return false; 
        }

        char temp = board[r][c]; 
        board[r][c] = '#'; // visited 
        bool dfs_res = (
            dfs(r + 1, c, i + 1) ||
            dfs(r - 1, c, i + 1) ||
            dfs(r, c + 1, i + 1) || 
            dfs(r, c - 1, i + 1) 
        );
        board[r][c] = temp; 
        return dfs_res; 
    }
};
