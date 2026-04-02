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
        
        # Step 1: Dump all node values into a standard Python list
        values = []
        curr = head
        while curr:
            values.append(curr.val)
            curr = curr.next
            
        # Step 2: Separate the values by index into two lists
        odds = []
        evens = []
        for i in range(len(values)):
            if (i + 1) % 2 != 0: # Using 1-based indexing as per problem
                odds.append(values[i])
            else:
                evens.append(values[i])
        
        # Step 3: Combine them (Odds first, then Evens)
        combined = odds + evens
        
        # Step 4: Rebuild the linked list by overwriting values in the original
        curr = head
        for val in combined:
            curr.val = val
            curr = curr.next
            
        return head