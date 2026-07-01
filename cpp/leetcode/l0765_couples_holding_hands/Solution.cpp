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

    int curr_pos[row.size()];

    for (size_t i = 0; i < row.size(); i++) {
      curr_pos[row[i]] = i;
    }

    int swap = 0;
    for (size_t i = 0; i < row.size(); i += 2) {
      int l = row[i], r = row[i + 1];

      if (adj[l] != r) {
        auto curr_index_r = curr_pos[adj[l]];
        row[curr_index_r] = r;
        row[i + 1] = adj[l];

        curr_pos[r] = curr_index_r;
        curr_pos[adj[l]] = i + 1;
        swap++;
      }
    }

    return swap;
  }
};
