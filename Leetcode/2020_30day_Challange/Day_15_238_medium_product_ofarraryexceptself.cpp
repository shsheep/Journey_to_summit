class Solution {
public:
    vector<int> productExceptSelf(vector<int>& nums) {
        vector<int> ret;
        int track = 1;
        for (int i=0; i<nums.size(); ++i) {
            if (i==0) {
                ret.push_back(1);
                continue;
            }
            ret.push_back(ret[i-1] * nums[i-1]);
        }
        for (int i=nums.size()-1; i>-1; --i) {
            ret[i] *= track;
            track *= nums[i];
        }
        return ret;
    }
};

/*
 * Runtime: 40 ms, faster than 75.23% of C++ online submissions for Product of Array Except Self.
 * Memory Usage: 10.7 MB, less than 100.00% of C++ online submissions for Product of Array Except Self.
 */
