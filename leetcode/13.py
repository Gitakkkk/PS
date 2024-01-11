# 13. Roman to Integer

class Solution:
    def romanToInt(self, s: str) -> int:
        _set = {
            'I': 1,
            'V': 5,
            'X': 10,
            'L': 50,
            'C': 100,
            'D': 500,
            'M': 1000
        }

        ans = 0
        for x, y in zip(s, s[1:]):
            if _set[x] < _set[y]:
                ans -= _set[x]
            else:
                ans += _set[x]

        return ans +  _set[s[-1]]