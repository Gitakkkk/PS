class Solution:
    def minimumOperations(self, nums: List[int]) -> int:
        # set 내 요소 0 제거, remove(0)과 동일하지만 한 줄로 처리 가능
        return len(set(nums)-{0})

        