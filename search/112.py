# 112. Path Sum

# 내가 작성한 코드
class Solution:
    def hasPathSum(self, root: Optional[TreeNode], targetSum: int) -> bool:
        if not root: return False
        ans = []
        def dfs(node):
            nonlocal ans
            if not node:
                if sum(ans) == targetSum: return True
                else:
                    ans = ans[:-1]
                    return
            ans.append(node.val)
            return dfs(node)
        return dfs(root)

# 다른 사람이 작성한 코드
# targetSum에서 root.val의 값을 빼주면서 재귀적으로 함수를 실행하는 방식을 취함
# 마지막 줄에서 or을 통해 왼쪽 노드를 탐색해서 False 값이 나오면 오른쪽 노드도 탐색하는 방식을 취함
class Solution:
    def hasPathSum(self, root: Optional[TreeNode], targetSum: int) -> bool:
        if not root:
            return False
        if not root.left and not root.right: # leaf node
            return targetSum == root.val
        return self.hasPathSum(root.left, targetSum - root.val) or self.hasPathSum(root.right, targetSum - root.val)