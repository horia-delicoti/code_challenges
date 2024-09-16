# 
#
# 
# Time Complexity: Can add and remove elementes at any position in O(1)
# Advantage: No need to have a fixed size
# Disadvantage: No random access; Require O(n) to access an element at a given position
# Overhead: every element need to have extra storage for the pointers

class ListNode:
    def __init__(self, val):
        self.val = val
        self.next = None

one = ListNode(1)
two = ListNode(2)
three = ListNode(3)

one.next = two
two.next = three
head = one

print(head.val)
print(head.next.val)
print(head.next.next.val)
