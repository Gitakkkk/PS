# 내가 제출한 답 (이중 for문을 돌기 때문에 시간복잡도는 O(n * n))
class Solution:
    def answerQueries(self, nums: List[int], queries: List[int]) -> List[int]:
        nums.sort()
        result = []
        for x in queries:
            temp = 0
            tempArr = []
            for y in nums:
                temp += y
                if x >= temp: tempArr.append(y)
            result.append(len(tempArr))
        return result

# 다른 사람이 제출한 답: bisect 라이브러리를 사용 + 시간복잡도 면에서 우월
class Solution:
    def answerQueries(self, nums: List[int], queries: List[int]) -> List[int]:
        nums.sort()
        # range 사용 시 idx로 접근
        # queries의 원소와 비교할 때, nums의 두 번째 원소부터는 누계로 계산함
        for i in range(1, len(nums)):
            nums[i] += nums[i - 1]
        answer = []
        
        for query in queries:
            # bisect 라이브러리는 원소들이 정렬된 리스트에서 특정 원소를 찾을 때 효과적
            # Binary Search 구현에 효과적
            # Linked list 자료구조
            # 정렬 순서에 맞춰 query가 들어갈 index를 반환, bisect_left도 있음
            index = bisect.bisect_right(nums, query)
            answer.append(index)
            
        # return answer
        return 1

        