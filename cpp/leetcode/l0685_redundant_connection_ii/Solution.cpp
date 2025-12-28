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
 * disjoint set doesnt work for directed graphs since it has no concept of an indegree or outdegree.
 *
 * BUT, we can get really hacky & use one of the "side effects" of disjoint set: it can tell us when 
 * we try to add two vertices that are already connected.
 *
 * but this only handles one case, where we have cyclic graph. the other issue is that we might have an extra node 
 * which causes u -> v to happen twice. this obviously needs to be the one that's removed. what we can do is maintain an extra 
 * array, loop edges and update this array. if we try to update it twice, we know the current parent and next parent.
 */
class Solution {
public:
  std::vector<int> findRedundantDirectedConnection(std::vector<std::vector<int>>& edges) {
    int ov = -1, cp = -1, np = -1;
    std::vector<int> parents(edges.size() + 1, -1);

    for (auto& edge: edges) {
      int u = edge[0], v = edge[1];
      if (parents[v] == -1) {
        parents[v] = u;
      } else { // found the repetition
        ov = v;
        cp = parents[v];
        np = u;
        break;
      }
    }

    DisjointSet ds(edges.size() + 1);

    for (auto& edge : edges) {
      int u = edge[0], v = edge[1];

      if (ov == v && u == np) continue;

      if (!ds.join(u, v)) {
        return ov == -1 ? edge : std::vector<int>{ cp, ov };
      }
    }

    return { np, ov };
  }
};
