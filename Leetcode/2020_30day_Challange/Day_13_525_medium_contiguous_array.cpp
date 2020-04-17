class Solution {
public:
    int findMaxLength(vector<int>& nums) {
        map<int, int> sections;
        int cnt = 0, max_length = 0;
        sections[0] = -1;
        
        for (int i=0; i<nums.size(); ++i) {
            if (nums[i] == 1)
                cnt += 1;
            else
                cnt += -1;
            
            if (sections.find(cnt) != sections.end())
                max_length = max(max_length, i-sections[cnt]);
            else
                sections[cnt] = i;
        }
        
        return max_length;
    }
};

/*
 * Runtime: 356 ms, faster than 8.04% of C++ online submissions for Contiguous Array.
 * Memory Usage: 18.2 MB, less than 100.00% of C++ online submissions for Contiguous Array.
 */
