# 513. Find Bottom Left Tree Value

class Solution:
    def findBottomLeftValue(self, root: Optional[TreeNode]) -> int:
        ans = 0
        q = deque([(root, 1)])

        while q:
            node, level = q.popleft()
            ans = node.val
            if node.right: q.append((node.right, level+1))
            if node.left: q.append((node.left, level+1))

        return ans