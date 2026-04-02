class Solution {
public:
    int evalRPN(vector<string>& tokens) {
        const unordered_set<string> operators = {"+", "-", "*", "/"};
        stack<int> nums; 
        for (string& item : tokens) { 
            if (operators.count(item) > 0) { // item is an operator 
                int y = nums.top(); 
                nums.pop(); 
                int x = nums.top(); 
                nums.pop();

                if (item == "+")
                    nums.push(x + y); 
                else if (item == "-")
                    nums.push(x - y); 
                else if (item == "*")
                    nums.push(x * y); 
                else 
                    nums.push(x / y); 
            }
            else { // item is a number
                int num = stoi(item); 
                nums.push(num);
            }
            
        }
        return nums.top();
    }
};
