#include <bits/stdc++.h>

using namespace std;

class Solution {
public:
    bool isOpening(char c) {return c == '(' || c == '[' || c == '{';}
    char openingChar(char c) {
      static const unordered_map<char,char> eq{
        {')','('}, {']','['}, {'}','{'}
      };

      return eq.at(c);
    }
    bool isValid(string s) {
        stack<char> stk;

        for (char c : s) {
          if (isOpening(c)) {
            stk.push(c);
          } else {
            if (stk.empty() || (c) != stk.top()) {
              return 0;
            }
            stk.pop();
          }
        }
        return stk.empty();
    }
};

int main(int argc, char const *argv[])
{
  Solution s;
  cout << s.isValid("()") << endl;
  cout << s.isValid("([)]") << endl;

  return 0;
}
