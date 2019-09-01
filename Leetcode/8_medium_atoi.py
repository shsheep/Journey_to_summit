class Solution:
    def myAtoi(self, str: str) -> int:
        if len(str) == 0:
            return 0
        already_number = negative = waiting = False
        ret = ''
        numbers = "0123456789"
        for ch in str:
            if already_number:
                if ch not in numbers:
                    if len(ret) > 0:
                        break
                    else:
                        return 0
                else:
                    ret += ch
            else:
                if ch == ' ' and not waiting and not negative:
                    continue
                elif ch == '+' and not negative and not waiting:
                    waiting = True
                elif ch == '-' and not waiting and not negative:
                    negative = True
                elif ch in numbers:
                    already_number = True
                    ret += ch
                else:
                    return 0
        if not already_number:
            return 0
        if negative:
            ret = int(ret) * (-1)
        else:
            ret = int(ret)
        if -1 * 2 ** 31 > ret:
            return -1 * 2 ** 31
        elif ret >= 2 ** 31:
            return 2 ** 31 - 1
        return ret

'''
Runtime: 40 ms, faster than 75.20% of Python3 online submissions for String to Integer (atoi).
Memory Usage: 14 MB, less than 5.95% of Python3 online submissions for String to Integer (atoi).
'''
