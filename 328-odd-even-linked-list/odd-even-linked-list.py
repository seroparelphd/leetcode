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
        if not head or not head.next:
            return head
        
        # Step 1: Collect all values into an array (Beginner-friendly)
        values = []
        curr = head
        while curr:
            values.append(curr.val)
            curr = curr.next
            
        # Step 2: Separate odds and evens based on index
        # This creates extra intermediate lists in memory
        odds = [values[i] for i in range(len(values)) if i % 2 == 0]
        evens = [values[i] for i in range(len(values)) if i % 2 != 0]
        
        # Step 3: Combine them
        combined = odds + evens
        
        # Step 4: Rebuild the linked list
        # This involves another O(N) pass and potential object creation
        dummy = ListNode(0)
        curr = dummy
        for val in combined:
            curr.next = ListNode(val) # Creating brand new nodes is memory intensive
            curr = curr.next
            
        return dummy.next