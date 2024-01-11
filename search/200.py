# 200. Number of Islands

# 이차원 매트릭스의 탐색공식이라고 생각하고 일단 외우기!
class Solution:
    def numIslands(self, grid: List[List[str]]) -> int:
        ans = 0
        rows = len(grid)
        cols = len(grid[0])

        def dfs(row, col):
            # row와 col이 범위를 벗어나거나 water라면 반환
            if row < 0 or row == rows or col < 0 or col == cols: return
            if grid[row][col] != '1': return

            grid[row][col] = 'v'
            
            dfs(row-1, col)
            dfs(row+1, col)
            dfs(row, col-1)
            dfs(row, col+1)

        for row in range(rows):
            for col in range(cols):
                if grid[row][col] == '1':
                    dfs(row, col)
                    ans += 1

        return ans