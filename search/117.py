# 117. Populating Next Right Pointers in Each Node II

class Solution:
    def connect(self, root: 'Node') -> 'Node':
        if not root: return None
        q = deque([root])
        while q:
            length = len(q)
            for i in range(length):
                node = q.popleft()
                if node.left: q.append(node.left)
                if node.right: q.append(node.right)
                if i != length -1 or not 1:
                    node.next = q[0]
                else:
                    node.next = None
        return root