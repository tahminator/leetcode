#define K 10

class Solution {
public:
  /**
   * s length of 11 means we should only run 0 and 1.
   * 
   */
  std::vector<std::string> findRepeatedDnaSequences(std::string s) {
    std::vector<std::string> res;

    if (s.length() <= K) return res;

    std::unordered_map<std::string, int> seen;

    for (int l = 0; l <= s.length() - K; l++) {
      std::string key = s.substr(l, K);

      if (auto found = seen.find(key); found != seen.end()) {
        if (found->second == 1) {
          res.emplace_back(found->first);
        }
        ++found->second;
      } else {
        ++seen[key];
      }
    }

    return res;
  }
};
