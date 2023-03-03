# 515. Find Largest Value in Each Tree Row

# DFS
# 내부적으로 [level] 키가 있는듯
class Solution:
    def largestValues(self, root: Optional[TreeNode]) -> List[int]:
        res = []

        def dfs(node, level):
            if not node: return
            if len(res) -1 < level:
                res.append(node.val)
            else:
                res[level] = max(res[level], node.val)
            dfs(node.left, level+1)
            dfs(node.right, level+1)

        dfs(root, 0)
        return res

# BFS
class Solution:
    def largestValues(self, root: Optional[TreeNode]) -> List[int]:
        if not root: return None
        res = []
        q = deque([root])
        
        while q:
            temp = []
            for i in range(len(q)):
                node = q.popleft()
                temp.append(node.val)

                if node.left: q.append(node.left)
                if node.right: q.append(node.right)

            res.append(max(temp))

        return res