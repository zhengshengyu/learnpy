/**
 * Definition for binary tree
 * struct TreeNode {
 *     int val;
 *     TreeNode *left;
 *     TreeNode *right;
 *     TreeNode(int x) : val(x), left(NULL), right(NULL) {}
 * };
 */
class Solution {
public:
    TreeNode* reConstructBinaryTree(vector<int> pre,vector<int> vin) {
        return ConstructBinaryTree(pre, 0, pre.size()-1, vin, 0, vin.size()-1);
    }
    TreeNode* ConstructBinaryTree(vector<int> pre, int pre_b, int pre_e, vector<int> vin, int vin_b, int vin_e){
        if(pre_b > pre_e || vin_b > vin_e) //到底需不需要= ?
            return NULL;//return; ERROR
        int rootVal = pre[pre_b];
        int rootIndex = vin_b;
        for (; rootIndex <= vin_e; ++rootIndex)
        {
            if (vin[rootIndex]==rootVal)
            {
                break;
            }
        }
        int lchilds=rootIndex-vin_b;
        int rchilds=vin_e-rootIndex;
        TreeNode* pRoot = new TreeNode(rootVal); //是个数据结构，要自己创造
        pRoot->left=lchilds<=0 ? NULL : ConstructBinaryTree(pre, pre_b+1, pre_b+lchilds, vin, vin_b, rootIndex-1);
        pRoot->right=rchilds<=0 ? NULL : ConstructBinaryTree(pre, pre_b+lchilds+1, pre_e, vin, rootIndex+1, vin_e);
        return pRoot;//这个忘记就是煞笔了
    }
};