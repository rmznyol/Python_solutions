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
