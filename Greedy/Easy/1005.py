# 1005. Maximize Sum Of Array After K Negations

# 내가 작성한 코드
# 매번 sort를 하기 때문에 시간복잡도 면에서 답이 없음
class Solution:
    def largestSumAfterKNegations(self, nums: List[int], k: int) -> int:
        nums.sort()
        while k > 0:
            nums.sort()
            if nums[0] == 0: return sum(nums)
            if nums[0] > 0:
                while k > 0:
                    nums[0] = -nums[0]
                    k -= 1
                    if k == 0: 
                        return sum(nums)
            nums[0] = -nums[0]
            k -= 1
        return sum(nums)

# 다른 사람이 작성한 코드
# 비슷한 논리로 간 거 같지만 if문에서 두 가지 조건을 더 제시함
# i+1 < len(nums) and abs(nums[i]) >= abs(nums[i+1])
class Solution:
    def largestSumAfterKNegations(self, nums: List[int], k: int) -> int:
        nums.sort()

        i = 0
        while i < len(nums) and k > 0:
            nums[i] = -nums[i]
            if nums[i] > 0 and i+1 < len(nums) and abs(nums[i]) >= abs(nums[i+1]):
                i += 1
            k -= 1

        return sum(nums)