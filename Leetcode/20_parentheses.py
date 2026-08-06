class Solution(object):
    def isValid(self, s):
        """
        :type s: str
        :rtype: bool
        """
        # Map matching close brackets to open brackets
        bracket_map = {')': '(', '}': '{', ']': '['}
        stack = []

        for char in s:
            if char in bracket_map:
                # If stack is not empty, pop top element; otherwise set a dummy value
                top_element = stack.pop() if stack else '#'
                
                # If mapped open bracket doesn't match popped element, return False
                if bracket_map[char] != top_element:
                    return False
            else:
                # If it's an opening bracket, push to stack
                stack.append(char)

        # If stack is empty, all brackets were validly closed
        return not stack
        