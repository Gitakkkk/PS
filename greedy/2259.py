# 2259. Remove Digit From Number to Maximize Result

# 내가 작성한 코드
class Solution:
    def removeDigit(self, number: str, digit: str) -> str:
        res = '0'
        for i, x in enumerate(number):
            if x == digit:
                temp = number[:i] + number[i+1:]
                if int(temp) > int(res): res = temp
        return res

# 다른 사람이 작성한 코드
# 같은 로직을 생각한 거 같지만 max 함수로 한번에 처리했다는 차이가 있음
class Solution:
    def removeDigit(self, number: str, digit: str) -> str:
        return max(
            number[:i] + number[i+1:]
            for i, d in enumerate(number)
            if d == digit
        )