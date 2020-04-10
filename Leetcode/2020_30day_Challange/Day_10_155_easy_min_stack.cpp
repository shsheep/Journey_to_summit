class MinStack {
public:
    vector<int> stack;
    priority_queue<int, vector<int>, greater<int>> heap;
    map<int, int> popped;
    int sp;
    
    /** initialize your data structure here. */
    MinStack() {
        while (!stack.empty())
            stack.pop_back();
        while (!heap.empty())
            heap.pop();
        sp = -1;
    }
    
    void push(int x) {
        stack.push_back(x);
        heap.push(x);
        ++sp;
    }
    
    void pop() {
        if (!stack.empty()) {
            int top = stack[sp--];
            stack.pop_back();
            popped[top] = 1;
        }
    }
    
    int top() {
        return stack[sp];
    }
    
    int getMin() {
        int ret;
        while (popped[heap.top()]) {
            popped[heap.top()] = 0;
            heap.pop();
        }
        ret = heap.top();
        return ret;
    }
};

/**
 * Your MinStack object will be instantiated and called as such:
 * MinStack* obj = new MinStack();
 * obj->push(x);
 * obj->pop();
 * int param_3 = obj->top();
 * int param_4 = obj->getMin();
 */

/**
 * Runtime: 44 ms, faster than 26.73% of C++ online submissions for Min Stack.
 * Memory Usage: 14.9 MB, less than 100.00% of C++ online submissions for Min Stack.
 **/
