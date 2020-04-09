class Solution {
	public:
		int singleNumber(vector<int>& nums) {
			// XOR result of same digits(of binary) will be 0.
			int ret = 0;
			for (int i=0; i<nums.size(); ++i)
				ret ^= nums[i];
			return ret;
		}
};

/*
 * Runtime: 12 ms, faster than 93.84% of C++ online submissions for Single Number.
 * Memory Usage: 7.5 MB, less than 100.00% of C++ online submissions for Single Number.
 */
