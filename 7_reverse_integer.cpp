#include <iostream>
#include <limits>
#include <cmath>

using namespace std;

const int MAX_INT = numeric_limits<int>::max();
const int MIN_INT = numeric_limits<int>::min();

class Solution {
public:
  int getLastDigit(int x) {
      return abs(x%10);
  }
  
  int reverse(int x) {
    int sign = x < 0 ? -1 : 1;
    unsigned int answer = 0;
    int r;

    while (x) {
      r = getLastDigit(x);
      if (answer > MAX_INT/10 || (answer == MAX_INT/10 && r > 7)) return 0;
      x /= 10;
      answer = 10 * answer + r; 
    }

    return sign * answer;
  }
};

int main(int argc, char const *argv[])
{
  // int n = 1534236469;
  int n = -2147483648;
  //int n = -2147483412;
  Solution s;
  cout << s.reverse(n) << endl;
  return 0;
}
