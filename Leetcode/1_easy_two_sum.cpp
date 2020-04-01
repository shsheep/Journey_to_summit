class Solution {
	public:
		vector<int> twoSum(vector<int>& nums, int target) {
			vector<int> ret;
			vector<pair<int, int>> sorted_vector;
			int left = 0, right = nums.size()-1;
			int calc;
			
			for (int i=0; i<nums.size(); ++i)
				sorted_vector.push_back(make_pair(nums[i], i));
			
			sort(sorted_vector.begin(), sorted_vector.end());
			
			while (1) {
				calc = sorted_vector[left].first + sorted_vector[right].first;
				if (calc == target) {
					ret.push_back(sorted_vector[left].second);
					ret.push_back(sorted_vector[right].second);
					break;
				}
				else if (calc < target)
					++left;
				else
					--right;
			}
			
			sort(ret.begin(), ret.end());
			return ret;
		}
};

/*
 * Runtime: 12 ms, faster than 64.24% of C++ online submissions for Two Sum.
 * Memory Usage: 7.7 MB, less than 100.00% of C++ online submissions for Two Sum.
 */
