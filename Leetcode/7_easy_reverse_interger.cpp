#include <iostream>
#include <string>
#include <cstring>

using namespace std;

class Solution {
public:
    int reverse(int x) {
		/*
        string str_x = to_string(x);
        string converted;
        string limit = str_x[0] == '-' ? "2147483649" : "2147483648";
        int size = str_x.length();
        int edge_idx = str_x[0] == '-' ? 1 : 0;
        int ret;
        bool is_zero_end = false;
        
        if (edge_idx == 1)
            --size;
        if (size > 10)
            return 0;
        
        for (int i=str_x.length()-1; i>=edge_idx; --i) {
            if (is_zero_end)
                converted += str_x[i];
            else if (!is_zero_end && str_x[i] != '0') {
                is_zero_end = true;
                converted += str_x[i];
            }
        }
        
        if (converted.length() == 10) {
            for (int i=0; i<10; ++i) {
                if (converted[i] > limit[i])
                    return 0;
                else if (converted[i] == limit[i]) {
                    if (i == 9)
                        return 0;
                }
                else
                    break;
            }
        }
        
        ret = atoi(converted.c_str());
        if (str_x[0] == '-')
            ret *= -1;
        return ret;
		*/
		int ret=0;
        while (x) {
            if (INT_MAX/10 < ret || INT_MIN/10 > ret)
                return 0;
            ret = ret*10 + x%10;
            x = x/10;
        }
        return ret;
    }
};

/*
 * Runtime: 4 ms, faster than 58.37% of C++ online submissions for Reverse Integer.
 * Memory Usage: 6 MB, less than 100.00% of C++ online submissions for Reverse Integer.
 */
