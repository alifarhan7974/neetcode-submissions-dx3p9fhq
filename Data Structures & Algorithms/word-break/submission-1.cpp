class Solution {
public:
    bool wordBreak(string s, vector<string>& wordDict) {
        int n = s.size();

        vector<bool> dp(n + 1, false);
        dp[n] = true;

        unordered_set<string> word_bank;
        for (string& word : wordDict) {
            word_bank.insert(word);
        }

        for (int start = n - 1; start >= 0; start--) {
            for (int end = start + 1; end <= n; end++) {
                string word = s.substr(start, end - start);

                if (word_bank.contains(word) && dp[end]) {
                    dp[start] = true;
                    break;
                }
            }
        }

        return dp[0];
    }
};