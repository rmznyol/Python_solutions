# Definition for singly-linked list.
class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next

# 1721. Swapping Nodes in a Linked List (EXTRA)
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
##############################################################################################################
# 328. Odd Even Linked List

class Solution:
    def oddEvenList(self, head: Optional[ListNode]) -> Optional[ListNode]:
        
        if head == None or head.next == None:
            return head 
        temp_odd = head
        temp_even = head.next
        middle_head = head.next
        i = 1 
        temp = head.next.next
        while temp:
            if i % 2 != 0:
                temp_odd.next = temp
                temp_odd = temp_odd.next

            else:
                temp_even.next = temp
                temp_even = temp_even.next
            i += 1
            temp = temp.next
        temp_even.next = None
        temp_odd.next = middle_head

        return head
##############################################################################################################
# 206. Reverse Linked List

class Solution:
    def reverseList(self, head: Optional[ListNode]) -> Optional[ListNode]:
        if head == None:
            return head
        before = None
        after = head
        while after!= None:
            temp = after
            after = after.next
            temp.next = before
            before = temp
        return before
##############################################################################################################
# 2130. Maximum Twin Sum of a Linked List    
