#include <bits/stdc++.h>

using namespace std;

class Solution {
public:
  int lengthOfLongestSubstring(string s) {
    string sub("");
    int max = 0;
    int charPos;

    for (char c : s) {
      charPos = sub.find(c);

      if (charPos != string::npos) {
        sub.erase(0,charPos + 1);
      }      
      
      sub.push_back(c);
      
      if (max < sub.size()) {
        max = sub.size();
      }
    }

    return max;
  }
};

int main(int argc, char const *argv[])
{
  Solution s;
  map<string,int> cases{
    {"pwwkew",3},{"dvdf", 3},{"abcabcbb",3},{" ",1}
  };
  
  for (auto [str, answer] : cases) {
    cout << s.lengthOfLongestSubstring(str) << " : " << answer << endl;
  }

  return 0;
}
