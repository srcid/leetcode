#include <bits/stdc++.h>

using namespace std;

class Solution {
public:
  string longestCommonPrefix(vector<string>& strs) {
    const int n = strs.size();
    int i, j;
    string common = "";

    if (n == 1) return strs[0];

    for (i=0; ; i++) {
      for (j=0; j<n-1; j++) {
        if (strs[j].size() == i || strs[j+1].size() == i || strs[j][i] != strs[j+1][i]) goto end;
      }
      if (j) {
        common.push_back(strs[j][i]);
      }
    }

    end:
    return common;
  }

  string longestCommonPrefix2(vector<string>& strs) {
    string common = strs[0];
    int b = common.size();

    for (int i=1; i < strs.size(); i++) {
      if (strs[i].size() < b) b = strs[i].size();
      
      int j;
      for (j=0; j <= b; j++) {
        if (common[j] != strs[i][j]) break;
      }

      b = j;
    }

    return common.substr(b);
  }
};

int main(int argc, char const *argv[])
{
  vector<vector<string>> arr{
    {"flower","flow","flight"},
    {"flower","flower","flower","flower"},
    {""},
  };

  Solution s;

  for (auto strs : arr) {
    for (auto s : strs) {
      cout << s << " ";
    }
    cout << endl << s.longestCommonPrefix(strs) << endl;
    cout << endl << s.longestCommonPrefix2(strs) << endl;
  }

  return 0;
}
