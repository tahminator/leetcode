struct Cmp {
  bool operator()(ListNode* a, ListNode* b) {
    return std::greater{}(a->val, b->val);
  }
};

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
public:
  ListNode* mergeKLists(vector<ListNode*>& lists) {
    int n = lists.size();
    ListNode* res_head = new ListNode();
    ListNode* res = res_head;

    std::priority_queue<ListNode*, std::vector<ListNode*>, Cmp> pq;

    bool done = false;
    while (!done) {
      int emptys = 0;

      for (int i = 0; i < n; i++) {
        auto& list = lists[i];
        if (list == nullptr) {
          emptys++;
          continue;
        }

        pq.emplace(list);
        lists[i] = lists[i]->next;
      }

      if (emptys == n) {
        done = true;
      }
    }

    while (!pq.empty()) {
      res->next = new ListNode();
      res = res->next;

      auto& top = pq.top();

      res->val = top->val;

      pq.pop();
    }

    return res_head->next;
  }
};
