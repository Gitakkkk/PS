# 1013. Partition Array Into Three Parts With Equal Sum

# 내가 작성한 코드
# [0, 0, 0, 0]과 같이 모든 요소가 0인 배열에 대한 예외처리를 못해서 실패
class Solution:
    def canThreePartsEqualSum(self, arr: List[int]) -> bool:
        _sum = sum(arr) // 3
        acc = 0
        cnt = 0
        for x in arr:
            acc += x
            if acc == _sum:
                cnt += 1
                acc = 0
        return cnt == 3

# 다른 사람이 작성한 답
# count >= 3에서 [0, 0, 0, 0] 배열을 판별할 수 있음
# 위 배열은 count가 4가 나오므로 >= 연산자를 사용해주면 해결할 수 있음
class Solution:
    def canThreePartsEqualSum(self, arr: List[int]) -> bool:
        total = sum(arr)
        if total % 3 != 0: return False
        count, cumsum, target = 0, 0, total // 3
        for num in arr:
            cumsum += num
            if cumsum == target:
                cumsum = 0
                count += 1
        return count >= 3