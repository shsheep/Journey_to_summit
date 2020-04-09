/**
 * Definition for singly-linked list.
 * struct ListNode {
 *     int val;
 *     ListNode *next;
 *     ListNode(int x) : val(x), next(NULL) {}
 * };
 */
class Solution {
public:
    ListNode* middleNode(ListNode* head) {
        int length = 0, middle;
        ListNode* node = head;
        while (node) {
            ++length;
            node = node->next;
        }
        middle = (int)(length/2);
        while (middle--)
            head = head->next;
        return head;
    }
};

/*
 * Runtime: 0 ms, faster than 100.00% of C++ online submissions for Middle of the Linked List.
 * Memory Usage: 6.6 MB, less than 100.00% of C++ online submissions for Middle of the Linked List.
 */
