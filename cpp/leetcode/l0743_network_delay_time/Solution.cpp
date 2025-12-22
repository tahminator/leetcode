class Solution {
public:
  int networkDelayTime(vector<vector<int>>& times, int n, int k) {
    std::unordered_map<int, std::vector<std::pair<int, int>>> adjList;

    for (auto& time : times) {
      int src = time[0], trg = time[1], w = time[2];
      adjList[src].push_back({w, trg});
    }

    std::priority_queue<
      std::pair<int, int>,
      std::vector<std::pair<int, int>>,
      std::greater<std::pair<int, int>>
    > q;

    // 0 is skipped.
    std::vector<int> dist(n + 1, INT_MAX);

    int startNode = k;
    auto first = std::pair<int, int>(0, startNode);
    dist[startNode] = 0;
    q.emplace(first);

    while (!q.empty()) {
      int w = q.top().first;
      int n = q.top().second;
      q.pop();

      if (w > dist[n]) continue;

      for (const auto& [cw, cn] : adjList[n]) {
        if (cw + w <= dist[cn]) {
          dist[cn] = cw + w;
          q.push({ cw + w, cn });
        }
      }
    }

    int max = -1;
    for (int i = 1; i < dist.size(); i++) {
      int d = dist[i];
      if (d == INT_MAX) {
        return -1;
      }
      max = std::max(max, d);
    }

    return max;
  }
};
