//输入一个链表，输出该链表中倒数第k个结点。
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
    ListNode* FindKthToTail(ListNode* pListHead, unsigned int k) {
        if(pListHead==NULL)
            return NULL;
        ListNode* pFirst=pListHead;
        ListNode* pSecond=pListHead;
        for (unsigned int i = 0; i < k; ++i)
        {
            if(pFirst==NULL)
                return NULL;
            pFirst=pFirst->next;
        }
        while(pFirst!=NULL){
            pFirst=pFirst->next;
            pSecond=pSecond->next;
        }
        return pSecond;
    }
};