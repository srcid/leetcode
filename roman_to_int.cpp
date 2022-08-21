#include <iostream>
#include <string>
#include <unordered_map>

using namespace std;

class Solution {
private:
  static const unordered_map<char, int> romans = {
    {'I', 1}, {'V', 5}, {'X', 10}, {'L', 50}, {'C', 100}, {'D', 500}, {'M', 1000}
  };

  enum {
    I = 1,
    V = 5,
    X = 10,
    L = 50,
    C = 100,
    D = 500,
    M = 1000
  };

public:
    int romanToInt(string s) {
        int cnt = 0;
        int prev = 0;
        int val;

        for (char c : s) {
          val = romans.at(c);

          if ((prev == I || prev == X || prev == C) && val > prev) {
            cnt -= 2 * prev;
          }

          cnt += val;
          prev = val;
        }

      return cnt;
    }
};

int main(int argc, char const *argv[])
{
  Solution s;
  cout << s.romanToInt("LVIII") << endl;
  cout << s.romanToInt("XCIX") << endl;
  cout << s.romanToInt("MCMXCIV") << endl;

  return 0;
}