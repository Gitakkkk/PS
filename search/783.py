# 783. Minimum Distance Between BST Nodes

# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def minDiffInBST(self, root: Optional[TreeNode]) -> int:
        num = []
        
        def dfs(root, num):
            if root == None:
                return
            dfs(root.left, num)
            num.append(root.val)
            dfs(root.right, num)
        
        dfs(root, num)
        res = float('inf') # 양의 무한대
        for i in range(len(num)-1): # O(n)
            diff = num[i+1] - num[i]
            res = min(diff, res)
         
        return res