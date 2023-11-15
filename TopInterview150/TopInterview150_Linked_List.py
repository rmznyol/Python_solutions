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
# 92. Reverse Linked List II
class Solution:
    def reverseBetween(self, head: Optional[ListNode], left: int, right: int) -> Optional[ListNode]:
        index = 0
        curr = head
        while current:
            if index == left:
                middle_head = curr
            if index == right:
                middle_tail == curr
            
            index += 1 
            curr = head.next

############################################################
# 25. Reverse Nodes in k-Group

class Solution:
    def reverse_a_group(self,head):
        before = None
        after = head
        while after:
            temp = after.next
            after.next = before
            before = after
            after = temp
        # should redurn head and tail
        return before, head # before is new head and head is new tail
    def reverseKGroup(self, head: Optional[ListNode], k: int) -> Optional[ListNode]:
        curr = head
        curr_prev = None
        while curr:
            count = 1
            inner_curr = curr
            # first we find a chunk of k nodes
            while count < k and inner_curr:
                count += 1
                inner_curr = inner_curr.next
            temp = inner_curr.next if inner_curr else None
            if inner_curr and count == k:
                inner_curr.next = None
                inner_head, inner_tail = self.reverse_a_group(curr)
                if curr_prev:
                    curr_prev.next = inner_head
                else:
                    head = inner_head
                inner_tail.next = temp
                curr_prev = inner_tail
            curr = temp
        return head
############################################################
# 19. Remove Nth Node From End of List
class Solution:
    def removeNthFromEnd(self, head: Optional[ListNode], n: int) -> Optional[ListNode]:
        if not head or not head.next:
            return None
        i = 0
        forward = head
        back = None
        while forward:
            print(forward.val,i)
            if i < n:
                i += 1
            else:
                back = back.next if back else head
                print(forward.val, back.val)
            forward = forward.next
        if n == i:
            if back:
                back.next = back.next.next
            else:
                head = head.next
            
        return head 

############################################################
# 82. Remove Duplicates from Sorted List II
class Solution:
    def deleteDuplicates(self, head: Optional[ListNode]) -> Optional[ListNode]:
        if head == None:
            return head
        counter = collections.defaultdict(int)
        curr = head
        while curr:
            counter[curr.val] += 1
            curr = curr.next
        new_head = new_curr = None
        curr = head
        while curr:
            if counter[curr.val] == 1:
                if not new_head: 
                    new_head = curr
                    new_curr = curr
                else:
                    new_curr.next = curr
                    new_curr = curr
            curr = curr.next 
        if new_curr:
            new_curr.next = None
        return new_head

############################################################
# 61. Rotate List

class Solution:
    def rotateRight(self, head: Optional[ListNode], k: int) -> Optional[ListNode]:
        if head:
            i = 1
            new_head_prev = None
            curr = head 
            pointer_store = {}
            while curr:
                pointer_store[i] = curr
                curr = curr.next
                i += 1
            k = k % (i-1)
            if k > 0:
                new_head_prev = pointer_store[i-1-k]
                new_head = new_head_prev.next
                new_head_prev.next = None
                curr2 = new_head
                while curr2.next:
                    curr2 = curr2.next
                curr2.next = head
                return new_head
            return head
        
############################################################
