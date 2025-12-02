class Solution:
    def isValid(self, s: str) -> bool:
        # stack will hold opening brackets that we have seen
        stack = []

        # map each type of opening bracket to its matching closing bracket
        openToClose = {"(" : ")", "[" : "]", "{" : "}"}

        # iterate over every character in the input string
        for c in s:
            # if c is an opening bracket
            if c in openToClose:          
                # push the opening bracket onto the stack
                stack.append(c)
            # c is a closing bracket
            else:                         
                # if the stack is empty, there is no matching opening bracket
                if not stack:
                    return False
                # pop the last opening bracket we saw
                open_br = stack.pop()
                # use the dictionary to find what closing bracket we EXPECT
                # for this opening bracket; if it doesn't match c, it's invalid
                if openToClose[open_br] != c:
                    return False

        # after processing all characters:
        # if the stack is empty, all opening brackets were matched and closed
        # if the stack is not empty, there are unmatched openings -> invalid
        return not stack