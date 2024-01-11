# 108. Convert Sorted Array to Binary Search Tree

class Solution:
    def sortedArrayToBST(self, nums: List[int]) -> Optional[TreeNode]:
        
        def bst(nums):
            if not nums: return None
            mid = len(nums)//2
            node = TreeNode(nums[mid])
            node.left = bst(nums[:mid])
            node.right = bst(nums[mid+1:])
            return node

        return bst(nums)