#include <vector>
#include <iostream>

class Solution {
public:
  /**
  * [
  *   [4, 3, 2, -1],
  *   [3, 2, 1, -1],
  *   [1, 1, -1, -2],
  *   [-1, -1, -2, -3]
  * ]
  *
  * each given row and given column is sorted
  * row l->r: desc
  * col u->d: desc
  *
  * the pattern is interesting u can see that it almost splits into a triangle of sorts where all the negatives end up closer to the bottom right 
  * while positives end up closer to the top left.
  *
  * [            *
  *   [4, 3, 2, -1],
  *   [3, 2, 1, -1],
  *   [1, 1, -1, -2],
  *   [-1, -1, -2, -3]
  * ]
  *
  * -1 is negative, which means it and all below it are negative. 
  * the coord for -1 is [0, 3]. if we want to include everything below it,
  * [1, 3], [2, 3], [3, 3].
  *
  * [      *
  *   [1, -1]
  *   [-1, -1]
  * ]
  *
  * top right is [0, 1]. All below is negative including it so that means [1, 1] is negative too.
  * next iter starts at [0, 0] which is 1. 
  */
  int countNegatives(std::vector<std::vector<int>>& grid) {
    const int n = grid.size(), m = grid[0].size();

    int count = 0;

    int r = 0, c = m - 1;
    while (r < n && c >= 0) {
      // everything below it is negative, including it is negative.
      if (grid[r][c] < 0) {
        count += n - r;
        c--; // move over
      } else { // keep looking for negative in the given col.
        r++;
      }
    }

    return count;
  }
};

int main() {
  Solution s;
  std::vector<std::vector<int>> g = { {3, 2}, {1, 0} };
  std::cout << s.countNegatives(g);
}
