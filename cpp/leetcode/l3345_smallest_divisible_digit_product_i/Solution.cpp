class Solution {
private:
  int calculateDigitProduct(int n) {
    int product = 1, curr = n;
    while (curr > 0) {
      int d = curr % 10;
      product *= d;
      curr /= 10;
    }

    return product;
  }

public:
  int smallestNumber(int n, int t) {
    int cur = n;
    while (true) {
      if (calculateDigitProduct(cur) % t == 0) {
        return cur;
      }
      cur++;
    }
  }
};
