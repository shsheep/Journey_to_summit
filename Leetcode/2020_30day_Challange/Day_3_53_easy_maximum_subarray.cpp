class Solution {
public:
    int maxSubArray(vector<int>& nums) {
        int ret, size = nums.size();
        vector<int> end_sum;
        end_sum.push_back(nums[0]);
        ret = nums[0];
        for(int i=1; i<size; ++i) {
            end_sum.push_back(max(end_sum[i-1] + nums[i], nums[i]));
            ret = max(ret, end_sum[i]);
        }
        return ret;
    }
};

/*
 * Kadane's algorithm
 * Runtime: 4 ms, faster than 98.08% of C++ online submissions for Maximum Subarray.
 * Memory Usage: 7.3 MB, less than 100.00% of C++ online submissions for Maximum Subarray.
 */
