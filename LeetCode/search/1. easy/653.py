# 653. Two Sum IV - Input is a BST

# 내가 작성한 코드
# BFS 사용
# q에 답고 정렬한 뒤, 좌/우 인덱스 하나씩 더하고 뺌
class Solution:
    def findTarget(self, root: Optional[TreeNode], k: int) -> bool:
        q = deque([root])
        _list = []
        while q:
            node = q.popleft()
            _list.append(node.val)
            if node.left: q.append(node.left)
            if node.right: q.append(node.right)
        _list.sort()
        left = 0
        right = len(_list)-1
        while left < right:
            if _list[left] + _list[right] == k: return True
            if _list[left] + _list[right] > k:
                right -= 1
            elif _list[left] + _list[right] < k:
                left += 1
        return False

# 다른 사람이 작성한 코드
# DFS, set 자료형 사용
# k - node.val 값이 set에 있으면 True, 없으면 val을 add
class Solution:
    def findTarget(self, root: Optional[TreeNode], k: int) -> bool:
        # dfs, set()에 담고 필요한 숫자가 set에 있으면 True
        
        def dfs(node, _set):
            if not node: return False
            if k - node.val in _set: return True
            _set.add(node.val)
            return dfs(node.left, _set) or dfs(node.right, _set)
        
        return dfs(root, set())