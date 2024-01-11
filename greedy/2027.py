# 2027. Minimum Moves to Convert String

# 내가 작성한 코드 ( 틀림 )
class Solution:
    def minimumMoves(self, s: str) -> int:
        ans = 0
        for i in range(3, len(s)+1):
            if s[i-3] == 'X' or s[i-2] == 'X' or s[i-1] == 'X':
                ans+=1
        return ans

# 다른 사람이 작성한 코드
# 접근 방법은 비슷했지만 while문 내에서 idx를 직접 3씩 올린다는 차이가 있음
class Solution:
    def minimumMoves(self, s: str) -> int:
        ans = i = 0
        while i < len(s): 
            if s[i] == "X": 
                ans += 1
                i += 3
            else: i += 1
        return ans