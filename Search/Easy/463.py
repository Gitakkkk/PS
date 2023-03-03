# 463. Island Perimeter

class Solution:
    def islandPerimeter(self, grid: List[List[int]]) -> int:
        ans = 0
        for i in range(len(grid)):
            for j in range(len(grid[0])):
                if grid[i][j] == 1:
                    ans += 4
                    # 윗 라인과 비교해서 겹치면 - 2
                    # 가장 윗 라인을 도는 경우 그 위의 라인은 돌 필요가 없으므로 i > 0 조건 추가
                    # IndexError 방지 의미도 있음
                    if i > 0 and grid[i-1][j] == 1:
                        ans -= 2
                    # 왼쪽 라인과 비교해서 겹치면 - 2
                    # 가장 왼쪽 라인을 도는 경우 그 위의 라인은 돌 필요가 없으므로 j > 0 조건 추가
                    if j > 0 and grid[i][j-1] == 1:
                        ans -= 2
        return ans