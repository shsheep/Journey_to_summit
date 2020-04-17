class Solution:
    def stringShift(self, s: str, shift: List[List[int]]) -> str:
        total_move = 0
        for direction, move in shift:
            if direction == 1:
                total_move += move
            else:
                total_move -= move
        total_move = total_move % len(s)
        
        if total_move == 0:
            return s
        
        ret = list(s)
        for i in range(len(s)):
            ret[i] = s[i-total_move]
        return ''.join(ret)

# Runtime: 32 ms
# Memory Usage: 13.9 MB
