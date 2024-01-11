# 133. Clone Graph

# BFS를 통해 neighbors 프로퍼티에 하나씩 추가
class Solution:
    def cloneGraph(self, node: 'Node') -> 'Node':
        if not node: return node
        q, clones = deque([node]), {node.val: Node(node.val, [])}

        while q:
            cur = q.popleft()
            cur_clone = clones[cur.val]

            for x in cur.neighbors:
                if x.val not in clones:
                    clones[x.val] = Node(x.val, [])
                    q.append(x)
                cur_clone.neighbors.append(clones[x.val])
            
        return clones[node.val]