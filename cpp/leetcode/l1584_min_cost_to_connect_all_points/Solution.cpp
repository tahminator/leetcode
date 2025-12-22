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
        rank[pu]++;
      }
    }
};

class Adj {
public:
  int w;
  int p1;
  int p2;

  Adj(int _w, int _p1, int _p2) : w(_w), p1(_p1), p2(_p2) {}
};

class Solution {
public:
  int minCostConnectPoints(std::vector<std::vector<int>>& points) {
    std::vector<Adj> adjList;

    for (int i = 0; i < points.size(); i++) {
      for (int j = i + 1; j < points.size(); j++) {
        auto& pi = points[i], pj = points[j];
        int xi = pi[0], yi = pi[1], xj = pj[0], yj = pj[1];
        int d = std::abs(xi - xj) + std::abs(yi - yj);
        Adj adj(d, i, j);
        adjList.emplace_back(adj);
      }
    }

    std::sort(adjList.begin(), adjList.end(), [](Adj &larger, Adj &smaller) {
      return smaller.w > larger.w;
    });

    DisjointSet ds(points.size());

    int tw = 0;
    for (auto& adj : adjList) {
      if (ds.find(adj.p1) != ds.find(adj.p2)) {
        tw += adj.w;
        ds.join(adj.p1, adj.p2);
      }
    }

    return tw;
  }
};

