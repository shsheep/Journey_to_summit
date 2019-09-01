class Solution:
    def convert(self, s: str, numRows: int) -> str:
        if numRows <= 1 or len(s) <= numRows:
            return s
        ret = [''] * numRows
        index, step = 0, 1
        for ch in s:
            ret[index] += ch
            if index == 0:
                step = 1
            elif index == numRows - 1:
                step = -1
            index += step
        return ''.join(ret)
                
'''
Runtime: 56 ms, faster than 93.72% of Python3 online submissions for ZigZag Conversion.
Memory Usage: 14.1 MB, less than 10.00% of Python3 online submissions for ZigZag Conversion.
'''
