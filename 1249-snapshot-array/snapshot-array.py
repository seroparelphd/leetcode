class SnapshotArray:

    def __init__(self, length: int):
        '''
        initializes an array-like data structure with the given length. 
        Initially, each element equals 0—BUT HOW?!
        '''
        self.id = 0
        self.history = [[[-1, 0]] for _ in range(length)]

    def set(self, index: int, val: int) -> None:
        '''
        sets the element at the given index to be equal to val
        '''
        self.history[index].append([self.id, val])

    def snap(self) -> int:
        '''
        takes a snapshot of the array and returns the snap_id: the total number of times we called snap() minus 1
        '''
        self.id += 1
        return self.id - 1

    def get(self, index: int, snap_id: int) -> int:
        '''
        returns the value at the given index, at the time we took the snapshot with the given snap_id
        '''
        ix = bisect_right(self.history[index], snap_id, key = lambda x: x[0])
        return self.history[index][ix - 1][1]

# Your SnapshotArray object will be instantiated and called as such:
# obj = SnapshotArray(length)
# obj.set(index,val)
# param_2 = obj.snap()
# param_3 = obj.get(index,snap_id)