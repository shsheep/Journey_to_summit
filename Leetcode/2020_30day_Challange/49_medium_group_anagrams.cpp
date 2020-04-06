class Solution {
	public:    
		vector<vector<string>> groupAnagrams(vector<string>& strs) {
			vector<vector<string>> ret;
			map<string, vector<string>> hash;
			string tmp;
			for (int i=0; i<strs.size(); ++i) {
				tmp = strs[i];
				sort(tmp.begin(), tmp.end());
				hash[tmp].push_back(strs[i]);
			}
			for (map<string, vector<string>>::iterator it = hash.begin(); it != hash.end(); ++it) 
					ret.push_back(it->second);
			
			return ret;
		}
};

/*
 * Runtime: 68 ms, faster than 34.11% of C++ online submissions for Group Anagrams.
 * Memory Usage: 16.8 MB, less than 100.00% of C++ online submissions for Group Anagrams.
 */

