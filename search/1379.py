# 1379. Find a Corresponding Node of a Binary Tree in a Clone of That Tree

class Solution:
    def getTargetCopy(self, original: TreeNode, cloned: TreeNode, target: TreeNode) -> TreeNode:
        targetVal = target.val

        def dfs(node):
            if node is None: return
            nonlocal targetVal
            if node.val == targetVal: return node
            return dfs(node.left) or dfs(node.right)

        return dfs(cloned)