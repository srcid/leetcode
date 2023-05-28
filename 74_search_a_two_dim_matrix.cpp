#include<iostream>
#include<vector>

using namespace std;

struct idx {
    const int r, c;

    idx(const int r, const int c) : r(r), c(c) {}
};

class Solution {
public:
    // i,j == i*(n-1) + j
    // dado n (pos) retorna i,j na matrix  
    idx at_pos(const int pos, const int m) {
        return idx(pos / m, pos % m) ;
    }
     
    bool searchMatrix(vector<vector<int>>& matrix, int target) {
        const int 
            n = matrix.size(),
            m = matrix[0].size(),
            size = n*m;
        
        int 
            i=0, 
            j = size-1,
            mid,
            d;

        while (i <= j) {
            mid = i + (j-i)/2;
            auto mid_idx = at_pos(mid, m);
            d = matrix[mid_idx.r][mid_idx.c] - target;

            if (d > 0) j = mid-1;
            else if (d < 0) i = mid+1;
            else return true; 
        }

        return false;
    }
};

int main(int argc, char const *argv[])
{
    vector<vector<int>> matrix = {
        {1,3,5,7}, 
        {10,11,16,20},
        {23,30,34,60}
    };

    Solution s;

    cout << s.searchMatrix(matrix, 3) << endl;

    return 0;
}
