class Solution {
public:
    void moveZeroes(vector<int>& nums) {
        /* //not in-place method
        vector<int> modified;
        int num_zero = 0;
        for (int i=0; i<nums.size(); ++i) {
            if (nums[i] == 0)
                ++num_zero;
            else
                modified.push_back(nums[i]);
        }
        while (num_zero--)
            modified.push_back(0);
        nums = modified;
        */
        int idx = 0;
        for (int i=0; i<nums.size(); ++i)
            if (nums[i] != 0)
                nums[idx++] = nums[i];
        for (int i=idx; i<nums.size(); ++i)
            nums[i] = 0;
    }
};

/*
 * Runtime: 12 ms, faster than 91.48% of C++ online submissions for Move Zeroes.
 * Memory Usage: 7.2 MB, less than 100.00% of C++ online submissions for Move Zeroes.
 */
