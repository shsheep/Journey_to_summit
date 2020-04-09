class Solution {
public:
    bool isHappy(int n) {
        map<int, int> visited;
        int result, div, remains;
        
        while (visited.find(n) == visited.end()) {
            visited[n] = 1;
            result = 0;
            div = n;
            while (div != 0) {
                remains = div % 10;
                result += remains*remains;
                div = div / 10;
            }
            if (result == 1)
                return true;
            n = result;
        }
        return false;
    }
};

/*
 * Runtime: 4 ms, faster than 58.22% of C++ online submissions for Happy Number.
 * Memory Usage: 6.4 MB, less than 100.00% of C++ online submissions for Happy Number.
 */

