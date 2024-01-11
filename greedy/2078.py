# 2078. Two Furthest Houses With Different Colors

# 내가 작성한 코드
# 100 >= len(colors)이라는 조건이 붙어 있었다.
# 그래서 이중 for문으로 풀었지만 더 나은 코드가 있을 거라고 생각한다.
class Solution:
    def maxDistance(self, colors: List[int]) -> int:
        result = 0
        for i in range(len(colors)):
            for j in range(1, len(colors)):
                if colors[i] != colors[j]:
                    length = abs(i - j)
                    if length > result:
                        result = length
        return result

# 다른 사람이 작성한 코드
# colors[0]과 colors[-1]만 비교하여 정답 추출
class Solution:
    def maxDistance(self, colors: List[int]) -> int:
        ans = 0 
        for i, x in enumerate(colors): 
            if x != colors[0]: ans = max(ans, i)
            if x != colors[-1]: ans = max(ans, len(colors)-1-i)
        return ans