#include <vector>

using namespace std;

class Solution {
public:
    int XORSum(vector<int>::iterator p, vector<int>::iterator q) {
        if (p != q) {
            return ((*p)^XORSum(p+1, q));
        }
        
        return 0;
    }
    
    vector<vector<int>> subSets(vector<int>& nums) {
        vector<vector<int>> res;
        
        for (int mask = 0; mask < (1<<nums.size()); mask++) {
            vector<int> sub;
            
            for (int j = 0; j < nums.size(); j++) {
                if (mask & (1<<j)) {
                    sub.push_back(nums[j]);
                }
            }
            
            res.push_back(sub);
        }
        
        return res;
    }
    
    int subsetXORSum(vector<int>& nums) {
        int sum = 0;
        
        for (auto arr : subSets(nums)) {
            sum += XORSum(arr.begin(), arr.end());
        }
        
        return sum;
    }
};
