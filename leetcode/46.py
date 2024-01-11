# 46. Permutations

# 내가 작성한 답과 생각한 로직
# < 로직 >
# 1. 배열 내 모든 수를 사용하여 최대한 많은 경우의 배열을 만들어내는 것
# 2. 길이는 nums 배열과 동일해야 함
# 3. backtracking: 특정 조건을 만족하는 경우만 처리하는 알고리즘 기술
# 4. 새로운 배열 생성 후 nums의 각 요소 append, 같은 수면 continue, 같은 길이면 stop
# 5. 순서대로 돌 순 없음, 즉 뒤로 도는 방법도 고려해야 됨
# 6. ans 배열에 추가 후 새로운 배열은 초기화
# 7. 같은 길이가 될 때까지 계속 반복하면서 추가
# 8. 같은 길이로 만든 그 배열이 ans 배열에 들어있다면 while문 종료 후 return ans

class Solution:
    def permute(self, nums: List[int]) -> List[List[int]]:
        length = len(nums)
        ans = []
        temp = []
        while True:
            for x in nums:
                if x not in temp:
                    temp.append(x)
                if len(temp) == length:
                    ans.append(temp)
                    temp = []
                    break
            if temp in ans:
                break
        return ans


# 다른 사람이 작성한 답 #

class Solution:
    def permute(self, nums: List[int]) -> List[List[int]]:

        def backtrack(first):
            if first == len(nums):
                ans.append(nums[:]) # 모든 원소가 사용된 경우 해당 순열의 복사본을 만들어 ans에 추가
            for i in range(first, len(nums)):
                nums[first], nums[i] = nums[i], nums[first]
                backtrack(first + 1)
                nums[first], nums[i] = nums[i], nums[first]
            
        ans = []
        backtrack(0)
        return ans
