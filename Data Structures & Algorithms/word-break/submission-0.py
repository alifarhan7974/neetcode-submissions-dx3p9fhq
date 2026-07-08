class Solution:
    def wordBreak(self, s: str, wordDict: List[str]) -> bool:
        wordbank = set(wordDict)
        memo = {}

        # can i break whole thing from this index 
        def can_break(start): 
            if start == len(s): 
                return True 

            if start in memo: 
                return memo[start]

            for end in range(start + 1, len(s) + 1): 
                word = s[start:end]

                if word in wordbank and can_break(end): 
                    memo[start] = True 
                    return True 
                    

            memo[start] = False 
            return False

        return can_break(0) 
                    


        