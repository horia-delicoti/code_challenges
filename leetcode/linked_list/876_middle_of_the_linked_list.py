# Given the head of a singly linked list, return the middle node of the linked list.
# If there are two middle nodes, return the second middle node.
# 
# Input: head = [1,2,3,4,5]
# Output: [3,4,5]
# Explanation: The middle node of the list is node 3.

def middleNode(head):
    arr = [head]
    while arr[-1].next:
        arr.append(arr[-1].next)
    return arr[len(arr) // 2]



head = [1,2,3,4,5,6]
middleNode(head)





# Time Commplexity: O(n)  // We need to iterate over n letters in our linked list
# Space Complexity: O(n)  // We keep a copy of n values in our array