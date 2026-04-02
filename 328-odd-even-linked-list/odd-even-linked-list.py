# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def oddEvenList(self, head: Optional[ListNode]) -> Optional[ListNode]:
#         if not head:
#             return None
        
#         odd = head
#         even = head.next
#         even_head = even

#         while even and even.next:
#             # print(even.val)
#             odd.next = even.next
#             odd = odd.next
#             even.next = odd.next
#             even = even.next
#         odd.next = even_head
#         return head

# class Solution:
#     def oddEvenList(self, head: Optional[ListNode]) -> Optional[ListNode]:
        # Minimalist edge case handling
        if not head or not head.next:
            return head
        
        odd = head
        even = head.next
        even_head = even # The only 'extra' pointer we truly need

        while even and even.next:
            # We are re-linking existing nodes, not creating new ones.
            # Space Complexity: O(1)
            odd.next = even.next
            odd = odd.next
            even.next = odd.next
            even = even.next
        
        odd.next = even_head
        return head