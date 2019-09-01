class Solution:
    def longestPalindrome(self, s: str) -> str:
        if len(s) <= 1 or len(set(s)) == 1:
            return s
        ret_list = []
        for idx, ch in enumerate(s):
            if idx == len(s) - 1:
                continue
            k = 1
            left_idx = right_idx = idx
            candidate = []
            if idx == 0:
                while right_idx + k <= len(s) - 1:
                    if s[left_idx] == s[right_idx+k]:
                        right_idx += 1
                        candidate = s[left_idx:right_idx+1]
                        length = right_idx + 1 - left_idx
                        if length == len(s):
                            return candidate
                    else:
                        break
            else:
                several_standard = True
                while left_idx - k >= 0 and right_idx + k <= len(s) - 1:
                    if s[left_idx] == s[right_idx+k] and several_standard:
                        right_idx += 1
                        candidate = s[left_idx:right_idx+1]
                        length = right_idx + 1 - left_idx
                        if length == len(s):
                            return candidate
                        #ret_list.append((candidate, length))
                    elif s[left_idx-k] == s[right_idx+k]:
                        candidate = s[left_idx-k:right_idx+k+1]
                        k += 1
                        several_standard = False
                    else:
                        break
            if len(candidate) != 0:
                ret_list.append((candidate, len(candidate)))
        if len(ret_list) == 0:
            return s[0]
        ret_list.sort(key = lambda tup: tup[1])
        print(ret_list)
        return ret_list[-1][0]

'''
Runtime: 596 ms, faster than 90.99% of Python3 online submissions for Longest Palindromic Substring.
Memory Usage: 15.8 MB, less than 14.29% of Python3 online submissions for Longest Palindromic Substring.
'''
