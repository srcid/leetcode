#include<iostream>
#include<limits>

struct ListNode {
    int val;
    ListNode *next;
    ListNode() : val(0), next(nullptr) {}
    ListNode(int x) : val(x), next(nullptr) {}
    ListNode(int x, ListNode *next) : val(x), next(next) {}
};

class Solution {
public:
    int getVal(ListNode* node) {
        return node != nullptr
            ? node->val 
            : std::numeric_limits<int>::min();
    }

    ListNode* mergeTwoLists3(ListNode* list1, ListNode* list2) {
        if (list1 == nullptr) {
            return list2;
        } 
        if (list2 == nullptr) {
            return list1;
        }

        if (list1->val < list2->val ) {
            return new ListNode(list1->val, mergeTwoLists3(list1->next, list2));
        }
        return new ListNode(list2->val, mergeTwoLists3(list1, list2->next));
    }

    ListNode* mergeTwoLists2(ListNode* list1, ListNode* list2) {
        ListNode* listMergedRoot = nullptr;
        ListNode* listMerged = listMergedRoot;
        int val;

        while (list1 != nullptr || list2 != nullptr) {
            if (getVal(list1) < getVal(list2)) {
                val = list1->val;
                list1 = list1->next;
            } else {
                val = list2->val;
                list2 = list2->next;
            }

            if (listMerged == nullptr) {
                listMerged = new ListNode(val);
                listMergedRoot = listMerged;
            } else {
                listMerged->next = new ListNode(val);
                listMerged = listMerged->next;
            }
        }

        return listMergedRoot;
    }

    ListNode* mergeTwoLists1(ListNode* list1, ListNode* list2) {
        ListNode* listMergedRoot = nullptr;
        ListNode* listMerged = listMergedRoot;
        int val;

        while (list1 != nullptr && list2 != nullptr) {
            if (list1->val < list2->val) {
                val = list1->val;
                list1 = list1->next;
            } else {
                val = list2->val;
                list2 = list2->next;
            }

            if (listMerged == nullptr) {
                listMerged = new ListNode(val);
                listMergedRoot = listMerged;
            } else {
                listMerged->next = new ListNode(val);
                listMerged = listMerged->next;
            }
        }

        if (listMerged == nullptr) {
            if (list1 != nullptr) {
                listMerged = list1;
            } else if (list2 != nullptr) {
                listMerged = list2;
            }
            listMergedRoot = listMerged;
        } else {
            if (list1 != nullptr) {
                listMerged->next = list1;
            } else if (list2 != nullptr) {
                listMerged->next = list2;
            }
        }

        return listMergedRoot;
    }
};