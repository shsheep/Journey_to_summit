class Solution {
	public:
		int maxProfit(vector<int>& prices) {
			if (prices.empty())
				return 0;
			int ret = 0;
			for (int i = 0; i < prices.size() - 1; ++i) {
				if (prices[i+1] > prices[i]) {
					ret += prices[i+1] - prices[i];
				}
			}
			return ret;
		}
};

/*
 * Runtime: 8 ms, faster than 49.26% of C++ online submissions for Best Time to Buy and Sell Stock II.
 * Memory Usage: 7.2 MB, less than 100.00% of C++ online submissions for Best Time to Buy and Sell Stock II.
