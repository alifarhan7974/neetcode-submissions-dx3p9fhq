class Solution {
public:
    bool isValid(string s) {
        map<char, char> pairs = {
            {'{', '}'},
            {'[', ']'},
            {'(', ')'}
        };  

        stack<char> parentheses_stack;
        for (const char& bracket : s) { 
            if (pairs.count(bracket) > 0) { // Push open to stack
                parentheses_stack.push(bracket);
                //cout << "Pushing " << bracket << endl; 
            } 
            else { // Encounter closed bracket 
                if (parentheses_stack.empty()) { // Empty stack
                    return false; 
                }

                char last_in = parentheses_stack.top(); 
                parentheses_stack.pop();
                //cout << "Popping " << last_in << endl; 

                if (bracket != pairs[last_in]) { 
                    return false; 
                }
            }
        }   

        if (parentheses_stack.empty())  
            return true; 
        return false;
    }
};
