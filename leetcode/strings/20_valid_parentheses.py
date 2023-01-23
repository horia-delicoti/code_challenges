# 20. Valid Parentheses
# Given a string s containing just the characters '(', ')', '{', '}', '[' and ']', determine if the input string is valid.
# An input string is valid if:
#  1. Open brackets must be closed by the same type of brackets.
#  2. Open brackets must be closed in the correct order.
#  3. Every close bracket has a corresponding open bracket of the same type.


# We are going to use python's built-in data structure list that can be used as a stack.
# - instead of push(), append() is used to add elements to the top of the stack
# - pop() removes the element in the LIFO order

left_pairs = ['(', '[', '}']
right_pairs = [')', ']', '}']

def isValid(string):
    """
    :type s: str
    :rtype: bool
    """

    # The stack to keep track of opening brackets.
    stack = []

    # Hash map for keeping track of mappings. This keeps the code very clean.
    # Also makes adding more types of parenthesis easier
    mapping = {")": "(", "}": "{", "]": "["}

    # For every bracket in the expression.
    for char in string:

        # If the character is an closing bracket
        if char in mapping:

            # Pop the topmost element from the stack, if it is non empty
            # Otherwise assign a dummy value of '#' to the top_element variable
            top_element = stack.pop() if stack else '#'

            # The mapping for the opening bracket in our hash and the top
            # element of the stack don't match, return False
            if mapping[char] != top_element:
                return False
        else:
            # We have an opening bracket, simply push it onto the stack.
            stack.append(char)

    # In the end, if the stack is empty, then we have a valid expression.
    # The stack won't be empty for cases like ((()
    return not stack

characters = "([)]"
print(isValid(characters))