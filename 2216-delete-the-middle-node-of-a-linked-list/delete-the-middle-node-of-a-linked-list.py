# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def deleteMiddle(self, head: Optional[ListNode]) -> Optional[ListNode]:
        if not head or not head.next:
            return None

        # Get length
        length = 0
        current = head
        while current:
            length += 1
            current = current.next
        # print(length)

        # Find middle and skip it
        # middle = (length - 1) // 2
        middle = (length - 2) // 2
        # print(middle)
        curr = head
        for i in range(middle):
            curr = curr.next
        curr.next = curr.next.next
        
        return head

# Time: O(2n) -> O(n)
# Space O(4) -> O(1)