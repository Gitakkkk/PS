# 559. Maximum Depth of N-ary Tree

# BFS 사용
# 깊이 구하는 문제는 queue 자료구조 사용하여 해결
class Solution:
    def maxDepth(self, root: 'Node') -> int:
        if not root: return 0

        q = deque([(root, 1)])
        depth = 1

        while q:
            node, val = q.popleft()
            depth = val
            if node.children:
                for child in node.children:
                    q.append([child, val+1])
        
        return depth