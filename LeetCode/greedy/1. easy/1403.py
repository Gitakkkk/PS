# 내가 제출한 답: result 배열을 만들어서 append & return
class Solution:
    def minSubsequence(self, nums: List[int]) -> List[int]:
        nums.sort(reverse=True)
        _sum = sum(nums)
        result = []
        for x in nums:
            sum_result = sum(result)
            if sum_result > _sum - sum_result:
                break
            result.append(x)
        return result

# 다른 사람이 제출한 답: if문에 걸렸을 때 nums에서 slicing을 통해 return (시간복잡도 우월)
class Solution:
    def minSubsequence(self, nums: List[int]) -> List[int]:
        nums.sort(reverse=True)
        total = sum(nums)
        s = 0
        for i in range(len(nums)):
            s += nums[i]
            if s > total - s:
                return nums[:i + 1]

                