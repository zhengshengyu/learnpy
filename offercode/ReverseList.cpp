//输入一个链表，反转链表后，输出链表的所有元素。
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
    ListNode* ReverseList(ListNode* pHead) {
        if(pHead == NULL)
            return NULL;
        stack<ListNode*> sNode; // 利用栈
        ListNode* pCur=pHead;
        while(pCur!=NULL){
            sNode.push(pCur);
            pCur=pCur->next;
        }
        ListNode* pRoot = sNode.top();
        pCur = pRoot;
        while(!sNode.empty()){
            sNode.pop();
            if(sNode.empty())
                pCur->next = NULL;
            else{
                ListNode* pNext = sNode.top();
                pCur->next = pNext;
                pCur = pNext;
            }
        }
        return pRoot;
    }

    ListNode* ReverseList(ListNode* pHead) {
        if(pHead == NULL)
            return NULL;//0节点
        ListNode* pPre = NULL;
        ListNode* pCur = pHead;
        while(pCur->next != NULL){
            ListNode* pNext = pCur->next;
            pCur->next = pPre;
            pPre = pCur;
            if(pNext!=NULL)
                pCur = pNext;
        }
        pCur->next = pPre;
        return pCur;
    }

};