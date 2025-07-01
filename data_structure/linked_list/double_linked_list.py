# A doubly linked list is like a singly linked list, but each node also contains a pointer to the previous node.
# This pointer is usually called prev, and it allows iteration in both directions.

# In a singly linked list, we needed a reference to the node at i - 1 if we wanted to add or remove at i.
# This is because we needed to perform operations on the prevNode. With a doubly linked list, we only need a
# reference to the node at i. This is because we can simply reference the prev pointer of that node to get the
# node at i - 1, and then do the exact same operations as above.

# With a doubly linked list, we need to do extra work to also update the prev pointers.

class ListNode:
    def __init__(self, val):
        self.val = val
        self.next = None
        self.prev = None

# Let node be the node at position i
def add_node(node, node_to_add):
    prev_node = node.prev
    node_to_add.next = node
    node_to_add.prev = prev_node
    prev_node.next = node_to_add
    node.prev = node_to_add

def delete_node(node):
    prev_node = node.prev
    next_node = node.next
    prev_node.next = next_node
    next_node.prev = prev_node

def get_middle(head):
    slow = head
    fast = head
    while fast and fast.next:
        slow = slow.next
        fast = fast.next.next
    return slow.val

one = ListNode(1)
two = ListNode(2)
three = ListNode(3)

print(one.val)
print(two.val)
print(three.val)
