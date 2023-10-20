# 48. Rotate Image

# 내가 작성한 코드
# matrix 리스트에 값을 할당하여도 matrix의 값이 변하지 않는다.
# matrix의 값을 변하게 하려면 matrix의 값을 직접 변경해야 한다.
class Solution:
    def rotate(self, matrix: List[List[int]]) -> None:
        """
        Do not return anything, modify matrix in-place instead.
        """
        ans = []
        for i in range(len(matrix)):
            ans.append([])
        for i in reversed(range(len(matrix))):
            for j in range(len(matrix[0])):
                ans[j][i] = matrix[i][j]
        matrix = ans

# 다른 사람이 작성한 코드
class Solution:
    def rotate(self, matrix: List[List[int]]) -> None:
        """
        Do not return anything, modify matrix in-place instead.
        """
        for i in range(len(matrix)):
            for j in range(i, len(matrix)):
                matrix[i][j], matrix[j][i] = matrix[j][i], matrix[i][j]
        for i in range(len(matrix)):
            matrix[i].reverse()
