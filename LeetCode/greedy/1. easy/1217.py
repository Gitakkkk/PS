class Solution:
    def minCostToMoveChips(self, position: List[int]) -> int:
        # Counter: 각 원소가 몇 번씩 나오는지 객체로 반환
        # position list의 index는 홀수냐 짝수냐의 의미만 가짐
        # 짝수 인덱스나 홀수 인덱스 모두 비용 없이 한 곳으로 모을 수 있음
        # 다시 말해 짝수 인덱스와 홀수 인덱스의 칩 개수를 확인하여 적은 쪽을 옮기는 게 이득
        dic = Counter([n%2 for n in position])
        return min(dic[0],dic[1])

# 라이브러리 사용하지 않고 푼 답안 ( 위 코드와 시간복잡도 동일 O(n) )
class Solution:
    def minCostToMoveChips(self, position: List[int]) -> int:
        a = b = 0
        for x in position:
            if x % 2 == 0:
                a += 1
            else:
                b += 1
        return min(a, b)