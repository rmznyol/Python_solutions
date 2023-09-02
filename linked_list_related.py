# Definition for singly-linked list.
class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next

# 1721. Swapping Nodes in a Linked List

class Solution:
    def swapNodes(self, head: Optional[ListNode], k: int) -> Optional[ListNode]:
        temp = head
        index = 0
        record = {}
        while temp:
            record[index] = temp
            index += 1 
            temp = temp.next
        if record:
            record[k-1].val, record[index-k].val = record[index-k].val, record[k-1].val
        return head

##############################################################################################################

# 2095. Delete the Middle Node of a Linked List

class Solution:
    def deleteMiddle(self, head: Optional[ListNode]) -> Optional[ListNode]:
        if not head or not head.next:
            return None
        slow = None
        fast = head
        while fast and fast.next:
            fast = fast.next.next
            slow = slow.next if slow else head
        slow.next = slow.next.next
        return head
        
