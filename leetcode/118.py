# 118. Pascal's Triangle

# 내가 작성한 코드
# list index out of range 에러 발생
class Solution:
    def generate(self, numRows: int) -> List[List[int]]:
        if numRows == 1: return [[1]]
        if numRows == 2: return [[1], [1,1]]
        ans = [[1], [1,1]]
        element = [1]
        for i in range(3, numRows+1):
            for j in range(len(ans[i-1])):
                value = ans[i-1][j] + ans[i-1][j+1]
                element.append(value)
            element.append(1)
            ans.append(element)
        return ans

# 다른 사람이 작성한 코드
class Solution:
    def generate(self, numRows: int) -> List[List[int]]:
        cnt = 0
        ans = []
        while cnt <= numRows:
            if cnt == 1:
                ans.append([1])
            if cnt == 2:
                ans.append([1,1])
            if cnt > 2:
                latest = ans[len(ans)-1]
                new = []
                new.append(1)
                for i in range(len(latest)-1):
                    new.append(latest[i] + latest[i+1])
                new.append(1)
                ans.append(new)
            cnt += 1
        return ans
        
