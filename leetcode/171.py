# 171. Excel Sheet Column Number

class Solution:
    def titleToNumber(self, columnTitle: str) -> int:
        ans, pos = 0, 0
        for x in reversed(columnTitle):
            digit = ord(x)-64
            ans += digit * 26**pos
            pos += 1
            
        return ans