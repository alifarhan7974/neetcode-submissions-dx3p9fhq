class Solution {
public:
    int numDecodings(string s) {
        int n = s.size(); 
        int next1 = 1; // dp[i + 1] 
        int next2 = 0; // dp[i + 2]
        
        for (int i = n - 1; i >= 0; i--) { 
            int curr = 0;

            if (s[i] != '0') { 
                curr += next1;
            } 

            if (i + 1 < n) { 
                int twodigit = 10 * (s[i] - '0') + (s[i+1] - '0');

                if (10 <= twodigit && twodigit <= 26) { 
                    curr += next2; 
                } 
            }

            next2 = next1; 
            next1 = curr; 
        }

        return next1;

    }
};
