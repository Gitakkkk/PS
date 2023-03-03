# 455. Assign Cookies

# 쿠기 크기가 가장 작은 어린이에게 가능한 한 많은 쿠키 할당
# res == 쿠키를 받는 어린이 수, i == 현재 어린이 인덱스
class Solution:
    def findContentChildren(self, g: List[int], s: List[int]) -> int:
        if not g or not s: return 0
        g.sort()
        s.sort()
        res = i = 0
        for x in s:
            if i >= len(g): return res
            if x >= g[i]:
                res += 1
                i += 1
        return res