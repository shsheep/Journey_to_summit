class Solution {
public:
    int lastStoneWeight(vector<int>& stones) {
        priority_queue<int, vector<int>, less<int>> heap;
        int stone_1, stone_2;
        
        for (int i=0; i<stones.size(); ++i)
            heap.push(stones[i]);
        while (heap.size() != 0 && heap.size() != 1) {
            stone_1 = heap.top();       heap.pop();
            stone_2 = heap.top();       heap.pop();
            if (stone_1 - stone_2)
                heap.push(stone_1-stone_2);
        }
        if (heap.size() == 0)
            return 0;
        else
            return heap.top();
    }
};

/*
 * Runtime: 4 ms, faster than 30.09% of C++ online submissions for Last Stone Weight.
 * Memory Usage: 6.3 MB, less than 100.00% of C++ online submissions for Last Stone Weight.
 */
