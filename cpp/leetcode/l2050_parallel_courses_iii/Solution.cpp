#include <queue>
#include <vector>

class Solution {
public:
  /**
   * this is obvi going to need kahn's algorithm, but for each jump to the next "course"
   * we need to consider the max(parents) because we have to wait for all requirements before we can move forward.
   *
   * im thinking that we could probably combine kahn's with djikstra's where we keep track of the distance as we drag along.
   * at the end, we just need to find the max elem of that array
   *
   * and at the end, we can just sum the times of each.
   */
  int minimumTime(int n, std::vector<std::vector<int>>& relations, std::vector<int>& time) {
    std::vector<std::vector<int>> postreqs(n + 1, std::vector<int>());
    std::vector<int> prereqs(n + 1, 0);
    std::vector<int> elapsed(n + 1, -1);
    int totalElapsed = 0;

    for (auto& relation : relations) {
      int prev = relation[0], next = relation[1];
      prereqs[next]++;
      postreqs[prev].emplace_back(next);
    }

    std::queue<int> q;

    for (int course = 1; course < prereqs.size(); course++) {
      int cnt = prereqs[course];
      if (cnt == 0) {
        q.emplace(course);
        elapsed[course] = time[course - 1];
      }
    }

    while (!q.empty()) {
      int course = q.front();
      q.pop();

      auto& children = postreqs[course];

      for (int child : children) {
        elapsed[child] = std::max(elapsed[course] + time[child - 1], elapsed[child]);
        int rem = --prereqs[child];
        if (rem == 0) {
          q.emplace(child);
        }
      }
    }

    return *std::max_element(elapsed.begin(), elapsed.end());
  }
};

int main() {
  Solution s;
  std::vector<std::vector<int>> relations = {{ 1, 3 }, {2, 3}};
  std::vector<int> time = {3, 2, 5};
  s.minimumTime(3, relations, time);
}
