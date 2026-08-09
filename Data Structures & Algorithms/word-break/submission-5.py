class Solution:
    def wordBreak(self, s: str, wordDict: List[str]) -> bool:
        wordbank = set(wordDict) # O(1) lookup 
        n = len(s)
        memo = defaultdict(bool)

        # Can we solve from this index 
        # Reach end done 
        def dfs(start): 
            print(f"start: {start}")
            if start == n: 
                return True  

            # Check memo 
            if start in memo and memo[start] == False: 
                return False  

            for i in range(start, n + 1): 
                if s[start:i] in wordbank: 
                    if dfs(i): 
                        return True 
                    else: 
                        memo[i] = False 

            memo[start] = False 
            return False 

        return dfs(0)
            

       

        