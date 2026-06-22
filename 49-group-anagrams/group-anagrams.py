class Solution:
    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:
        hash_table = {}
        for s in strs:
            print(f"s = {s}")
            sorted_s = "".join(sorted(s))
            # print(f"  sorted_s = {sorted_s}")
            if sorted_s not in hash_table:
                hash_table[sorted_s] = []
            hash_table[sorted_s].append(s)
        #     print(f"  hash_table = {hash_table}")
        # print(f"final hash_table = {hash_table}")
        print(f"values hash_table = {list(hash_table.values())}")
        return list(hash_table.values())

# Time ~O(N)...~ O(N * K log K) where N is # of strings and K is max len of longest string
# Space ~O(N)...~ O(N*K)