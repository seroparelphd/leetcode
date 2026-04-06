# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def pairSum(self, head: Optional[ListNode]) -> int:
        head_list = []
        current = head
        while current:
            head_list.append(current.val)
            current = current.next
        # print(head_list)
        max_twin_sum = float(-inf)
        head_list_len = len(head_list)
        r = head_list_len - 1
        # for l in range(head_list_len/2 - 1):
        l = 0
        print(head_list[l])
        while l < r:
            # print(head_list[l])
            max_twin_sum = max(max_twin_sum, head_list[l] + head_list[r])
            print(max_twin_sum)
            l += 1
            r -= 1
        return max_twin_sum
