#include<bits/stdc++.h>

using namespace std;

class Solution {
public:
    void setZeroes(vector<vector<int>>& matrix) {
        const int 
            m = matrix.size(),
            n = matrix[0].size();
        
        vector<int> 
            rows(m, -1), 
            cols(n, -1);

        for (int i=0; i < m; i++) {
            for (int j=0; j < n; j++) {
                if (matrix[i][j] == 0) {
                    rows[i] = i;
                    cols[j] = j;
                }
            }
        }

        for (const int i: rows) {
            if (i != -1) {
                for (int j=0; j < n; j++) {
                    matrix[i][j] = 0;
                }
            }
        }

        for (const int j: cols) {
            if (j != -1) {
                for (int i=0; i < m; i++) {
                    matrix[i][j] = 0;
                }
            }
        }
    }
};

void vtos(vector<int>& v) {
    for (const int n: v) {
        cout << n << " ";
    }
    cout << endl;
}

int main(int argc, char const *argv[])
{
    vector<vector<int>> matrix{{0,1,2,0},{3,4,5,2},{1,3,1,5}};
    Solution s;
    s.setZeroes(matrix);

    for (auto row: matrix) {
        vtos(row);
    }
    
    return 0;
}
