class DisjointSet {
  std::vector<int> s;

public:
  DisjointSet(int n) : s(std::vector<int>(n, -1)) {}

  int find(int i) {
    if (s[i] < 0) {
      return i;
    }

    int par = find(s[i]);
    s[i] = par;
    return par;
  }

  bool join(int u, int v) {
    int pu = find(u), pv = find(v);
    int ru = s[pu], rv = s[pv];

    // same component already, return false.
    if (pu == pv) {
      return false;
    }

    // rank u larger
    if (ru < rv) {
      s[pu] = pv;
    // rank v larger
    } else if (ru > rv) {
      s[pv] = pu;
    } else {
      s[pu] = pv;
      s[pv]--;
    }

    return true;
  }

};

/**
 * the main thing to realize is that we can find the redundant connection when 
 * we try to connect two things together that are already connected. this also works 
 * because the constraint says that if there are "multiple answers", remove the last one.
 * this already happens due to how a disjoint set works (if there is PREIVOUSLY a connection, then we 
 * know our answer is this). 
 */
class Solution {
public:
  std::vector<int> findRedundantConnection(std::vector<std::vector<int>>& edges) {
    DisjointSet ds(edges.size() + 1);

    for (auto& edge : edges) {
      int src = edge[0], trg = edge[1];

      if (!ds.join(src, trg)) {
        return { src, trg };
      }
    }

    throw std::runtime_error("cant happen");
  }
};

