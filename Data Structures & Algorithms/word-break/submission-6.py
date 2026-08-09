class Solution:
    def wordBreak(self, s: str, wordDict: List[str]) -> bool:
        wordbank = set(wordDict) # O(1) lookup 
        n = len(s)
        memo = set() # Indexes that dont work 

        # Can we solve from this index 
        # Reach end done 
        def dfs(start): 
            print(f"start: {start}")
            if start == n: 
                return True  

            # Check memo 
            if start in memo: 
                return False 

            for i in range(start + 1, n + 1): 
                if s[start:i] in wordbank: 
                    if dfs(i): 
                        return True 

            memo.add(start) 
            return False 

        return dfs(0)
            

       

        