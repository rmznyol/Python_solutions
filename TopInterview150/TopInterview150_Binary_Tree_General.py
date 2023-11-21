# 104. Maximum Depth of Binary Tree

class Solution:
    def maxDepth(self, root: Optional[TreeNode]) -> int:
        def depth(curr):
            if not curr:
                return 0
            return 1 + max([depth(curr.left),depth(curr.right)])
        return depth(root)
    
########################################################
# 100. Same Tree

from collections import deque
class Solution:
    def isSameTree(self, p: Optional[TreeNode], q: Optional[TreeNode]) -> bool:
        if not q and not p:
            return True
        if (not q and p) or (q and not p):
            return False
        queue = [p,q]
        while queue:
            qcurr = queue.pop()
            pcurr = queue.pop()
            if qcurr.val != pcurr.val:
                return False
            if (qcurr.left and not pcurr.left) or (not qcurr.left and pcurr.left):
                return False
            if (qcurr.right and not pcurr.right) or (not qcurr.right and pcurr.right):
                return False
            if qcurr.left:
                queue += [qcurr.left, pcurr.left]
            if qcurr.right:
                queue += [qcurr.right, pcurr.right]

        return True
########################################################
# 226. Invert Binary Tree
from collections import deque
class Solution:
    def invertTree(self, root: Optional[TreeNode]) -> Optional[TreeNode]:
        if root == None:
            return root
        my_queue = deque([root])
        while len(my_queue) > 0:
            temp = my_queue.popleft()
            if temp.left:
                my_queue.append(temp.left)
            if temp.right:
                my_queue.append(temp.right)
            switch = temp.left
            temp.left = temp.right
            temp.right = switch
        return root
########################################################
# 101. Symmetric Tree
from collections import deque
class Solution:
    def isSymmetric(self, root: Optional[TreeNode]) -> bool:
        if not root or (not root.left and not root.right):
            return True
        if not root.left and root.right:
            return False
        if root.left and not root.right:
            return False
        if root.left.val != root.right.val:
            return False
        leftq = deque([root.left])
        rightq = deque([root.right])
        while len(leftq) > 0:
            temp_left = leftq.popleft()
            temp_right = rightq.popleft()
            if temp_left.left and temp_right.right:
                if temp_left.left.val != temp_right.right.val:
                    return False
                leftq.append(temp_left.left)
                rightq.append(temp_right.right)
            elif (temp_left.left and not temp_right.right) or (not temp_left.left and temp_right.right):
                return False
            if temp_left.right and temp_right.left:
                if temp_left.right.val != temp_right.left.val:
                    return False
                leftq.append(temp_left.right)
                rightq.append(temp_right.left)
            elif (temp_left.right and not temp_right.left) or (not temp_left.right and temp_right.left):
                return False
        return True
########################################################
