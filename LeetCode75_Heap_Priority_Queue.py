# 215. Kth Largest Element in an Array

from heapq import heappush, heappushpop
class Solution:
    def findKthLargest(self, nums: List[int], k: int) -> int:
        heap = []
        for num in nums:
            if len(heap) < k:
                heappush(heap, num)
            else:
                heappushpop(heap,num)
        return heap[0]
############################################################
# 2336. Smallest Number in Infinite Set
class SmallestInfiniteSet:

    def __init__(self):
        self.set = []
        self.removed = set()

    def popSmallest(self) -> int:
        to_be_removed = 1
        while to_be_removed in self.removed:
            to_be_removed += 1 
        self.removed.add(to_be_removed)
        return to_be_removed
    def addBack(self, num: int) -> None:
        self.removed.discard(num)
############################################################

############################################################
#2462. Total Cost to Hire K Workers

from heapq import heapify, heappop
class Solution:
    def totalCost(self, costs: List[int], k: int, candidates: int) -> int:
        total_cost = 0
        left = candidates
        right = len(costs) - candidates
        if candidates <= len(costs) / 2:
            heap = [(cost,index,True) for index,cost in enumerate(costs[:left])]
            heap += [(cost, right + index, False) for index,cost in enumerate(costs[right:])]
        else:
            heap = [(cost,index,True) for index,cost in enumerate(costs)]
        heapify(heap)
        while k:
            cost, index, on_left = heappop(heap)
            total_cost += cost
            k -= 1
            if left < right:
                if on_left :
                    heappush(heap,(costs[left], left, True))
                    left += 1
                else:
                    right -= 1
                    heappush(heap,(costs[right], right, False))
        return total_cost
