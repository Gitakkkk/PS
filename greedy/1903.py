# 1903. Largest Odd Number in String

# 내가 제출한 답
class Solution:
    def largestOddNumber(self, num: str) -> str:
        if int(num) % 2 == 1: return num
        arr = ["9", "7", "5", "3", "1"]
        for x in num[::-1]:
            if x in arr:
                idx = num.rindex(x)
                return num[0:idx+1]
        return ""

# 다른 사람이 제출한 답
# 나는 num[::-1]을 통해 뒤에서부터 확인했지만 range(len(num) - 1, -1, -1)도 가능
# 요소로 돌지 않고 인덱스로 돌아 따로 인덱스를 구하는 과정 없이 처리
class Solution:
    def largestOddNumber(self, num: str) -> str:
        for i in range(len(num) - 1, -1, -1) :
            if num[i] in {'1','3','5','7','9'} :
                return num[:i+1]
        return ''