# 20. Valid Parentheses
# Given a string s containing just the characters '(', ')', '{', '}', '[' and ']', determine if the input string is valid.
# An input string is valid if:
#  1. Open brackets must be closed by the same type of brackets.
#  2. Open brackets must be closed in the correct order.
#  3. Every close bracket has a corresponding open bracket of the same type.


# We are going to use python's built-in data structure list that can be used as a stack.
# - instead of push(), append() is used to add elements to the top of the stack
# - pop() removes the element in the LIFO order

def isValid(string):

    # The stack to keep track of opening brackets.
    stack = []

    # Hash map for keeping track of mappings. This keeps the code very clean.
    # Also makes adding more types of parenthesis easier
    mapping = {")": "(", "}": "{", "]": "["}

    # For every bracket in the expression.
    for char in string:

        # If the character is an closing bracket
        if char in mapping.values():
            stack.append(char)

        elif char in mapping.keys():
            if not stack or stack.pop() != mapping[char]:
                return False
    
    return len(stack) == 0


characters = "([)"
print(isValid(characters))