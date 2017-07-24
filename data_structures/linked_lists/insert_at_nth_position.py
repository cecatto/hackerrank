import sys

"""
 Insert Node at a specific position in a linked list
 head input could be None as well for empty list
 Node is defined as

 class Node(object):

   def __init__(self, data=None, next_node=None):
       self.data = data
       self.next = next_node

 return back the head of the linked list in the below method.
"""


class Node(object):
    def __init__(self, data=None, next_node=None):
        self.data = data
        self.next = next_node

# This is a "method-only" submission.
# You only need to complete this method.
def InsertNth(head, data, position):
    cur_pos = 0
    prev_node = None
    cur_node = head

    if head:
        while cur_pos < position and cur_node:
            prev_node = cur_node
            cur_node = cur_node.next
            cur_pos += 1

        if prev_node:
            prev_node.next = Node(data, cur_node)
        else:
            return Node(data, cur_node)
        return head

    return Node(data, None)


n = int(input().strip())
head = None
for i in range(n):
    data, pos = map(int, input().strip().split(' '))
    head = InsertNth(head, data, pos)

cur_node = head
while cur_node.next:
    sys.stdout.write("%d --> " % (cur_node.data))
    cur_node = cur_node.next
sys.stdout.write(str(cur_node.data))






