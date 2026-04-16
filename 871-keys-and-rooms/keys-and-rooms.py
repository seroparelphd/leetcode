class Solution:
    def canVisitAllRooms(self, rooms: List[List[int]]) -> bool:
        visited = {0}
        stack = [0]
        while stack:
            current = stack.pop()
            for key in rooms[current]:
                if key not in visited:
                    visited.add(key)
                    stack.append(key)
        print(visited)
        print(rooms)
        return len(visited) == len(rooms)