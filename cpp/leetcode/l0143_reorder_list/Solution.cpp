// leetcode mobile

/**
 * Definition for singly-linked list.
 * struct ListNode {
 *     int val;
 *     ListNode *next;
 *     ListNode() : val(0), next(nullptr) {}
 *     ListNode(int x) : val(x), next(nullptr) {}
 *     ListNode(int x, ListNode *next) : val(x), next(next) {}
 * };
 */
class Solution {
private:
    void print_list(ListNode* head) {
        auto c = head;
        std::cout << "list: ";
        while (c != nullptr) {
            std::print("{} ", c->val);
            c = c->next;
        }
        std::println();
    }
    
    ListNode* travel_to(ListNode* head, int i) {
        auto c = head;
        int _i = 0;
        while (c != nullptr && _i != i) {
            c = c-> next;
            _i++;
        }
        
        return c;
    }
public:
    void reorderList(ListNode* head) {
        int n = 0;
        
        auto c = head;
        while (c != nullptr) {
            n++;
            c = c->next;
        }
        
        int nhalf = (n + 1) / 2;
        auto nhalfconn_node = travel_to(head, nhalf - 1);
        auto nhalf_node = travel_to(head, nhalf);
        
        ListNode* prev = nullptr;
        c = nhalf_node;
        nhalfconn_node->next = nullptr;
        
        ListNode* last = nullptr;
        while (c != nullptr) {
            if (c->next == nullptr) {
                last = c;
            }
            auto cnext = c->next;
            
            c->next = prev;
            prev = c;
            
            c = cnext;
        }
        
        auto l = head, r = last;

        while (r != nullptr) {
            auto lnext = l->next;
            auto rnext = r->next;
    
            l->next = r;
            r->next = lnext;
    
            l = lnext;
            r = rnext;
        }
    }
};
