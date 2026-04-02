# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
# class Solution:
#     def oddEvenList(self, head: Optional[ListNode]) -> Optional[ListNode]:
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

class Solution:
    def oddEvenList(self, head: Optional[ListNode]) -> Optional[ListNode]:
        if not head: return None

        # Helper generator to yield values by position
        def get_values(is_odd):
            curr = head
            idx = 1
            while curr:
                # Yield if we want odd positions (1, 3, 5...) 
                # or even positions (2, 4, 6...)
                if (idx % 2 != 0) == is_odd:
                    yield curr.val
                curr = curr.next
                idx += 1

        # Reconstruct the list using the generator
        dummy = ListNode(0)
        curr = dummy
        
        # Pass 1: Add all odds
        for val in get_values(is_odd=True):
            curr.next = ListNode(val)
            curr = curr.next
            
        # Pass 2: Add all evens
        for val in get_values(is_odd=False):
            curr.next = ListNode(val)
            curr = curr.next
            
        return dummy.next