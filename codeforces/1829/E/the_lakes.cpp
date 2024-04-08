#include<bits/stdc++.h>

using namespace std;

class Solution {
public:
    vector<vector<int>> matrix;
    int m;
    int n;

    int dfs(const int i, const int j) {
        if (!(0 <= i && i < m) || !(0 <= j && j < n) || matrix[i][j] == 0) {
            return 0;
        }

        auto cur = matrix[i][j];
        matrix[i][j] = 0;
        
        int up = dfs(i+1, j); 
        int down = dfs(i-1, j);
        int left = dfs(i, j+1);
        int right = dfs(i, j-1);

        return cur + up + down + left + right;
    }

    int volOfBigestLake(vector<vector<int>> _matrix) {
        matrix = _matrix;
        m = matrix.size(),
        n = matrix[0].size();

        vector<int> ans = {0};

        for (int i = 0; i < m; i++) {
            for (int j = 0; j < n; j++) {
                if (matrix[i][j] != 0) {
                    int lake_vol = dfs(i, j);
                    ans.push_back(lake_vol);
                }
            }
        }

        auto maxVol = *max_element(ans.begin(), ans.end());

        return maxVol;
    }
};

int main(int argc, char const *argv[])
{
    int ncases;
    cin >> ncases;
    
    vector<int> ans;

    while (ncases--) {
        Solution s;
        int m, n;
        cin >> m;
        cin >> n;

        vector<vector<int>> matrix(m, vector<int>(n, 0));

        for (int i = 0; i < m; i++) {
            for (int j = 0; j < n; j++) {
                cin >> matrix[i][j];
            }
        }

        int volOfBigestLake = s.volOfBigestLake(matrix);
        ans.push_back(volOfBigestLake);
    }

    for (const int vol: ans) {
        cout << vol << endl;
    }
    
    return 0;
}
