# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def mergeNodes(self, head: Optional[ListNode]) -> Optional[ListNode]:
        curr = head.next   
        dummy = ListNode(0)
        tail = dummy
        current_sum = 0
        while curr:
            if curr.val == 0:
                tail.next = ListNode(current_sum)
                tail = tail.next
                current_sum = 0
            else:
                current_sum += curr.val
            curr = curr.next
        return dummy.next