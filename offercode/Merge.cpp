//输入两个单调递增的链表，输出两个链表合成后的链表，当然我们需要合成后的链表满足单调不减规则。
/*
struct ListNode {
    int val;
    struct ListNode *next;
    ListNode(int x) :
            val(x), next(NULL) {
    }
};*/
class Solution {
public:
    ListNode* Merge(ListNode* pHead1, ListNode* pHead2)
    {
        ListNode* pMerge = new ListNode();
        while(pHead1!=NULL && pHead2!=NULL){
            ListNode* pTemp = NULL;
            if (pHead1->val <= pHead2->val)
            {
                pTemp = pHead1;
                pHead1 = pHead1->next;
            }
            else{
                pTemp = pHead2;
                pHead2 = pHead2->next;
            }
            pTemp->next = NULL;
            pMerge = pTemp;
        }
    }
};