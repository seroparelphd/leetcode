class Solution(object):
    def countStudents(self, students, sandwiches):
        """
        :type students: List[int]
        :type sandwiches: List[int]
        :rtype: int
        """
        
        students = deque(students)
        sandwiches = deque(sandwiches)

        # continues until none of the queue students want to take the top sandwich and are thus unable to eat
        while sandwiches and students:
            if sandwiches[0] in students:
                # If the student at the front of the queue prefers the sandwich on the top of the stack
                if students[0] == sandwiches[0]:
                    # they will take it and leave the queue
                    students.popleft()
                    sandwiches.popleft()
                # Otherwise, they will leave it and go to the queue's end
                else:
                    students.append(students.popleft())
            else:
                return len(students)
        return len(students)