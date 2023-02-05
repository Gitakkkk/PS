# 1827. Minimum Operations to Make the Array Increasing
# enumerate 사용 시 [(0, 1), (1, 2), ...] 형태로 출력됨
class Solution:
    def minOperations(self, nums: List[int]) -> int:
        count = 0
        
        if len(nums) < 2:
            return count
        
        prev = None
        for i, num in enumerate(nums):
            if prev and num <= prev:
                count += prev - num + 1
                nums[i] = prev + 1
            prev = nums[i]
        
        return count