class Solution {
public:
    bool backspaceCompare(string S, string T) {
        vector<char> stack_S, stack_T;
        for(int i=0; i<S.length(); ++i) {
            if (stack_S.empty()) {
                if (S[i] == '#')
                    continue;
                else
                    stack_S.push_back(S[i]);
            }
            else {
                if(S[i] == '#')
                    stack_S.pop_back();
                else
                    stack_S.push_back(S[i]);
            }
        }
        for(int i=0; i<T.length(); ++i) {
            if (stack_T.empty()) {
                if (T[i] == '#')
                    continue;
                else
                    stack_T.push_back(T[i]);
            }
            else {
                if(T[i] == '#')
                    stack_T.pop_back();
                else
                    stack_T.push_back(T[i]);
            }
        }
        return stack_S == stack_T;
    }
};

/*
 * Runtime: 0 ms, faster than 100.00% of C++ online submissions for Backspace String Compare.
 * Memory Usage: 6.5 MB, less than 100.00% of C++ online submissions for Backspace String Compare
 */
