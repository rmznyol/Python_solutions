# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

#530. Minimum Absolute Difference in BST

class Solution:
    def getMinimumDifference(self, root: Optional[TreeNode]) -> int:
        ordered = []
        def in_order(root):
            if root:
                in_order(root.left)
                ordered.append(root.val)
                in_order(root.right)
        in_order(root)
        mn = float('inf')
        for after, before in zip(ordered[1:],ordered[:-1]):
            mn = min(after - before, mn)
        return mn
    
########################################################
# 230. Kth Smallest Element in a BST
class Solution:
    def kthSmallest(self, root: Optional[TreeNode], k: int) -> int:
        stack = [root]
        res = []
        while stack:
            curr = stack.pop()
            while curr:
                stack.append(curr)
                curr = curr.left
            curr = stack.pop()
            res.append(curr.val)

########################################################
# 98. Validate Binary Search Tree
from collections import deque
class Solution:
    def isValidBST(self, root: Optional[TreeNode]) -> bool:
        if root is None:
            return True 
        queue = deque([(root,-2**31-1,2**31)])
        while len(queue) > 0:
            cur, low, high = queue.popleft()
            if cur.val >= high or cur.val <= low:
                return False
            if cur.left:
                queue.append((cur.left,low,min(cur.val,high)))
            if cur.right:
                queue.append((cur.right,max(cur.val,low), high))
        return True