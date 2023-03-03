# 2224. Minimum Number of Operations to Convert Time

# 내가 작성한 코드
# 각 시간의 차이를 minute 단위로 환산하여 나누었음
class Solution:
    def convertTime(self, current: str, correct: str) -> int:
        result = 0
        cur = int(current[:2])*60 + int(current[3:])
        cor = int(correct[:2])*60 + int(correct[3:])
        temp = cor - cur
        if temp // 60 > 0:
            result += temp // 60
            temp = temp % 60
        if temp // 15 > 0:
            result += temp // 15
            temp = temp % 15
        if temp // 5 > 0:
            result += temp // 5
            temp = temp % 5
        if temp // 1 > 0:
            result += temp // 1
        return result

# 새로 작성한 코드
# 나눈 값으로 if문에 해당하는지 판별하지 않고, 값 자체를 >=에 대입하여 조건 해당 여부 판별
class Solution:
    def convertTime(self, current: str, correct: str) -> int:
        result = 0
        cur = int(current[:2])*60 + int(current[3:])
        cor = int(correct[:2])*60 + int(correct[3:])
        temp = cor - cur
        while temp > 0:
            if temp >= 60:
                result += temp // 60
                temp = temp % 60
            elif temp >= 15:
                result += temp // 15
                temp = temp % 15
            elif temp >= 5:
                result += temp // 5
                temp = temp % 5
            elif temp >= 1:
                result += temp // 1
                temp = temp % 1
        return result