#include <vector>

using namespace std;

class Solution {
public:
    vector<vector<int>> subsets(vector<int>& nums) {
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
};