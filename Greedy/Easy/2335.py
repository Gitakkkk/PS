# 2335. Minimum Amount of Time to Fill Cups

# heapq.heapify 함수를 통해 list를 힙 자료구조로 변경
# heappop 함수를 통해 힙 자료구조 중 가장 작은 값 제거 & 반환
# 반환한 값에 += 1 후 heappush (값이 0 이상인 경우 힙 자료구조에 push 되지 않음)
# 가장 큰 또는 가장 작은 값에 순차적으로 변경이 필요할 때 사용하기 좋은 자료구조
class Solution:
    def fillCups(self, amount: List[int]) -> int:
        pq = [-q for q in amount if q != 0]
        heapq.heapify(pq)
        ret = 0
        
        while len(pq) > 1:
            first = heapq.heappop(pq)
            second = heapq.heappop(pq)
            first += 1
            second += 1
            ret += 1
            if first:
                heapq.heappush(pq, first)
            if second:
                heapq.heappush(pq, second)

        if pq:
            return ret - pq[0]
        else:
            return ret