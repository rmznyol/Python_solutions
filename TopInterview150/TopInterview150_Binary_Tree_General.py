# 104. Maximum Depth of Binary Tree

class Solution:
    def maxDepth(self, root: Optional[TreeNode]) -> int:
        def depth(curr):
            if not curr:
                return 0
            return 1 + max([depth(curr.left),depth(curr.right)])
        return depth(root)