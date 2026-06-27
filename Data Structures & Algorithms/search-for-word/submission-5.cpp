class Solution {
public:
    bool exist(vector<vector<char>>& board, string word) {
        int rows = board.size(); 
        int cols = board[0].size(); 

        for (int r = 0; r < rows; r++) {
            for (int c = 0; c < cols; c++) {
                if (dfs(r, c, 0, word, board)) { 
                    return true;  
                }
            }
        }

        return false; 
    }

    bool dfs(int r, int c, int i, string& word, vector<vector<char>>& board) { 
        // base case 
        int rows = board.size(); 
        int cols = board[0].size(); 

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
            dfs(r + 1, c, i + 1, word, board) ||
            dfs(r - 1, c, i + 1, word, board) ||
            dfs(r, c + 1, i + 1, word, board) || 
            dfs(r, c - 1, i + 1, word, board) 
        );
        board[r][c] = temp; 
        return dfs_res; 
    }
};
