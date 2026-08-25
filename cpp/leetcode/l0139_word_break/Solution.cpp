class TrieNode {
public:
  bool end;
  TrieNode* children[26];

  TrieNode() {
      end = false;
      for (int i = 0; i < 26; i++) {
          children[i] = nullptr;
      }
  }
};

class Solution {
private:
  int memo[301];

  bool dfs(string& s, int start, TrieNode* root) {
    if (start == s.length()) return true;
    if (memo[start] != -1) return memo[start];


    auto node = root;
    for (int i = start; i < s.length(); i++) {
      char c = s[i] - 'a';

      if (node == nullptr || node->children[c] == nullptr) {
        break;
      }

      node = node->children[c];

      if (node->end && dfs(s, i + 1, root)) {
        memo[start] = true;
        return true;
      }
    }

    memo[start] = false;
    return false;
  }

public:
  // can put wordDict in trie for efficient prefixing
  //
  // for s, there r a couple scenarios we need to be able to handle
  //
  // we either cant make a word on the given prefix (clear prefix, move on the next char)
  // or we found a valid trie prefix for the current s prefix and we should keep going until we hit a valid word.
  //
  // the hard part is that we might have multiple valid answers in a given string, which im not sure how we account for.
  // its kinda like backtracking where if we find a valid word in trie, we can either keep it or keep looking for a longer word to match on.
  bool wordBreak(string s, vector<string>& wordDict) {
    std::fill(std::begin(memo), std::end(memo), -1);
    TrieNode* root = new TrieNode();

    for (auto& word : wordDict) {
      auto cur = root;
      for (auto c : word) {
        int i = c - 'a';
        if (cur->children[i] == nullptr) {
          cur->children[i] = new TrieNode();
        }
        cur = cur->children[i];
      }
      cur->end = true;
    }

    return dfs(s, 0, root);
  }
};
