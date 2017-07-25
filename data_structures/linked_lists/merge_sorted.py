import sys

"""
 Merge two linked lists
 head could be None as well for empty list
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


def MergeLists(a, b):
    if not a:
        return b
    if not b:
        return a

    if a.data < b.data:
        return Node(a.data, MergeLists(a.next, b))
    else:
        return Node(b.data, MergeLists(a, b.next))


def link_nodes(data):
    if data:
        return Node(data.pop(0), link_nodes(data))

    return None

n = int(input().strip())
input_a = [int(i) for i in input().strip().split(' ')]
head_a = link_nodes(input_a)

m = int(input().strip())
input_b = [int(i) for i in input().strip().split(' ')]
head_b = link_nodes(input_b)

head = MergeLists(head_a, head_b)
cur_node = head

while cur_node.next:
    sys.stdout.write("%d -> " % cur_node.data)
    cur_node = cur_node.next
sys.stdout.write(str(cur_node.data))
