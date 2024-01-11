# 807. Max Increase to Keep City Skyline
class Solution:
    def maxIncreaseKeepingSkyline(self, grid: List[List[int]]) -> int:
        # 요소 0을 len(grid), len(grid[0])만큼 늘리기.
        rows_max = [0] * len(grid)
        cols_max = [0] * len(grid[0])

        # rows_max는 매번 원소를 비교하지만, cols_max는 인덱스 j마다 비교하기 때문에 1/4번마다 비교
        for i in range(len(grid)):
            for j in range(len(grid[0])):
                rows_max[i] = max(rows_max[i], grid[i][j])
                cols_max[j] = max(cols_max[j], grid[i][j])

        res = 0
        for i in range(len(grid)):
            for j in range(len(grid[0])):
                res += min(rows_max[i], cols_max[j]) - grid[i][j]

        return res