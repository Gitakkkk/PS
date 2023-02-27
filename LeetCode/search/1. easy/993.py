# 993. Cousins in Binary Tree

# 내가 작성한 코드
# 부모 노드 값 저장할 방법 못 찾음
class Solution:
    def isCousins(self, root: Optional[TreeNode], x: int, y: int) -> bool:
        if not root: return False
        q = deque([(root, 1)])
        depX = depY = float('inf')
        while q:
            node, val = q.popleft()
            if node.val == x: depX = val
            if node.val == y: depY = val
            if node.left: q.append([node.left, val+1])
            if node.right: q.append([node.right, val+1])
        
        return depX == depY
    
# 다른 사람이 작성한 코드
# 부모 노드를 tuple 자료형으로 함께 저장
class Solution:
    def isCousins(self, root: TreeNode, x: int, y: int) -> bool:
        res = []
		
        queue = deque([(root, None, 0)])        
        while queue:
            if len(res) == 2:
                break
            node, parent, depth = queue.popleft()
            if node.val == x or node.val == y:
                res.append((parent, depth))
            if node.left:
                queue.append((node.left, node, depth + 1))
            if node.right:
                queue.append((node.right, node, depth + 1))

        node_x, node_y = res
		
        return node_x[0] != node_y[0] and node_x[1] == node_y[1]