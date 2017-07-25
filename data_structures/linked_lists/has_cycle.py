"""
Detect a cycle in a linked list. Note that the head pointer may be 'None' if the list is empty.

A Node is defined as:

    class Node(object):
        def __init__(self, data = None, next_node = None):
            self.data = data
            self.next = next_node
"""

class Node(object):
    def __init__(self, data=None, next_node=None):
        self.data = data
        self.next = next_node

def has_cycle(head):
    if not head:
        return 0

    slow = head
    fast = head

    while fast and fast.next:
        slow = slow.next
        fast = fast.next.next

        if slow is fast:
            return 1

    return 0

a = Node(1, Node(2))
a.next.next = Node(3, a)

b = Node(1, Node(2, Node(3, None)))

print(has_cycle(a))
print(has_cycle(b))
