# 숫자 2개씩 한 묶음으로 만든다고 했을 때,
# 첫 번째 값이 최소 값일 수밖에 없음.
class Solution:
    def arrayPairSum(self, nums: List[int]) -> int:
        # 처음부터 끝까지 간격 2 단위로 슬라이싱 : [1, 3]
        return sum(sorted(nums)[::2])
        
# Time : 332 ms
# Memory : 16.5 M

class Solution:
    def arrayPairSum(self, nums: List[int]) -> int:
        nums.sort()
        sum_ = 0
        # range의 세 번째 인자값: 증분값, 즉 2 간격씩 순회
        for i in range(0,len(nums),2):
            sum_ += nums[i]
        return sum_

# Time : 356 ms
# Memory : 16.7 M