class Solution {
public:
    int countElements(vector<int>& arr) {
        int ret = 0;
        int max = *max_element(arr.begin(), arr.end());
        map<int, int> visited;
        map<int, int>::iterator it;
        vector<int> vec_visited;
        for (int i=0; i<max+1; ++i)
            vec_visited.push_back(-1);
        for (int i=0; i<arr.size(); ++i)
            ++visited[arr[i]];
        for (it=visited.begin(); it != visited.end(); ++it)
            vec_visited[it->first] = it->second;
        for (int i=0; i<vec_visited.size()-1; ++i) {
            if (vec_visited[i+1] != -1 && vec_visited[i] != -1)
                ret += vec_visited[i];
        }
        return ret;
    }
};

/*
class Solution {
public:
    int countElements(vector<int>& arr) {
        map<int, int> maps;
        int ans = 0;
        for (auto t : arr)
            maps[t]++;
        for (auto t : maps) {
            if (maps.find(t.first + 1) != maps.end()) {
                ans += t.second;
            }
        }
        return ans;
    }
};
*/
