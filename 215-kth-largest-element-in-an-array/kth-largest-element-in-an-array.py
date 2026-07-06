class Solution:
    def findKthLargest(self, nums: List[int], k: int) -> int:
        min_heap = nums[:k]
        # print(f"min_heap = {min_heap}")
        heapq.heapify(min_heap)        
        # print(f"heapq.heapify(min_heap) = {min_heap}")
        for num in nums[k:]:
            # print(f"num = {num}")
            if num > min_heap[0]:
                # heapq.heappushpop(min_heap, num)
                heapq.heapreplace(min_heap, num)
            # print(f"  min_heap = {min_heap}")
        return min_heap[0]