class Solution:
    def lengthOfLongestSubstring(self, s: str) -> int:
        if len(s) < 2:
            return len(s)
        tmp = ''
        substring_list = []
        for ch in s:
            if ch not in tmp:
                tmp += ch
            else:
                substring_list.append((tmp, len(tmp)))
                ch_idx = tmp.index(ch)
                tmp = tmp[ch_idx+1:] + ch
        substring_list.append((tmp, len(tmp)))
        substring_list.sort(key = lambda tup: tup[1])
        return substring_list[-1][1]

'''
Runtime: 64 ms, faster than 73.89% of Python3 online submissions for Longest Substring Without Repeating Characters.
Memory Usage: 20.8 MB, less than 5.10% of Python3 online submissions for Longest Substring Without Repeating Characters.
'''
