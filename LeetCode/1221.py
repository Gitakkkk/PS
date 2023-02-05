# 1221. Split a String in Balanced Strings
class Solution:
    def balancedStringSplit(self, s: str) -> int:
        count = 0
        r = 0
        l = 0
        for x in s:
            if x == 'R':
                r+=1
            elif x == 'L':
                l+=1
            if r == l:
                count+=1
                r = 0
                l = 0
        return count