class Solution {
    int longest_word = 0; 
    int start = 0; 
public:
    string longestPalindrome(string s) {
        for (int i = 0; i < s.size(); i++) { 
            expand(i, i, s); // Odd case 
            expand(i, i + 1, s); // Even case 
        }

        return s.substr(start, longest_word); 
    }

    void expand(int l, int r, const string& s) { 
        while (l >= 0 && r < s.size() && s[l] == s[r]) { 
            l--;
            r++; 
        }

        if (r - l > longest_word) { 
            longest_word = r - l - 1; 
            start = l + 1; 
        }
    }


};
