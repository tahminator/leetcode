#define ll long long

class Solution {
public:
  int countPaths(int N, std::vector<std::vector<int>>& roads) {
    std::unordered_map<int, std::vector<std::pair<int, int>>> adjList;

    for (auto& road : roads) {
      int u = road[0], v = road[1], w = road[2];
      adjList[u].push_back({v, w});
      adjList[v].push_back({u, w}); // undirected, do both
    }

    std::vector<ll> dst(N, LLONG_MAX);

    // this is the secret sauce right here. we can calculate the different paths depending on 
    // the distance of what we r currently looking at.
    std::vector<int> ways(N);

    std::priority_queue<
      std::pair<ll, int>,
      std::vector<std::pair<ll, int>>,
      std::greater<std::pair<ll, int>>
    > q;

    q.emplace(0, 0);
    dst[0] = 0;
    ways[0] = 1; // start, nowhere to go.

    while (!q.empty()) {
      auto [d, v] = q.top();
      q.pop();

      // not a shortest path
      if (d > dst[v]) continue;

      for (auto [n, t] : adjList[v]) {
        if (dst[v] + t < dst[n]) {
          dst[n] = dst[v] + t;
          ways[n] = ways[v];
          q.emplace(dst[n], n);
        } else if (dst[v] + t == dst[n]) {
          ways[n] = (ways[n] + ways[v]) % static_cast<int>(1e9 + 7);
        }
      }
    }

    return ways[N - 1];
  }
};
