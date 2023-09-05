# Definition for a binary tree node.
class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right

# 199. Binary Tree Right Side View
from collections import deque

class Solution:
    def rightSideView(self, root: Optional[TreeNode]) -> List[int]:
        results = []
        if root:
            queue = deque([(root,0)])
            heights = set()
            while queue:
                curr, height = queue.popleft()
                if height not in heights:
                    results.append(curr.val)
                    heights.add(height)
                if curr.right:
                    queue.append((curr.right, height+1))
                if curr.left:
                    queue.append((curr.left, height+1))
        return results

######################################################
# 1161. Maximum Level Sum of a Binary Tree

from collections import deque
class Solution:
    def maxLevelSum(self, root: Optional[TreeNode]) -> int:
        if root:
            mx, result = root.val, 1
            record = {0:[root.val]} 
            queue = deque([(root,1)])
            while queue:
                curr, level = queue.popleft()
                if level not in record:
                    if mx < sum(record[level-1]):
                        result = level - 1
                        mx = sum(record[level-1])
                    record[level] = []
                record[level].append(curr.val)
                if curr.left:
                    queue.append((curr.left, level+1))
                if curr.right:
                    queue.append((curr.right, level+1))
            if mx < sum(record[level]):
                result = level
        return result