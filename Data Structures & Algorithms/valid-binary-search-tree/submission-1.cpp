/**
 * Definition for a binary tree node.
 * struct TreeNode {
 *     int val;
 *     TreeNode *left;
 *     TreeNode *right;
 *     TreeNode() : val(0), left(nullptr), right(nullptr) {}
 *     TreeNode(int x) : val(x), left(nullptr), right(nullptr) {}
 *     TreeNode(int x, TreeNode *left, TreeNode *right) : val(x), left(left), right(right) {}
 * };
 */


class Solution {
public:
    bool isValidBST(TreeNode* root) {
        int pos_inf = numeric_limits<int>::max(); 
        int neg_inf = numeric_limits<int>::min(); 
        return helper(root, neg_inf, pos_inf);
    }

    bool helper(TreeNode* node, int min_val, int max_val) { 
        if (node == nullptr) { 
            return true; 
        }

        if (!(min_val < node->val && node->val < max_val)) { 
            return false; 
        }

        return helper(node->left, min_val, node->val)
            && helper(node->right, node->val, max_val); 

    }
};
