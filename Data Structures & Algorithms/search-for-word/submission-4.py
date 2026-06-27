class Solution:
    def exist(self, board: List[List[str]], word: str) -> bool:
        rows, cols = len(board), len(board[0])

        def dfs(r, c, word): 
            # Base case 
            if word == "":
                return True
            
            # Valid index 
            if not (0 <= r < rows and 0 <= c < cols): 
                return False

            # Check visited
            if board[r][c] == "0": 
                return False 

            # Curr letter is valid 
            if board[r][c] == word[0]: 
                temp = board[r][c]
                board[r][c] = "0"
                dfs_res = (
                    dfs(r + 1, c, word[1:]) or 
                    dfs(r - 1, c, word[1:]) or
                    dfs(r, c + 1, word[1:]) or 
                    dfs(r, c - 1, word[1:])
                )
                board[r][c] = temp
                return dfs_res

            return False 

        for r in range(rows): 
            for c in range(cols): 
                if board[r][c] == word[0]:
                    if dfs(r, c, word[:]): # Pass in copy so og is unchanged
                        return True 

        return False 

