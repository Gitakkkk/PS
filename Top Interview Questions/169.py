# 169. Majority Element

# 내가 작성한 코드
class Solution:
    def majorityElement(self, nums: List[int]) -> int:
        dic = {}
        for x in nums:
            if x not in dic: dic[x] = 1
            else: dic[x] += 1
        # 최대 값이 2개 이상인 경우
        [k for k,v in di.items() if max(di.values()) == v]
        # 최대 값이 1개인 경우
        return max(dic,key = dic.get)
        

# 다른 사람이 작성한 코드
# 정렬하여 가운데 값을 출력하면 최빈값
class Solution:
    def majorityElement(self, nums: List[int]) -> int:
        nums.sort()
        return nums[len(nums)//2]