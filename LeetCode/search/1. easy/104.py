# 104. Maximum Depth of Binary Tree

class Solution:
    def maxDepth(self, root: Optional[TreeNode]) -> int:
        def dfs(root, ans):
            if not root: return ans
            return max(dfs(root.left, ans+1), dfs(root.right, ans+1))
        return dfs(root, 0)