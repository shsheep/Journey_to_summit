/**
 * // This is the BinaryMatrix's API interface.
 * // You should not implement it, or speculate about its implementation
 * class BinaryMatrix {
 *   public:
 *     int get(int x, int y);
 *     vector<int> dimensions();
 * };
 */

/**
 * Solution 1 : Using binary search
 **/
class Solution {
public:
    int binarySearch(BinaryMatrix bM, int row, int default_right) {
        int left = 0, right = default_right, mid;
        if (bM.get(row, right) != 1)
            return 101;
        while (left <= right) {
            mid = (left+right)/2;
            if (bM.get(row, mid) == 1)
                right = mid-1;
            else
                left = mid+1;
        }
        return left;
    }
    
    int leftMostColumnWithOne(BinaryMatrix &binaryMatrix) {
        vector<int> dim = binaryMatrix.dimensions();
        int N = dim[0], M = dim[1];
        int left, right;
        int ret = M;
        for (int i=0; i<N; ++i)
            ret = min(ret, binarySearch(binaryMatrix, i, M-1));
        ret = ret == M ? -1 : ret;
        return ret;
    }
};

/**
 * 37 / 37 test cases passed.
 * Status: Accepted
 * Runtime: 32 ms
 * Memory Usage: 46 MB
 **/

/**
 * Solution 2
 **/
class Solution {
public:
    int leftMostColumnWithOne(BinaryMatrix &binaryMatrix) {
        vector<int> dim = binaryMatrix.dimensions();
        int N = dim[0], M = dim[1];
        int x = 0, y = M-1;
        int ret;
        while (x < N && y > -1) {
            if (binaryMatrix.get(x, y) == 1)
                --y;
            else
                ++x;
        }
        ret = y == M-1 ? -1 : y+1;
        return ret;
    }
};

/**
 * 37 / 37 test cases passed.
 * Status: Accepted
 * Runtime: 4 ms
 * Memory Usage: 8.3 MB
 **/
