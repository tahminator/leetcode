class DisjointSet {
  std::vector<int> parent;
  std::vector<int> rank;

  public:
    DisjointSet(int n) {
      // 0 is ignored
      rank.resize(n + 1);
      parent.resize(n + 1);

      for (int i = 1; i <= n; i++) {
        parent[i] = i;
        rank[i] = 0;
      }
    }

    int find(int i) {
      if (parent[i] == i) {
        return i;
      }

      int p = find(parent[i]);
      parent[i] = p;
      return p;
    }

    void join(int u, int v) {
      int pu = find(u);
      int pv = find(v);

      int ru = rank[pu];
      int rv = rank[pv];

      if (ru < rv) {
        parent[pu] = pv;
      } else if (ru > rv) {
        parent[pv] = pu;
      } else {
        parent[pv] = pu;
        rank[rv]++;
      }
    }
};

class Solution {
  public:
    /**
    * example:
    *
    * [
    *   [1,1,0],
    *   [1,1,0],
    *   [0,0,1]
    * ]
    *
    * which means (l to r):
    * c1 -> c1
    * c1 -> c2
    * c2 -> c1
    * c2 -> c2
    * c3 -> c3
    *
    * first of all, identity connections everywhere (they can be ignored).
    */
    int findCircleNum(std::vector<std::vector<int>>& isConnected) {
      // i == j == n
      DisjointSet ds(isConnected.size());

      for (int city = 0; city < isConnected.size(); city++) {
        auto& conns = isConnected[city];

        std::cout << std::endl;
        for (int connCity = 0; connCity < conns.size(); connCity++) {
          if (connCity == city) continue;

          auto conn = conns[connCity];
          if (conn == 1) {
            ds.join(city + 1, connCity + 1);
          }
        }
      }

      std::unordered_set<int> seen;
      for (int city = 1; city <= isConnected.size(); city++) {
        seen.emplace(ds.find(city));
      }

      return seen.size();
    }
};
