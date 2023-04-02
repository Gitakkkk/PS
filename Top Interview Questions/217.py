# 217. Contains Duplicate

# 내가 작성한 코드
# dict 사용
class Solution:
    def containsDuplicate(self, nums: List[int]) -> bool:
        cont = dict()

        for x in nums:
            if x in cont: cont[x] += 1
            else: cont[x] = 1
        
        for x in cont.values():
            if x > 1: return 1
        
        return 0

# 다른 사람이 작성한 코드
# set 사용
class Solution:
    def containsDuplicate(self, nums: List[int]) -> bool:
        num_set = set(nums)
        if len(nums) != len(num_set):
            return True
        else:
            return False