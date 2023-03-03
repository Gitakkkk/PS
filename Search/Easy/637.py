# 637. Average of Levels in Binary Tree

class Solution:
    def averageOfLevels(self, root: Optional[TreeNode]) -> List[float]:
        q=deque([root])
        ans =[]
        while q:
            # leaf node의 길이는 0
            qlen=len(q)
            val =0
            for i in range(qlen):
                node = q.popleft()
                val += node.val
                if node.left: q.append(node.left)
                if node.right: q.append(node.right)
            ans.append(val/qlen)
        return ans
