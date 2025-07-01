def backspaceCompare(s, t):

    def process_string(string):
        stack = []
        backspace = "#"
        for char in string:
            if char != backspace:
                stack.append(char)
            elif char == backspace and stack:
                stack.pop()
        return stack
    
    return process_string(s) == process_string(t)

s = "ab#c"
t = "ad#c"

s1 = "ab##"
t1 = "c#d#"

s2 = "a#c"
t2 = "b"

s3 = "a##c"
t3 = "#a#c"
print(backspaceCompare(s, t))
print(backspaceCompare(s1, t1))
print(backspaceCompare(s2, t2))
print(backspaceCompare(s3, t3))