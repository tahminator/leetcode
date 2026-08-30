// leetcodemobile

class Solution {
public:
    int minSubArrayLen(int target, vector<int>& nums) {
        int n = nums.size();
        int l = 0, r = 0;
        
        int res = INT_MAX;
        int curr = 0;
        while (r < n) {
            curr += nums.at(r);
            
            while (curr >= target) {
                res = min(res, r - l + 1);
                
                curr -= nums.at(l);
                l++;
            }
            
            r++;
        }
        
        return res == INT_MAX ? 0 : res;
    }
};
