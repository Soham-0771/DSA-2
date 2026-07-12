# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def allPossibleFBT(self, n: int) -> List[Optional[TreeNode]]:
        memo = {}
        def build(nodes):
            if nodes in memo:
                return memo[nodes]

            if nodes == 1:
                return [TreeNode(0)]

            if nodes % 2 == 0:
                return []

            res = []

            for left_nodes in range(1, nodes, 2):
                right_nodes = nodes - 1 - left_nodes

                for left in build(left_nodes):
                    for right in build(right_nodes):
                        root = TreeNode(0)
                        root.left = left
                        root.right = right
                        res.append(root)

            memo[nodes] = res
            return res

        return build(n)
