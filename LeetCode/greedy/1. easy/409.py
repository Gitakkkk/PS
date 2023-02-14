# 409. Longest Palindrome

# 파이썬의 dict == hash table
class Solution:
    def longestPalindrome(self, s: str) -> int:
        a = set()
        for x in s:
            if x not in a:
                a.add(x)
            else:
                a.remove(x)
        if len(a) != 0:
            return len(s) - len(a) + 1
        else:
            return len(s)
                
