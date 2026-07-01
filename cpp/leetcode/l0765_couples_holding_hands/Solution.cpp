class Solution {
public:
  int minSwapsCouples(std::vector<int>& row) {
    // special adj, only 1:1 mappings
    std::unordered_map<int, int> adj;

    for (size_t i = 0; i < row.size(); i += 2) {
      int l = i, r = i + 1;

      adj[l] = r;
      adj[r] = l;
    }

    int swap = 0;
    for (size_t i = 0; i < row.size(); i += 2) {
      int l = row[i], r = row[i + 1];

      if (adj[l] != r) {
        auto curr_r_it = std::find(row.begin(), row.end(), adj[l]);
        auto curr_r_i = curr_r_it - row.begin();
        row[curr_r_i] = r;
        row[i + 1] = adj[l];
        swap++;
      }
    }

    return swap;
  }
};
