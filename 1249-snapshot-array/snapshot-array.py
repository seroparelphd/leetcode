class SnapshotArray:

    def __init__(self, length: int):
        self.snap_n = 0
        self.history = [[[-1, 0]] for _ in range(length)]
        
    def set(self, index: int, val: int) -> None:
        self.history[index].append([self.snap_n, val])

    def snap(self) -> int:
        self.snap_n += 1
        return self.snap_n - 1

    def get(self, index: int, snap_id: int) -> int:
        idx = bisect_right(self.history[index], snap_id, key=lambda x: x[0])
        return self.history[index][idx - 1][1]
        # return bisect_right(self.history[index], snap_id)

        # print(f"index = {index} | snap_id = {snap_id} | self.history = {self.history} | self.history[snap_id][index] = {self.history[snap_id][index]}")

# Your SnapshotArray object will be instantiated and called as such:
# obj = SnapshotArray(length)
# obj.set(index,val)
# param_2 = obj.snap()
# param_3 = obj.get(index,snap_id)