struct DoublyListNode {
    int key;
    int val;
    DoublyListNode *prev;
    DoublyListNode *next;
    DoublyListNode() : key(0), val(0), next(nullptr) {}
    DoublyListNode(int key, int x) : key(key), val(x), next(nullptr), prev(nullptr) {}
    DoublyListNode(int key, int x, DoublyListNode *next) : key(key), val(x), next(next) {}
    DoublyListNode(int key, int x, DoublyListNode *prev, DoublyListNode *next) : key(key), val(x), next(next) {}
};

void print_list(DoublyListNode* node) {
  auto c = node;

  std::print("list: ");
  while (c != nullptr) {
    std::print("{} ", c->val);
    c = c->next;
  }
  std::println();
}

class LRUCache {
private:
  std::unordered_map<int, DoublyListNode*> data_store;
  DoublyListNode* store_head;
  DoublyListNode* store_tail;
  int store_size;
  int capacity;

public:
  LRUCache(int capacity) : store_head(nullptr), store_tail(nullptr), store_size(0), capacity(capacity) {
  }

  int get(int key) {
    // std::println("running get on {}", key);
    if (data_store.contains(key)) {
      auto& node = data_store.at(key);
      // print_list(node);
      if (node->next != nullptr) {
        auto prev = node->prev;
        auto next = node->next;
        next->prev = prev;
        if (prev != nullptr) {
            prev->next = next;
        } else {
            store_head = next;
            store_head->prev = nullptr;
        }


        store_tail->next = node;
        node->prev = store_tail;
        node->next = nullptr;
        store_tail = store_tail->next;
      }
      // print_list(store_head);
      return data_store.at(key)->val;
    }

    return -1;
  }

  void put(int key, int value) {
    // std::println("running put on {}:{}", key, value);
    if (data_store.contains(key)) {
      auto& node = data_store.at(key);
      if (node->next != nullptr) {
        auto prev = node->prev;
        auto next = node->next;
        if (prev != nullptr) {
            prev->next = next;
        } else {
            store_head = next;
        }
        next->prev = prev;

        store_tail->next = node;
        node->prev = store_tail;
        node->next = nullptr;
        store_tail = node;
      }

      node->val = value;
    } else {
      if (store_size + 1 > capacity) {
        // print_list(store_head);
        auto head = store_head;

        store_head = store_head->next;
        if (store_head != nullptr) {
          store_head->prev = nullptr;
        } else {
          store_tail = nullptr;
        }
        // std::println("deleting from data_store key of {}", head->key);
        data_store.erase(head->key);
        // std::cout << "{";
        for (const auto& [x, y] : data_store) {
          // std::print("{}:{},", x, y->val);
        }
        // std::cout << "}\n";

        delete head;
        store_size--;

        // print_list(store_head);
      }

      DoublyListNode* node = new DoublyListNode(key, value);

      if (store_head == nullptr) {
        store_head = node;
        store_tail = node;
      } else {
        store_tail->next = node;
        node->prev = store_tail;
        store_tail = node;
      }

      store_size++;
      data_store[key] = node;
    }

    // std::println("put for {}:{} finished with store_size of {}", key, value, store_size);
    // print_list(store_head);
  }
};

/**
 * Your LRUCache object will be instantiated and called as such:
 * LRUCache* obj = new LRUCache(capacity);
 * int param_1 = obj->get(key);
 * obj->put(key,value);
 */
