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
# 138. Copy List with Random Pointer

class Solution:
    def copyRandomList(self, head: 'Optional[Node]') -> 'Optional[Node]':
        if head is None:
            return None
        pointer_dict=dict()
        temp=head
        head2=Node(head.val)
        if temp.random==temp:
            head2.random=head2
        elif temp.random is not None:
            nn=Node(temp.random.val)
            head2.random=nn
            pointer_dict[head.random]=nn
        connected_dict=dict()
        connected_dict[head]=head2
        temp=temp.next
        temp2=head2
        while temp is not None:
            if temp in pointer_dict:
                nn=pointer_dict[temp]
            else:
                nn=Node(temp.val)
            connected_dict[temp]=nn
            temp2.next=nn
            if temp.random is not None:
                if temp.random in connected_dict:
                    nn.random=connected_dict[temp.random]
                elif temp.random in pointer_dict:
                    nn.random=pointer_dict[temp.random]
                else:
                    nnn=Node(temp.random.val)
                    nn.random=nnn
                    pointer_dict[temp.random]=nnn   
            temp2=nn
            temp=temp.next
        return head2

############################################################