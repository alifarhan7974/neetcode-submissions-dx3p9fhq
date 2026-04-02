class Solution {
public:
    bool isValid(string s) {
        unordered_map<char, char> pairs = {
            {'{' , '}'}, 
            {'(' , ')'}, 
            {'[' , ']'}
        };

        stack<char> open_stack; 

        for (int i = 0; i < s.size(); i++) {
            // Open bracket case 
            if (pairs.find(s[i]) != pairs.end()) {
                open_stack.push(s[i]); 
            }
            // Closing bracket
            else {
                if (!open_stack.empty()) {
                    char opening = open_stack.top(); 
                    open_stack.pop();
                    if (pairs[opening] != s[i]) {
                        return false; 
                    }
                    
                } else {
                    return false; 
                }

            }
        }

        if (open_stack.empty()) {
            return true; 
        }
        return false; 
            
    }
};
