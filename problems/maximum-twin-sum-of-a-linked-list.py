## https://leetcode.com/problems/maximum-twin-sum-of-a-linked-list

# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def pairSum(self, head: Optional[ListNode]) -> int:
        slow = head
        fast = head

        while fast is not None and fast.next is not None:
            slow = slow.next
            fast = fast.next.next

        prev = None
        current = slow

        while current is not None:
            nextNode = current.next
            current.next = prev
            prev = current
            current = nextNode

        maxSum = 0
        right = head
        left = prev

        while left is not None:
            currentSum = right.val + left.val
            if currentSum >  maxSum:
                maxSum = currentSum
            right = right.next
            left = left.next
        

        return maxSum

        
