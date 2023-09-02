# 104. Maximum Depth of Binary Tree

class Solution:
    def maxDepth(self, root: Optional[TreeNode]) -> int:
        def depth(curr):
            if not curr:
                return 0
            return 1 + max([depth(curr.left),depth(curr.right)])
        return depth(root)
#################################################################
#872. Leaf-Similar Trees

class Solution:
    def leafSimilar(self, root1: Optional[TreeNode], root2: Optional[TreeNode]) -> bool:
        def traverse(temp):
            if temp:
                if not (temp.left or temp.right):
                    record.append(temp.val)
                traverse(temp.left)
                traverse(temp.right)
        record = []
        traverse(root1)
        record1 = record
        record = []
        traverse(root2)
        return record1 == record
#################################################################
# 1448. Count Good Nodes in Binary Tree

class Solution:
    def goodNodes(self, root: TreeNode) -> int:
        count = 0 
        def path_recorder(curr, max_until = None):
            nonlocal count
            if curr:
                if max_until is None:
                    count = 1
                elif curr.val >= max_until:
                    count += 1
                max_until = max_until if max_until and max_until > curr.val else curr.val
                path_recorder(curr.left, max_until)
                path_recorder(curr.right, max_until)
        path_recorder(root)
        return count
#################################################################
# 437. Path Sum III

#################################################################
# 1372. Longest ZigZag Path in a Binary Tree

class Solution:
    def longestZigZag(self, root: Optional[TreeNode]) -> int:
        mx = 0
        def traverse(curr, last = None, zcount = 0):
            if curr:
                nonlocal mx
                if last == 'right':
                    mx = mx if mx > zcount else zcount 
                    traverse(curr.left,'left',zcount + 1)
                else:
                    traverse(curr.left,'left', 1)
                if last == 'left':
                    mx = mx if mx > zcount else zcount 
                    traverse(curr.right,'right', zcount + 1)
                else:
                    traverse(curr.right,'right', 1)
                
        traverse(root)
        return mx 
#################################################################
# 236. Lowest Common Ancestor of a Binary Tree