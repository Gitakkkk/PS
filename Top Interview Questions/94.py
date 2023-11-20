# 94. Binary Tree Inorder Traversal

class Solution:
    def inorderTraversal(self, root: Optional[TreeNode]) -> List[int]:
        res = []

        def dfs(root):
            if root == None: return
            
            dfs(root.left)
            res.append(root.val)
            dfs(root.right)
        
        dfs(root)

        return res
