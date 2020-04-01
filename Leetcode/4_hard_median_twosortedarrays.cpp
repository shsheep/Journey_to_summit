class Solution {
    public:
        double findMedianSortedArrays(vector<int>& nums1, vector<int>& nums2) {
            if (nums1.empty()) {
                if (nums2.size() % 2 == 0) 
                    return 0.5 * (nums2[nums2.size()/2] + nums2[nums2.size()/2-1]);
                else
                    return nums2[nums2.size()/2];
            }
            else if (nums2.empty()) {
                if (nums1.size() % 2 == 0)
                    return 0.5 * (nums1[nums1.size()/2] + nums1[nums1.size()/2-1]);
                else
                    return nums1[nums1.size()/2];
            }
            
            double ret;
            int pop_val;
            int start_idx = 0;
            priority_queue<int, vector<int>, less<int>> max_heap;
            priority_queue<int, vector<int>, greater<int>> min_heap;
            
            if (nums1.size() != 0){
                max_heap.push(nums1[0]);
                for (int i = 1; i < nums1.size(); ++i) {
                    if (nums1[i] > max_heap.top()) {
                        min_heap.push(nums1[i]);
                        if (min_heap.size() - max_heap.size() > 0) {
                            pop_val = min_heap.top();   min_heap.pop();
                            max_heap.push(pop_val);
                        }
                    }
                    else {
                        max_heap.push(nums1[i]);
                        if (max_heap.size() - min_heap.size() > 1)
                            pop_val = max_heap.top();   max_heap.pop();
                            min_heap.push(pop_val);
                    }
                }
            }
            if (max_heap.size() == 0) {
                start_idx = 1;
                max_heap.push(nums2[0]);
            }
            for (int i = start_idx; i < nums2.size(); ++i) {
                if (nums2[i] > max_heap.top()) {
                    min_heap.push(nums2[i]);
                    if (min_heap.size() - max_heap.size() > 0) {
                        pop_val = min_heap.top();   min_heap.pop();
                        max_heap.push(pop_val);
                    }
                }
                else {
                    max_heap.push(nums2[i]);
                    if (max_heap.size() - min_heap.size() > 1) {
                        pop_val = max_heap.top();   max_heap.pop();
                        min_heap.push(pop_val);
                    }
                }
            }
            if ((nums1.size() + nums2.size()) % 2 == 0) {
                ret = max_heap.top();
                ret += min_heap.top();
                ret /= 2;
            }
            else
                ret = (double) max_heap.top();

            return ret;
         }
};

/*
 * Runtime: 44 ms, faster than 5.78% of C++ online submissions for Median of Two Sorted Arrays.
 * Memory Usage: 8.4 MB, less than 100.00% of C++ online submissions for Median of Two Sorted Arrays.
 */
