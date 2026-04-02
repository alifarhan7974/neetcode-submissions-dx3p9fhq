class Solution:
    def lengthOfLongestSubstring(self, s: str) -> int:
        l = 0
        current_substring = set()
        longest_substring = 0

        for r in range(len(s)):
            while s[r] in current_substring:
                current_substring.remove(s[l])
                l += 1

            current_substring.add(s[r])
            longest_substring = max(
                longest_substring,
                len(current_substring)
            )

        return longest_substring
            
            
            
