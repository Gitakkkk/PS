# 530. Minimum Absolute Difference in BST

# 내가 작성한 코드
# 트리의 순서대로만 뺄 수 있음
class Solution:
    def getMinimumDifference(self, root: Optional[TreeNode]) -> int:
        ans = float('inf')
        def dfs(node, val):
            nonlocal ans
            if node == None: return
            if ans > abs(val - node.val): ans = abs(val - node.val)
            return dfs(node.left, node.val) or dfs(node.right, node.val)
        dfs(root, ans)
        return ans

# 다른 사람이 작성한 코드
# DFS를 사용하여 val들을 list에 append
# 그 list에서 가장 작은 값을 구함
class Solution:
    def getMinimumDifference(self, root: TreeNode) -> int:
        nums = []
        
        def dfs(node):
            if node == None: return
            nonlocal nums
            dfs(node.left)
            nums.append(node.val)
            dfs(node.right)
        
        dfs(root)
        return min(nums[i+1] - nums[i] for i in range(len(nums)-1))