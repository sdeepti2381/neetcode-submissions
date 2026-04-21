class Solution:
    def isValid(self, s: str) -> bool:

        stack = []

        for c in s:
            # if c is a closing bracket check if the
            # last element is the corresponding opening
            # bracket
            if (len(stack) == 0) and (c in [']', '}', ')']):
                return False
            elif c == ']' and stack[-1] == '[':
                stack.pop()
            elif c == '}' and stack[-1] == "{":
                stack.pop()
            elif c == ')' and stack[-1] == "(":
                stack.pop()
            else:
                # if c is a opening bracket, append it
                stack.append(c)
        
        return len(stack) == 0





        