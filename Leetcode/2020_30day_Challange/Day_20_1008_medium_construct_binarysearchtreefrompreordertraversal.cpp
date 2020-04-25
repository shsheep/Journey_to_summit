/**
 * Definition for a binary tree node.
 * struct TreeNode {
 *     int val;
 *     TreeNode *left;
 *     TreeNode *right;
 *     TreeNode(int x) : val(x), left(NULL), right(NULL) {}
 * };
 */
class Solution {
public:
    TreeNode* addNode(TreeNode* root, int val) {
        if (!root)
            return new TreeNode(val);
        else if (root->val < val)
            root->right = addNode(root->right, val);
        else
            root->left = addNode(root->left, val);
        
        return root;
    }
    
    TreeNode* bstFromPreorder(vector<int>& preorder) {
        TreeNode* root = NULL;
        for (int i=0; i<preorder.size(); ++i)
            root = addNode(root, preorder[i]);
        return root;
    }
};

/**
 * Runtime: 4 ms, faster than 85.15% of C++ online submissions for Construct Binary Search Tree from Preorder Traversal.
 * Memory Usage: 11.8 MB, less than 9.52% of C++ online submissions for Construct Binary Search Tree from Preorder Traversal.
 **/
