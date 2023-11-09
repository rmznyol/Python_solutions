# 141. Linked List Cycle
class Solution:
    def hasCycle(self, head: Optional[ListNode]) -> bool:
        temp = head
        record = {}
        while temp != None:
            if record.get(temp) != None:
                return True
            record[temp] = True
            temp = temp.next
############################################################
# 2. Add Two Numbers

class Solution:
    def addTwoNumbers(self, l1: Optional[ListNode], l2: Optional[ListNode]) -> Optional[ListNode]:
        # Definition for singly-linked list.
        a=ListNode((l1.val+l2.val)%10)
        temp=a
        carry=(l1.val+l2.val)//10
        l1,l2=l1.next,l2.next
        while (l1 is not None) and (l2 is not None):
            temp.next=ListNode((l1.val+l2.val+carry)%10)
            carry=(l1.val+l2.val+carry)//10
            l1,l2=l1.next,l2.next
            temp=temp.next
        while (l1 is not None):
            temp.next=ListNode((l1.val+carry)%10)
            carry=(l1.val+carry)//10
            l1=l1.next
            temp=temp.next
        while (l2 is not None):
            temp.next=ListNode((l2.val+carry)%10)
            carry=(l2.val+carry)//10
            l2=l2.next
            temp=temp.next
        if carry>0:
            temp.next=ListNode(carry)
        return a

############################################################
# 21. Merge Two Sorted Lists
class Solution:
    def mergeTwoLists(self, list1: Optional[ListNode], list2: Optional[ListNode]) -> Optional[ListNode]:
        p1 = list1
        p2 = list2
        p3 = head = ListNode()
        while p1 and p2:
            if p1.val < p2.val:
                p3.next = p1
                p3 = p1
                p1 = p1.next
            else:
                p3.next = p2
                p3 = p2
                p2 = p2.next
        if p1 is None:
            p3.next = p2
        else:
            p3.next = p1 
        return head.next 
    
############################################################