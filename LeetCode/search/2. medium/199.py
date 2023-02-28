# 199. Binary Tree Right Side View

# 내가 작성한 코드
# root로 [1,2]가 들어오는 테스트케이스에서 실패
# [1,2]면 2가 왼쪽 노드로 가는 거 아닌가? [1, null, 2]가 오른쪽 노드
class Solution:
    def rightSideView(self, root: Optional[TreeNode]) -> List[int]:
        if not root: return root
        
        ans = []
        
        def dfs(node):
            if not node: return
            nonlocal ans
            ans.append(node.val)
            dfs(node.right)
        
        dfs(root)
        return ans

# 다른 사람이 작성한 코드
class Solution:
    def rightSideView(self, root: Optional[TreeNode]) -> List[int]:
        def solve(root, level):
            if root:
                # 가장 오른쪽 노드
                if len(ans) == level:
                    res.append(root.val)
                solve(root.right, level+1)
                solve(root.left, level+1)
            return

        res = []
        solve(root, 0)
        return ans