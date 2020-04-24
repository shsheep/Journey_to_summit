class Solution {
public:
    int rangeBitwiseAnd(int m, int n) {
        if (m == n)
            return m;
        unsigned int power = 2, iter = 0;
        unsigned int ret = 0;
        if (m >= 2) {
            while (power <= m) {
                ++iter;
                power *= 2;
                if (power > INT_MAX)
                    break;
            }
        }
        else {
            power = 1;
            iter = 0;
        }
        
        if (n < power) {
            ret = m;
            for (unsigned int i=m+1; i<=n; i++)
                ret &= i;
        }
            
        else
            ret = 0;
        
        return ret;
    }
};

/**
 * Runtime: 12 ms, faster than 63.14% of C++ online submissions for Bitwise AND of Numbers Range.
 * Memory Usage: 5.9 MB, less than 100.00% of C++ online submissions for Bitwise AND of Numbers Range.
 **/

/**
 * Correct solution
 * class Solution {
 * public:
 * 		int rangeBitwiseAnd(int m, int n) {
 * 		int c = 0;
 * 		while (m!=n){
 * 			m >>= 1;
 * 			n >>= 1;
 * 			++c;
 * 		}
 * 		return n << c;
 * 		}
 * 	};
 **/
