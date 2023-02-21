# 111. Minimum Depth of Binary Tree

class Solution:
    def minDepth(self, root: TreeNode) -> int:
        if not root: return 0
        queue = collections.deque([(root, 1)])
        ans = float("inf")
        while queue:
            node, level = queue.popleft()
            if not node.left and not node.right:
                return min(ans, level) - 1
            if node.left: queue.append((node.left, level+1))
            if node.right: queue.append((node.right, level+1))