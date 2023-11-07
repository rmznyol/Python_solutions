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