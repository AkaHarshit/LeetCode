# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def gcd(self, a, b):
        while b != 0:
            a, b = b, a % b
        return a
    
    def insertGreatestCommonDivisors(self, head):
        curr = head
        
        while curr and curr.next:
            g = self.gcd(curr.val, curr.next.val)
            new_node = ListNode(g)
            new_node.next = curr.next
            curr.next = new_node
            curr = new_node.next
        
        return head