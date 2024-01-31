class Solution:
    def merge(self, nums1: List[int], m: int, nums2: List[int], n: int) -> None:
        """
        Do not return anything, modify nums1 in-place instead.
        """
        ans = []
        
        for i in range(m):
            ans.append(nums1[i])
        for i in range(n):
            ans.append(nums2[i])

        ans.sort()
        nums1.clear()
        
        for i in range(len(ans)):
            nums1.append(ans[i])