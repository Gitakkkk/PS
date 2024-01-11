# 202. Happy Number

class Solution:
    def isHappy(self, n: int) -> bool:
        hashMap = {}
        while True:
            if n == 1: return 1
            if n in hashMap: return 0

            hashMap[n] = 0
            _sum = 0
            for i in str(n):
                _sum += int(i) ** 2
            n = _sum