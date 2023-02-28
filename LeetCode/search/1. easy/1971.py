# 1971. Find if Path Exists in Graph

# 내가 작성한 코드
# source가 edges의 뒷부분에 있는 경우 처리 못함
class Solution:
    def validPath(self, n: int, edges: List[List[int]], source: int, destination: int) -> bool:
        if len(edges) == 0: return True
        route = set()
        q = deque(edges)
        while q:
            x, y = q.popleft()
            if x == source or y == source:
                route.add(x)
                route.add(y)
            if x in route: route.add(x)
            if y in route: route.add(y)
            if destination in route: return True
        return False

# 다른 사람이 작성한 코드
from collections import defaultdict
class Solution:
    def validPath(self, n: int, edges: List[List[int]], start: int, end: int) -> bool:
        adj_list = defaultdict(list)
        for k, v in edges:
            adj_list[k].append(v)
            adj_list[v].append(k)
        # defaultdict(<class 'list'>, {0: [1, 2], 1: [0, 2], 2: [1, 0]})
        visited = set()
        def dfs(node):
            if node == end: return True
            if node not in visited:
                visited.add(node)
                for edge in adj_list[node]:
                    res = dfs(edge)
                    if res: return True
        return dfs(start)