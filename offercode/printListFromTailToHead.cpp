/**
*  struct ListNode {
*        int val;
*        struct ListNode *next;
*        ListNode(int x) :
*              val(x), next(NULL) {
*        }
*  };
*/
class Solution {
public:
    vector<int> printListFromTailToHead(ListNode* head) {
        vector<int> vecValue;
        stack<int> staValue;
        ListNode* pRoot=head;
        while(pRoot!=NULL)
        {
            staValue.push(pRoot->val);
            pRoot = pRoot->next;
        }
        while(!staValue.empty())
        {
            vecValue.push_back(staValue.top());
            staValue.pop();
        }
        return vecValue;
    }
};