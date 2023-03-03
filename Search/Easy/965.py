# 965. Univalued Binary Tree

# 내가 작성한 코드
# BFS를 사용하여 set 자료형에 담음
# set의 길이가 1이 아니라면 False 반환
class Solution:
    def isUnivalTree(self, root: Optional[TreeNode]) -> bool:
        q = deque([root])
        val = set()
        while q:
            node = q.popleft()
            val.add(node.val)
            if node.left: q.append(node.left)
            if node.right: q.append(node.right)

        return len(val) == 1

# 다른 사람이 작성한 코드
# DFS 사용
# list를 사용하지 않고 바로 set 자료형을 사용하는게 더 낫지 않을까?
class Solution:
    def isUnivalTree(self, root: Optional[TreeNode]) -> bool:
        if not root:
            return False

        def dfs(node):
            r = []
            if node.left:
                r = dfs(node.left)
            r.append(node.val)
            if node.right:
                r += dfs(node.right)
            
            return r

        if len(set(dfs(root))) == 1:
            return True
        return False