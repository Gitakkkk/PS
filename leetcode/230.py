# 230. Kth Smallest Element in a BST

# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def kthSmallest(self, root: Optional[TreeNode], k: int) -> int:
        # 전체 노드들 중 k번째로 작은 수 찾기
        nodeList = []

        def searched(root):
            if root == None: return

            searched(root.left)
            nodeList.append(root.val)
            searched(root.right)

        searched(root)

        return nodeList[k-1]