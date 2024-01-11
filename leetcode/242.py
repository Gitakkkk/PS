# 242. Valid Anagram

# 내가 작성한 답
class Solution:
    def isAnagram(self, s: str, t: str) -> bool:
        s = sorted(s)
        t = sorted(t)
        if s == t: return True
        return False

# 다른 사람이 작성한 답
# set 자료구조를 사용
class Solution:
    def isAnagram(self, s: str, t: str) -> bool:
        if len(s) != len(t): return False
        if len(set(s)) != len(set(t)): return False
        return True