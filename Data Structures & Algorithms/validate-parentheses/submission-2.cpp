class Solution {
public:
    bool isValid(string s) {
        unordered_map<char, char> pairs = {
        {')', '('},
        {']', '['},
        {'}', '{'}
    };

        stack<char> parentheses_stack;

        for (char bracket : s) { 
            if (pairs.count(bracket) == 0) { 
                // Opening bracket
                parentheses_stack.push(bracket);
            } 

            else { // Encounter closed bracket     open                 closed
                if (parentheses_stack.empty() || parentheses_stack.top() != pairs[bracket])
                    return false;
                parentheses_stack.pop(); 
            }
        }   
        return parentheses_stack.empty();
    }
};
