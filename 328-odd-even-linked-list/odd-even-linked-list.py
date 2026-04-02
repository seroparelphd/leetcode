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
        # 1. Immediate exit for small lists (saves time/memory)
        if not head or not head.next or not head.next.next:
            return head
        
        # 2. Use pointers only. Do not create ANY new lists or nodes.
        odd = head
        even = head.next
        even_head = even # Save the starting point of the even chain

        while even and even.next:
            # Re-wire the 'next' pointers in-place
            odd.next = even.next
            odd = odd.next
            even.next = odd.next
            even = even.next
        
        # 3. Stitch the odd tail to the even head
        odd.next = even_head
        return head