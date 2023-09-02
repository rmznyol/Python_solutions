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

############################################################

############################################################