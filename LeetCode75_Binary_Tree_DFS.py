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

from collections import deque, defaultdict
class Solution:
    def pathSum(self, root: Optional[TreeNode], targetSum: int) -> int:
        count = 0
        if root:
            root_dict = defaultdict(int)
            root_dict[0] = 1
            queue = deque([(root, 0, root_dict)])
            while queue:
                curr, sum_until, sums_until = queue.popleft()
                sum_until += curr.val
                # print(curr.val, sum_until, sums_until)
                # print(sum_until - targetSum,sums_until[sum_until - targetSum], count )
                count += sums_until[sum_until - targetSum]
                sums_until = sums_until.copy()
                sums_until[sum_until] += 1
                if curr.left:
                    queue.append((curr.left, sum_until, sums_until))
                if curr.right:
                    queue.append((curr.right, sum_until, sums_until))
        return count
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

from collections import deque
class Solution:
    def lowestCommonAncestor(self, root: 'TreeNode', p: 'TreeNode', q: 'TreeNode') -> 'TreeNode':
        
        #lets first record the ancestory:
        queue = deque([(root,[root])])
        records = {root:[root]}
        while p not in records or q not in records:
            curr, curr_ancestors = queue.popleft()
            if curr.left:
                curr_ancestors_left = curr_ancestors + [curr.left]
                records[curr.left] = curr_ancestors_left
                queue.append((curr.left,curr_ancestors_left))
            if curr.right:
                curr_ancestors_right = curr_ancestors + [curr.right]
                records[curr.right] = curr_ancestors_right
                queue.append((curr.right,curr_ancestors_right))
        q_records = {record:True for record in records[q]}
        for p_record in records[p][::-1]:
            if p_record in q_records:
                return p_record
        return None
