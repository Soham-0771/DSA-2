class Solution:
    def rob(self, root: Optional[TreeNode]) -> int:
        def dfs(node):
            if not node:
                return (0, 0)

            left_rob, left_not = dfs(node.left)
            right_rob, right_not = dfs(node.right)

            rob_current = node.val + left_not + right_not

            not_rob_current = (
                max(left_rob, left_not)
                + max(right_rob, right_not)
            )

            return (rob_current, not_rob_current)

        return max(dfs(root))